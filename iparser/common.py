#!/usr/bin/env python3

"""
该模块包含解析*.si文件和*.i文件中通用的操作
"""

import os.path
from typing import List
from typing import Set
from typing import Tuple
from core import State
import re


def iread(file_name: str) -> str:
    """
    该函数用来读取接口文件
    """
    if not os.path.exists(file_name):
        print("[!] Error: {} is not exist!".format(os.path.abspath(file_name)))
        exit(0)

    with open(file_name, mode='r') as f:
        return f.read()


def parse_file_to_list(file_name) -> List[str]:
    """
    对迁移系统表示的字符串进行预处理
    :param file_name: .i结尾或者*.si结尾的文件
    :return: 一个字符串列表
    """
    strs = iread(file_name)
    strs = strs.strip('\n')
    return strs.split('\n')


def parse_initial_state(file_name) -> List[str]:
    """
    构造初始状态对象
    """
    file_list = parse_file_to_list(file_name)

    if len(file_list) <= 3:
        print("[!] Error: bad representation!!!")
        exit(0)

    return file_list[1].split(':')[1].strip()


def parse_states(file_name) -> List[str]:
    """
    该函数获取所有状态名的集合

    :param file_name: .i结尾或者*.si结尾的文件
    :return: 所有状态名的集合
    """

    states = set()  # states名字的集合

    file_list = parse_file_to_list(file_name)

    if len(file_list) <= 3:
        print("[!] Error: bad representation!!!")
        exit(0)

    # 将文本字符串表示迁移系统的状态名称保存到states集合中
    for line in file_list[2:-1]:
        line = line.strip()
        match = re.search(r'{.*}', line)
        if not match:
            print('[!] Error: error match in parse_states()')

        result = match.group()
        first_state = result[1:-1].split()[0]
        second_state = result[1:-1].split()[-1]
        states.add(first_state)
        states.add(second_state)

    return states


def parse_actions(file_name) -> List[Set[str]]:
    """
    该函数获取所有动作名的集合

    :param file_name: .i结尾或者*.si结尾的文件
    :return: 所有动作名的集合[[输入动作集合]， [输入动作集合], [内部动作集合]]
    """
    actions = [set(), set(), set()]

    file_list = parse_file_to_list(file_name)

    if len(file_list) <= 3:
        print("[!] Error: bad representation!!!")
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

    return actions


def parser_transitions(file_name) -> List[Tuple[str]]:
    """
    该函数获取所有迁移关系的集合

    :param file_name: .i结尾或者*.si结尾的文件
    :return: 所有迁移的集合[(起始状态，动作，终止状态)]
    """
    transitions = list()

    file_list = parse_file_to_list(file_name)

    if len(file_list) <= 3:
        print("[!] Error: bad representation!!!")
        exit(0)

    for line in file_list[2:-1]:
        line = line.strip()
        state_match = re.search(r'{.*}', line)
        if not state_match:
            print('[!] Error: error match in _get_states()')

        result = state_match.group()
        # 解析转换的状态的名字
        first_state = result[1:-1].split()[0]
        second_state = result[1:-1].split()[-1]

        # 解析动作的名字
        action_name = line.split(maxsplit=2)[1].strip()

        transitions.append((first_state, action_name, second_state))

    return transitions
