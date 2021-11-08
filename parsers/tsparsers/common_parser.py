#!/usr/bin/env python3

from typing import List
from typing import Tuple
import os
import re

from constants import TS_TYPE

"""
该模块主要涉及将*.ts文件转换为迁移系统对象所需要的通用文件
"""


def file_read(file_name: str) -> str:
    """
    该函数用来读取接口文件
    """
    if not os.path.exists(file_name):
        print("\033[31m[!] Error: {} is not exist!\033[0m".format(os.path.abspath(file_name)))
        exit(0)

    with open(file_name, mode='r') as f:
        return f.read()


def parse_file_to_list(file_name) -> List[str]:
    """
    对迁移系统表示的字符串进行预处理
    :param file_name: .i结尾或者*.si结尾的文件
    :return: 一个字符串列表
    """
    text = file_read(file_name)
    text = text.strip('\n')
    return text.split('\n')


def parse_initial_state(file_name) -> List[str]:
    """
    构造初始状态对象
    """
    file_list = parse_file_to_list(file_name)

    if len(file_list) <= 3:
        print("\033[31m[!] Error: bad representation!\033[0m")
        exit(0)

    return file_list[1].split(':')[1].strip()


def parse_states(file_name) -> List[str]:
    """
    该函数获取所有状态名的集合

    :param file_name: .ts结尾的文件
    :return: 所有状态名的集合
    """

    states = set()  # states名字的集合

    file_list = parse_file_to_list(file_name)

    if len(file_list) <= 3:
        print("\033[31m[!] Error: bad representation!\033[0m")
        exit(0)

    # 将文本字符串表示迁移系统的状态名称保存到states集合中
    for line in file_list[2:-1]:
        line = line.strip()
        match = re.search(r'{.*}', line)
        if not match:
            print('\033[31m[!] Error: error match in parse_states()!\033[0m')

        result = match.group()
        first_state = result[1:-1].split()[0]
        second_state = result[1:-1].split()[-1]
        states.add(first_state)
        states.add(second_state)

    return list(states)


def parse_actions_with_iots(file_name) -> List[List[str]]:
    """
    该函数获取所有动作名的集合

    :param file_name: .ts结尾的文件
    :return: 所有动作名的集合[[输入动作集合]， [输入动作集合], [内部动作集合]]
    """
    actions = [set(), set(), set()]

    file_list = parse_file_to_list(file_name)

    if len(file_list) <= 3:
        print("\033[31m[!] Error: bad representation!\033[0m")
        exit(0)

    for line in file_list[2:-1]:
        line = line.strip()
        line_list = line.split(maxsplit=2)
        action_type = line_list[0].strip()
        action_name = line_list[1].strip()

        if action_type == 'input':
            actions[0].add(action_name)
        elif action_type == 'output':
            actions[1].add(action_name)
        else:
            actions[-1].add(action_name)

    actions = [list(act) for act in actions]

    return actions


def parse_actions_with_lts(file_name) -> List[List[str]]:
    """
    该函数获取所有动作名的集合

    :param file_name: .ts结尾的文件
    :return: 所有动作名的集合[[动作集合]]
    """
    actions = [set(), set(), set()]

    file_list = parse_file_to_list(file_name)

    if len(file_list) <= 3:
        print("\033[31m[!] Error: bad representation!\033[0m")
        exit(0)

    for line in file_list[2:-1]:
        line = line.strip()
        line_list = line.split(maxsplit=2)
        action_name = line_list[1].strip()

        actions[0].add(action_name)

    actions = [list(act) for act in actions]

    return actions


def parse_actions_with_sts(file_name) -> List[List[str]]:
    """
    该函数获取所有动作名的集合

    :param file_name: .ts结尾的文件
    :return: 所有动作名的集合[[动作集合]]
    """
    return parse_actions_with_iots(file_name)


def parse_ts_type(file_name) -> str:
    """
    该函数用来解析文件所代表的是哪种类型的迁移系统

    :param file_name: .ts结尾的文件
    :return: 文件类型LTS、IOTS或者STS
    """

    file_list = parse_file_to_list(file_name)
    ts_type_line = file_list[0]
    if "lts" in ts_type_line:
        return "LTS"
    elif "iots" in ts_type_line:
        return "IOTS"
    elif "sts" in ts_type_line:
        return "STS"

    return


def parse_actions(file_name) -> List[List[str]]:
    """
    根据不同的迁移系统选择不同的解析动作的方法
    """

    ts_type = parse_ts_type(file_name)
    if ts_type not in TS_TYPE:
        print("\033[31m[!] Error: type is not exist!\033[0m")
        exit(0)

    if ts_type == "LTS":
        return parse_actions_with_lts(file_name)
    elif ts_type == "IOTS":
        return parse_actions_with_iots(file_name)
    elif ts_type == "STS":
        return parse_actions_with_sts(file_name)

    return


def parse_transitions(file_name) -> List[Tuple[str]]:
    """
    该函数获取所有迁移关系的集合

    :param file_name: .ts结尾的文件
    :return: 所有迁移的集合[(起始状态，动作，终止状态)]
    """
    transitions = list()

    file_list = parse_file_to_list(file_name)

    if len(file_list) <= 3:
        print("\033[31m[!] Error: bad representation!\033[0m")
        exit(0)

    for line in file_list[2:-1]:
        line = line.strip()
        state_match = re.search(r'{.*}', line)
        if not state_match:
            print('\033[31m[!] Error: error match in parser_transitions()\033[0m')

        result = state_match.group()
        # 解析转换的状态的名字
        first_state = result[1:-1].split()[0]
        second_state = result[1:-1].split()[-1]

        # 解析动作的名字
        action_name = line.split(maxsplit=2)[1].strip()

        transitions.append((first_state, action_name, second_state))

    return transitions
