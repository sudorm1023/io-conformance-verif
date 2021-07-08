#!/usr/bin/env python

from ts import LTS
from ts import IOTS
from ts import STS
from confgraph import TsGraph


def lts_to_graph(lts: LTS):
    """
    该函数根据LTS对象生成TsGraph对象
    """
    ts_graph = TsGraph()
    ts_graph.init_vertex = lts.init_state
    for transition in lts.transitions:
        adj = (transition.action, transition.end_state)
        ts_graph.adjlists[transition.start_state].append(adj)

    return ts_graph


def iots_to_graph(iots: IOTS):
    pass


def sts_to_graph(sts: STS):
    pass
