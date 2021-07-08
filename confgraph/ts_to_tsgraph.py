#!/usr/bin/env python

from ts import LTS
from ts import IOTS
from ts import STS
from confgraph import TsGraph

import enum


def lts_to_graph(lts: LTS):
    """
    该函数根据LTS对象生成TsGraph对象

    :param lts: LTS对象
    """
    ts_graph = TsGraph()
    ts_graph.init_vertex = lts.init_state
    for transition in lts.transitions:
        adj = (transition.end_state, transition.action)
        ts_graph.adjlists[transition.start_state].append(adj)

    return ts_graph


class ActionEnum(enum.Enum):
    """
    对IOTS系统中Action进行区分：
    0 表示输入动作
    1 表示输出动作
    2 表示内部动作
    """
    INPUT = 0
    OUTPUT = 1
    INTERNAL = 2


def iots_to_graph(iots: IOTS):
    """
    该函数根据IOTS对象生成TsGraph对象

    :param iots: IOTS对象
    """
    ts_graph = TsGraph()
    ts_graph.init_vertex = iots.init_state
    for transition in iots.transitions:
        first_state = transition.start_state
        action = transition.action
        second_state = transition.end_state

        # 设置动作的属性，是输入动作还是输出动作，或者是内部动作
        if action in iots.output_actions:
            action.action_type = ActionEnum.OUTPUT
        elif action in iots.input_actions:
            action.action_type = ActionEnum.INPUT
        else:
            action.action_type = ActionEnum.INTERNAL

        adj = (second_state, action)
        ts_graph.adjlists[first_state].append(adj)

    return ts_graph
