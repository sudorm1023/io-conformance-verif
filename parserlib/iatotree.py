#!/usr/bin/env python3

from lib.node import Node
from ia.interfaceautomat import InterfaceAutomata
from ia.state import State as IaState
from lib.lts_tree import LTSTree
from lib.state import State as LtsState
from parserlib.common import get_node_children
import queue


def ia_parser_to_tree(ia: InterfaceAutomata) -> LTSTree:
    """
    该函数通过InterfaceAutomata的一个实例装换为LtsTree实例
    :param ia: InterfaceAutomata实例对象
    :return: LTSTree实例对象
    """
    init_state = ia.state_init
    root_state = LtsState(init_state.state_name)
    root = Node(None, root_state)
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        node = q.get()
        ia_state = IaState(node.state.state_name)
        node.children = get_node_children(ia, ia_state)
        if node.children:
            for child in node.children:
                q.put(child)

    lts_tree = LTSTree(root)

    return lts_tree
