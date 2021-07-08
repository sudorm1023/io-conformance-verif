#!/usr/bin/env python3

"""
该模块将标记迁移系统用图的邻接表表示
"""

from ts import LTS


class LtsGraph:
    """
        该类用用来讲一个标记迁移系统对象转换为LtsGraph对象
    """

    def __init__(self):
        """
        self.__adjs保存是一个字典，保存了顶点与另外一个顶点的映射关系，假设，有如下简单图：
        a -2-> b, 其中2是权重，则self.adjs = {a: (b, 2)}，
        self.__init_vertex表示一个初始顶点，遍历都从这里开始
        """
        self.__adjlists = dict()
        self.__init_vertex = None

    @property
    def init_vertex(self):
        """
        :return: 返回初始节点
        """
        return self.__init_vertex

    @init_vertex.setter
    def init_vertex(self, vertex):
        self.__init_vertex = vertex

    @property
    def adjlists(self):
        """
        :return: 返回图中连接表关系的集合
        """
        return self.__adjlists

    @adjlists.setter
    def adjlists(self, adjs):
        self.__adjlists = adjs

