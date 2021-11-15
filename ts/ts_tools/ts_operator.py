#!/usr/bin/env python3
"""
该模块中的函数用来对ts对象进行一些操作
"""

from typing import List

from ts import LTS
from ts import IOTS
from ts import STS


def get_ts_observed_actions(ts) -> List:
    """
    该函数用来返回可观察的动作

    :param ts: 迁移系统对象
    :return: 返回可观察动作对象的集合
    """
    if type(ts) == LTS:
        return list(ts.actions - ts.hide_actions)
    elif type(ts) == IOTS:
        return list(ts.input_actions + ts.output_actions)
    elif type(ts) == STS:
        return list(ts.input_actions + ts.output_actions)

    return []

