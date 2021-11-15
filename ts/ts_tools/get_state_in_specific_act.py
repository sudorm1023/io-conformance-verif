#!/usr/bin/env python3

"""
该模块中的函数用来获取特定动作迁移的末位状态
"""

from typing import List

from core import State
from ts import IOTS
from confgraph import ts_to_tsgraph
from ts.ts_tools import get_ts_observed_actions


def get_end_state_with_hide_action(iots: IOTS, start_state: State) -> List:
    """
    若迁移系统中包含 a->hide_action->c 或者 a->hide_action->b->hide_action->, 则该函数返回 [b, c]
    :param iots: IOTS 对象
    :param start_state: 开始的状态对象
    :return: 一个集合
    """

    def dfs(state):
        adj = graph.adjlists[state]

        if not adj:
            result.append(state)
            return

        for s, act in adj:
            if act in io_actions:
                return
            else:
                result.append(s)
                dfs(s)

    graph = ts_to_tsgraph(iots)
    io_actions = get_ts_observed_actions(iots)
    result = list()
    dfs(start_state)

    return result
