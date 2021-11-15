#!/usr/bin/env python3

"""
测试用例生成模块
"""

from ts import IOTS
from ts import Testcase
from ts.ts_tools import get_end_state_with_hide_action
from conf.conf_tools import get_init
from ts.ts_tools import obtian_subset_from_iots


def iots_testcase_generate(iots: IOTS) -> Testcase:
    """
    该函数根据iots对象生成testcase
    """
    init_state = iots.init_state
    states = iots.states
    acts = iots.actions
    ins = iots.input_actions
    outs = iots.output_actions
    transitions = iots.transitions
    verdict = dict()

    init = get_init(iots, iots.init_state)  # init(iots.init_state)
    hide_transitions_start_with_init_state = get_end_state_with_hide_action(iots, iots.init_state)
    iots_subset = obtian_subset_from_iots(iots)

    return Testcase(
        init_state,
        states,
        acts,
        ins,
        outs,
        transitions,
        verdict
    )
