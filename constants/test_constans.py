#!/usr/bin/env python3

"""
该模块用来构建一些简单的迁移系统对象常量，方便进行测试程序的正确性
"""

from core import Action
from core import State
from core import Transition
from ts import IOTS

"""
SIMPLE_IOTS 表示如下迁移系统：
s0->act1?->s1
s1->act2!->s2
s1->act3!->s3
"""

s0, s1, s2, s3 = (State(s) for s in ("s0", "s1", "s2", "s3"))
act1, act2, act3 = (Action(a) for a in ("act1", "act2", "act3"))

states = [s0, s1, s2, s3]
actions = [act1, act2, act3]
ins = [act1]
outs = [act2, act3]
transitions = [Transition(s0, act1, s1), Transition(s1, act2, s2), Transition(s1, act3, s3)]

SIMPLE_IOTS_TEST = IOTS(s0, states, actions, ins, outs, transitions)
