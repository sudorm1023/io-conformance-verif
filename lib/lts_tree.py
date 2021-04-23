#!/usr/bin/env python3

"""
该模块对LTS系统抽象一颗LTSTree，使用树来表示LTS
"""

import queue
from lib.action import ActionEnum


class LTSTree:
    """
    类LTSTree使用树的形式来抽象表示LTS系统
    """
    def __init__(self, root):
        """
        :param root: 树的根节点
        """
        self.__root = root

    def io_conform(self, other):
        """
        对LTS系统进行一致性检测，检查实现是否io一致性规范
        :param other: LTSTree实例，一般表示规范的LTS树实例
        :return: if implementation 满足一致性 specification，返回True，否则返回False
        """
        if not self.root or not other.root:
            return False
        q = queue.Queue()
        q.put(self.root)
        flag = True

        while not q.empty():
            node = q.get()

            # 判断根节点和其他节点
            if not node.action:
                pass
            else:
                flag = self.after(node.action.action_name, node.action.action_type).issubset(other.after(
                    node.action.action_name, node.action.action_type))
            if not flag:
                return False

            if node.children:
                for child in node.children:
                    q.put(child)

        return flag

    @property
    def root(self):
        """
        返回根节点
        :return: 根节点
        """
        return self.__root

    @root.setter
    def root(self, root):
        """
        更新根节点
        :param root: 新的根节点
        :return: None
        """
        self.__root = root

    def out(self, state_name: str):
        """
        根据该定义获得 out(q) =def { x∈LU | q −−x→ } ∪ { δ | δ(q) }
        也就是获取获取存在output action 转换的节点
        :param state_name: 需要找到的状态名字为state_name
        :return: 返回node中动作类型为OUT的节点
        """
        nodes_list = []  # 保存符合要求的节点

        if not self.root:
            return nodes_list

        node = None
        queue_ = queue.Queue()
        queue_.put(self.__root)

        # 找到node中的state对象的name为state_name的node对象
        while not queue_.empty():
            node = queue_.get()
            if node.state.state_name == state_name:
                break

            if node.children:
                for child in node.children:
                    queue_.put(child)

        if node.children:
            for child in node.children:
                if child.action.action_type == ActionEnum.OUTPUT:
                    nodes_list.append(child)

        return nodes_list

    def out_all(self, state_name_list: list):
        """
        out(Q) =def U { out(q) | q∈Q }
        找到一个state集合中所有的out(state)
        :param state_name_list:
        :return: 一个集合，包含了符合state_name_list的集合
        """
        nodes_list = []
        if not self.__root:
            return nodes_list

        for state_ in state_name_list:
            state_out = self.out(state_)
            if state_out:
                nodes_list.extend(state_out)

        return nodes_list

    def after(self, action_name: str, action_type: ActionEnum):
        """
        返回特定动作之后的集合
        :param action_name:
        :param action_type:
        :return:
        """
        action_set = set()

        if not self.__root:
            return action_set

        q = queue.Queue()
        q.put(self.__root)
        node = None

        while not q.empty():
            node = q.get()
            if not node.action:
                pass
            elif node.action.action_type == action_type and node.action.action_name == action_name:
                break

            if node.children:
                for child in node.children:
                    q.put(child)

        # 使用out求得该结点的out()集合
        nodes = self.out(node.state.state_name)
        for node_ in nodes:
            action_set.add(node_.action.action_name)

        return action_set
