#!/usr/bin/env python3

"""
该模块对LTS系统抽象一颗LTSTree，使用树来表示LTS
"""


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
        return True

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
