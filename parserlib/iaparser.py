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

# global states action transitions
globals_states = None
globals_input_actions = None
globals_output_actions = None
globals_hide_actions = None
globals_transitions = None


def _get_ia_rep_list(ia_rep: str) -> List[str]:
    """
    对IA表示的字符串进行预处理
    :param ia_rep: 字符串表示的Ia
    :return: 一个字符串列表
    """
    ia_rep = ia_rep.strip('\n')
    ia_rep_list = ia_rep.split('\n')
    return ia_rep_list


def _get_states(ia_rep: str) -> List[IaState]:
    """

    :param ia_rep: 字符串表示的ia
    :return: 状态实例的集合
    """
    states = []  # State实例列表
    states_str = set()  # states_名字的集合

    ia_rep_list = _get_ia_rep_list(ia_rep)

    if len(ia_rep_list) <= 3:
        print("[!] Error: bad representation!!!")
        return False

    # 将文本字符串表示ia的state名称保存到states_str集合中
    for line in ia_rep_list[2:-1]:
        line = line.strip()
        match = re.search(r'{.*}', line)
        if not match:
            print('[!] Error: error match in _get_states()')

        result = match.group()
        first_state = result[1:-1].split()[0]
        second_state = result[1:-1].split()[-1]
        states_str.add(first_state)
        states_str.add(second_state)

    for state_str in states_str:
        states.append(IaState(state_str))

    global globals_states
    globals_states = states

    return True


def _get_actions(ia_rep: str, action_type: str):
    """
    获取对应动作的Action实例集合
    :param ia_rep: 字符串表示的ia
    :param action_type: 动作的类型：主要有3中：input、output、hide
    :return:
    """
    actions = []

    ia_rep_list = _get_ia_rep_list(ia_rep)

    if len(ia_rep_list) <= 3:
        print("[!] Error: bad representation!!!")
        return False

    for line in ia_rep_list[2:-1]:
        line = line.strip()
        line_list = line.split(maxsplit=2)
        action_type_ = line_list[0].strip()
        action_name = line_list[1].strip()

        if action_type_ == action_type:
            actions.append(IaAction(action_name))

    if action_type == 'input':
        global globals_input_actions
        globals_input_actions = actions
    elif action_type == 'output':
        global globals_output_actions
        globals_output_actions = actions
    elif action_type == 'hide':
        global globals_hide_actions
        globals_hide_actions = actions

    return True


def _get_specific_state(states: List[IaState], state_name: str):
    """
    返回状态名字为state_name的State对象
    :param states: IaState对象的集合
    :param state_name: 状态的名字
    :return: 名字为state_name的State对象
    """
    return [state for state in states if state.state_name == state_name][0]


def _get_specific_action(actions: List[IaAction], action_name: str):
    """
    返回状态名字为action_name的Action对象
    :param actions: IaAction对象集合
    :param action_name: 动作的名字
    :return: 名字为action_name的Action对象
    """
    return [action for action in actions if action.action_name == action_name][0]


def _get_transitions(ia_rep: str) -> List[IaTransition]:
    transitions = []

    if not globals_states:
        _get_states(ia_rep)

    if globals_hide_actions is None:
        _get_actions(ia_rep, 'hide')

    if globals_input_actions is None:
        _get_specific_action(ia_rep, 'input')

    if globals_output_actions is None:
        _get_actions(ia_rep, 'output')

    ia_rep_list = _get_ia_rep_list(ia_rep)

    if len(ia_rep_list) <= 3:
        print("[!] Error: bad representation!!!")
        return False

    for line in ia_rep_list[2:-1]:
        line = line.strip()
        state_match = re.search(r'{.*}', line)
        if not state_match:
            print('[!] Error: error match in _get_states()')

        result = state_match.group()
        # 解析转换的状态的名字
        first_state = result[1:-1].split()[0]
        second_state = result[1:-1].split()[-1]

        first_state_obj = _get_specific_state(globals_states, first_state)
        second_state_obj = _get_specific_state(globals_states, second_state)

        # 解析转换动作的名字
        action_type = line.split(maxsplit=2)[0].strip()
        action_name = line.split(maxsplit=2)[1].strip()

        action_obj = None
        if action_type == 'hide':
            action_obj = _get_specific_action(globals_hide_actions, action_name)
        elif action_type == 'output':
            action_obj = _get_specific_action(globals_output_actions, action_name)
        elif action_type == 'input':
            action_obj = _get_specific_action(globals_input_actions, action_name)

        transitions.append(IaTransition(first_state_obj, action_obj, second_state_obj))

    global globals_transitions
    globals_transitions = transitions

    return True


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
    _get_states(ia_rep)  # state集合
    init_s = ia_rep_list[1].split(':')[1].strip()
    init_state = [state for state in globals_states if init_s == state.state_name][0]  # initial state
    _get_actions(ia_rep, 'input')
    _get_actions(ia_rep, 'output')
    _get_actions(ia_rep, 'hide')
    _get_transitions(ia_rep)
    ia = InterfaceAutomata(init_state,
                           globals_states,
                           globals_input_actions,
                           globals_output_actions,
                           globals_hide_actions,
                           globals_transitions)

    return ia





