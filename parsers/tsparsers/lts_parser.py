#!/usr/bin/env python3

"""
该模块中的函数用来将，以如下文本文件表示的迁移系统：

module-lts euler_rate_to_ang_vel_AC_AttitudeControl:
initial : s0
output sinf : {s0 -> s1}
output cosf : {s1 -> s2}
output cosf : {s2 -> s3}
output sinf : {s3 -> s4}
endmodule-lts

转换为标记迁移系统LTS实例
"""

from ts import LTS
from parsers.tsparsers import parse_initial_state
from parsers.tsparsers import parse_actions
from parsers.tsparsers import parse_states
from parsers.tsparsers import parse_transitions
from core import Action
from core import State
from core import Transition


def lts_parser(file_name: str) -> LTS:
    """
    根据*.ts文件中描述的输入输出迁移系统，生成对应的LTS对象
    :param file_name: .ts结尾的文件
    :return: LTS对象
    """
    init_s = parse_initial_state(file_name)
    s = parse_states(file_name)
    a = parse_actions(file_name)
    t = parse_transitions(file_name)

    # 构造所有状态对象
    states = [State(name) for name in s]
    init_state = [s for s in states if s.state_name == init_s][0]

    actions = a[0]

    # 所有动作的对象
    acts = [Action(name) for name in actions]

    # 动作名到动作的一个映射
    act_map = dict()
    for act in acts:
        act_map[act.action_name] = act

    # 状态名到状态对象的一个映射
    state_map = dict()
    for s in states:
        state_map[s.state_name] = s

    # 构造所有迁移对象集合
    transitions = list()
    for first_state, act, second_state in t:
        transitions.append(Transition(
            state_map[first_state],
            act_map[act],
            state_map[second_state]
        ))

    return LTS(
        init_state,
        states,
        acts,
        transitions
    )
