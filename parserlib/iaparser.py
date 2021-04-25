#!/usr/bin/env python3

"""
该模块中的函数用来将，以如下文本文件表示的interface Automata：

module euler_rate_to_ang_vel_AC_AttitudeControl:
initial : s0
output sinf_L_ : {s0 -> s1}
output cosf_L_ : {s1 -> s2}
output cosf_L_ : {s2 -> s3}
output sinf_L_ : {s3 -> s4}
endmodule

转换为InterfaceInterface实例
"""

from ia.interfaceautomat import InterfaceAutomata
from ia.state import State as IaState
from ia.action import Action as IaAction
from ia.transition import Transition as IaTransition
import re
from typing import List


def _get_states(ia_rep: str) -> List[IaState]:
    """

    :param ia_rep: 字符串表示的ia
    :return: 状态实例的集合
    """
    states = []  # State实例列表
    states_str = set()  # states_名字的集合

    ia_rep = ia_rep.strip('\n')
    ia_rep_list = ia_rep.split('\n')

    # 将文本字符串表示ia的state名称保存到states_str集合中
    for line in ia_rep_list[2:-1]:
        line = line.strip()
        match = re.search(r'{.*}', line)
        if not match:
            print('[!] Error: error match in _get_states()')

        result = match.group()
        first_state = result.split()[0]
        second_state = result.split()[-1]
        states_str.add(first_state)
        states_str.add(second_state)

    for state_str in states_str:
        states.append(IaState(state_str))

    return states


def _get_actions(ia_rep: str, action_type: str):
    """
    获取对应动作的Action实例集合
    :param ia_rep: 字符串表示的ia
    :param action_type: 动作的类型：主要有3中：input、output、hide
    :return:
    """
    actions = []

    ia_rep = ia_rep.strip('\n')
    ia_rep_list = ia_rep.split('\n')

    for line in ia_rep_list:
        line = line.strip()
        line_list = line.split(maxsplit=2)
        action_type_ = line_list[0].strip()
        action_name = line_list[1].strip()

        if action_type_ == action_type:
            actions.append(IaAction(action_name))

    return actions


def _get_specific_state(states: List[IaState], state_name: str):
    """
    返回状态名字为state_name的State对象
    :param states: IaState对象的集合
    :param state_name: 状态的名字
    :return: 名字为state_name的State对象
    """
    return [state.state_name == state_name for state in states][0]


# need to fix program
def _get_transitions(ia_rep: str) -> List[IaTransition]:
    transitions = []

    ia_rep = ia_rep.strip('\n')
    ia_rep_list = ia_rep.split('\n')

    for line in ia_rep_list:
        line = line.strip()
        state_match = re.search(r'{.*}', line)
        if not state_match:
            print('[!] Error: error match in _get_states()')

        result = state_match.group()
        # 解析转换的状态的名字
        first_state = result.split()[0]
        second_state = result.split()[-1]

        # 解析转换动作的名字
        action_name = line.split(maxsplit=1)[0].strip()

        start_state = _get_specific_state()


def ia_parser(ia_rep: str) -> InterfaceAutomata:
    """
    将字符串ia_rep表示的ia转换为InterfaceAutomata实例
    :param ia_rep: 字符串表示的ia
    :return: InterfaceAutomata实例
    """
    if not ia_rep:
        print('[!] Error: The interface automata representation with string is empty')
        exit(0)

    ia_rep = ia_rep.strip('\n')
    ia_rep_list = ia_rep.split('\n')

    # 解析initial state
    states = _get_states(ia_rep)  # state集合
    init_s = ia_rep_list[1].split(':')[1].strip()
    init_state = [init_s == state.state_name for state in states][0]  # initial state
    in_actions = _get_actions(ia_rep, 'input')
    out_actions = _get_actions(ia_rep, 'output')
    hide_actions = _get_actions(ia_rep, 'hide')




