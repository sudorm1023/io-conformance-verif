#!/usr/bin/env python3

from ia.interfaceautomat import InterfaceAutomata
from ia.state import State as IaState
from ia.action import Action as IaAction
from lib.action import Action as LtsAction
from lib.state import State as LtsState
from lib.action import ActionEnum
from lib.node import Node
from typing import List


"""
parserlib.common 模块下函数是用来将InterfaceAutomata
实例转换为LTSTree实例时用到的通用函数
"""


def adjust_action_type(ia_: InterfaceAutomata, action: IaAction) -> ActionEnum:
    """
    该函数用来将InterfacAutomata实例转换LTSTree对象时，判断ia中action为LTSTree中对应的类型
    :param ia_: InterfaceAutomata 实例
    :param action: ia.Action对象实例
    :return: lib.ActionEnum实例
    """
    if action in ia_.ins:
        return ActionEnum.INPUT
    elif action in ia_.outs:
        return ActionEnum.OUTPUT
    else:
        return ActionEnum.INTERNAL


def get_node_children(ia_: InterfaceAutomata, state: IaState) -> List[Node]:
    """
    该函数是用来解析ia实例，获取某个起始状态为state的transition的action和end_state
    并将action和end_state封装成Node对象。

    For example:
    ia : s0 -!act1-> s1
    sate: s0
    return [Node(act1, s1)]

    :param ia_: InterfaceAutomata 实例
    :param state: 状态实例
    :return: 一个包含Node对象的列表
    """
    children = []

    # 遍历ia_中transition，获取start_state的Transition
    transitions = ia_.transitions
    for tran in transitions:
        if tran.start_state == state:
            # 获取ia transition中state和action
            action_name = tran.action.action_name
            action_type = adjust_action_type(ia_, tran.action)
            end_state_name = tran.end_state.state_name

            # 构造node对象
            node_state = LtsState(end_state_name)
            node_action = LtsAction(action_name, action_type)
            node = Node(node_action, node_state)
            children.append(node)

    return children


def get_ia_state(ia: InterfaceAutomata, state_name: str) -> IaState:
    """
    根据状态的名字找到ia中对应的State对象
    :param ia: InterfaceAutomata实例
    :param state_name: The name of state
    :return: IaState对象
    """
    for state in ia.states:
        if state.state_name == state_name:
            return state

    return None
