#!/usr/bin/env python3

"""
将要实现的一致性检测算法需要通过树的遍历来完成，
因此，需要定义树的节点，每个结点点包含两部分信息：状态结点和动作这个部分的信息。

比如，如下图所示的简单LTS：
      s0
  i? / \ o!
    s1  s2

上面的LTS需要3个Node
Node 0 : {state:s0, action:Node}
Node 1 : {state:s1, action:i?}
Node 2 : {state:s2, action:o!}
"""

from lib.action import Action
from lib.state import State
from typing import List


class Node:
    """
    Node节点的表示
    """
    def __init__(self, action: Action, state: State):
        """

        :param action: Node中Action实例
        :param state: Node中state实例
        """
        self.__action = action
        self.__state = state
        self.__children = None

    @property
    def state(self):
        """
        :return: 返回Node结点中的state实例
        """
        return self.__state

    @state.setter
    def state(self, state: State):
        """
        更新state实例
        :param state: State实例
        :return: None
        """
        self.__state = state

    @property
    def action(self):
        """
        :return: 返回Node节点中的action实例
        """
        return self.__action

    @action.setter
    def action(self, action: Action):
        """
        更新action实例
        :param action: Action实例
        :return: None
        """
        self.__action = action

    @property
    def children(self):
        """
        该Node节点的孩子节点的集合
        :return: 孩子节点的集合
        """
        return self.__children

    @children.setter
    def children(self, children: List):
        """
        更新该结点的孩子结点集合
        :param children: 孩子结点的集合
        :return: None
        """
        self.__children = children

