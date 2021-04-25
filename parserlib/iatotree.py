#!/usr/bin/env python3

from lib.node import Node
from ia.interfaceautomat import InterfaceAutomata
from lib.lts_tree import LTSTree
from lib.state import State as LtsState


def ia_parser_to_tree(ia: InterfaceAutomata):
    """
    该函数通过InterfaceAutomata的一个实例装换为LtsTree实例
    :param ia: InterfaceAutomata实例对象
    :return: LTSTree实例对象
    """
    init_state = ia.state_init
    root_state = LtsState(init_state.state_name)
    root = Node(None, root_state)

    lts_tree = LTSTree(root)

    #
