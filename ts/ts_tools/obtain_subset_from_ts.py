#!/usr/bin/env python3

"""
该模块用来从一个ts迁移系统中获取所有的ts集合

例如，有一个迁移系统 a->1->b, a->2->c, 则该模块内的函数返回a->1->b, a->2->c
"""

from typing import List

from ts import IOTS
from confgraph import ts_to_tsgraph
from core import State
from core import Action
from core import Transition
from confgraph import ActionEnum


def _transition_list_iots(trans_list: List) -> IOTS:
    if not trans_list:
        return

    old_init_state = trans_list[0][0]
    ins = set()
    outs = set()
    acts = set()
    states = set()

    for s1, act, s2 in trans_list:
        if act.action_type == ActionEnum.INPUT:
            ins.add(act.action_name)
        elif act.action_type == ActionEnum.OUTPUT:
            outs.add(act.action_name)
        acts.add(act.action_name)
        states.add(s1.state_name)
        states.add(s2.state_name)

    acts_map = dict()
    states_map = dict()

    states = [State(s) for s in list(states)]
    acts = [Action(a) for a in list(acts)]

    for s in states:
        states_map[s.state_name] = s

    for a in acts:
        acts_map[a.action_name] = acts

    new_init_state = states_map[old_init_state.state_name]
    outs = [acts_map[a] for a in list(outs)]
    ins = [acts_map[a] for a in list(ins)]
    transitions = list()

    for s1, act, s2 in trans_list:
        t = Transition(states_map[s1.state_name],
                       acts_map[act.action_name],
                       states_map[s2.state_name])
        transitions.append(t)

    return IOTS(new_init_state,
                states,
                acts,
                ins,
                outs,
                transitions)


def obtian_subset_from_iots(iots: IOTS) -> List[IOTS]:
    """
    获取IOTS对象的所有迁移的子集
    :param iots:
    :return:
    """

    def dfs(state: State):
        adj = graph.init_vertex[state]
        if not adj:
            return

        for s, act in adj:
            paths.append([state, act, s])
            result.append(list(paths))
            dfs(s)
            paths.pop()

    graph = ts_to_tsgraph(iots)
    init_state = graph.init_vertex
    result = list()
    paths = list()

    dfs(init_state)
    result = [_transition_list_iots(s) for s in result]
    return result






