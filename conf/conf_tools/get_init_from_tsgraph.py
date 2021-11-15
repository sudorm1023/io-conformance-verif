#!/usr/bin/env python3

"""
该模块中的函数用来从ts中获得init(p)
首先第一步需要将ts转换为TsGraph对象
"""

from typing import List

from confgraph import ts_to_graph
from ts import LTS
from core import State
from ts.ts_tools import get_ts_observed_actions


def get_init(ts: LTS, start_state: State) -> List:
    """
    从ts对象中获取init(p)

    :param ts: 迁移系统对象
    :param start_state: 起始状态对象
    :return: init(start_state)的结果
    """

    def dfs(state: State):
        adj = graph.adjlists[state]

        if not adj:
            return

        for s, act in adj:
            if act in io_acts:
                result.append(act)
                return
            else:
                dfs(s)

    graph = ts_to_graph(ts)
    io_acts = get_ts_observed_actions(ts)  # 可观察动作对象的集合

    init_state = graph.init_vertex

    result = list()
    dfs(init_state)

    return result



