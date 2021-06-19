#!/usr/bin/env python3

"""
该模块对LTS系统抽象一颗LTSTree，使用树来表示LTS
"""

import queue
from lib.action import ActionEnum
from lib.node import Node
from lib.state import State as LtsState
from typing import List
import queue


class LTSTree:
    """
    类LTSTree使用树的形式来抽象表示LTS系统
    """
    def __init__(self, root: Node):
        """
        :param root: 树的根节点
        """
        self.__root = root
        self.__paths = []

    def io_conform(self, other) -> bool:
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

    def after_trace(self, trace):
        """

        :param trace: 动作的序列集合
        :return: 状态对象的集合
        """
        if not self.root:
            return None

    # 可能需要回溯算法, 需要研究
    def _tree_path(self):
        """
        求树的路径
        :return:
        """

        def dfs(root):
            if not root:
                # self.paths.append(''.join(path))
                return
            if not root.action:
                path.append('')
            elif root.action.action_type == ActionEnum.INTERNAL:
                path.append('#')
            else:
                path.append(root.action.action_name)

            if root.children:
                for child in root.children:
                    dfs(child)
                    self.paths.append(''.join(path))
                    path.pop()

        path = []
        self.paths = []
        dfs(self.root)

    def init_p(self):
        """
        init(p) = {a 属于L | p =a=>}
        :return: init(self.root), Action名字的列表
        """
        if not self.root:
            return []

        stack = list()
        actions = list()
        stack.append(self.root)

        while stack:
            node = stack.pop()
            if node.children:
                for child in node.children:
                    if child.action.action_type == ActionEnum.INTERNAL:
                        stack.append(child)
                    else:
                        actions.append(child.action)

        return [(action.action_name, action.action_type) for action in actions]

    def trace(self):
        """
        获取一棵树的所有路径
        :return: 一颗树的所有路径
        """
        if not self.root:
            return

        q = queue.Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            path = ''
            if not node.action:
                pass
            else:
                if node.action.action_type == ActionEnum.INTERNAL:
                    path += '$'
                else:
                    path += node.action.action_name

            self.__paths.append(path)

    def io_conform2(self, other) -> bool:
        """
        使用另外一种算法来实现io一致性检测
        :param other:  LTSTree实例，一般表示规范的LTS树实例
        :return: if implementation 满足一致性 specification，返回True，否则返回False
        """
        if not self.root or not other.root:
            return False

        return set(self.__paths) <= set(other.paths)

    @property
    def paths(self):
        """
        返回路径
        :return: 返回路径的列表
        """
        return self.__paths

    @paths.setter
    def paths(self, value):
        """
        更新路径
        :param value: 更新的path列表值
        :return: None
        """
        self.__paths = value

    @property
    def root(self) -> Node:
        """
        返回根节点
        :return: 根节点
        """
        return self.__root

    @root.setter
    def root(self, root: Node):
        """
        更新根节点
        :param root: 新的根节点
        :return: None
        """
        self.__root = root

    def out(self, state_name: str) -> List[Node]:
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


def get_quiescent_states(lts_tree) -> List[LtsState]:
    """

    :param lts_tree: LTSTree对象实例
    :return: 返回沉默状态的列表
    """
    states = []
    if not lts_tree.root:
        return states;

    q = list((lts_tree.root,))
    flag = False
    while q:
        for _ in range(len(q)):
            node = q.pop(0)
            if node.children:
                for child in node.children:
                    if (child.action.action_type == ActionEnum.INTERNAL or
                            child.action.action_type == ActionEnum.OUTPUT):
                        flag = True
                    q.append(child)
            if flag:
                states.append(node.state)
            flag = False

    return states
