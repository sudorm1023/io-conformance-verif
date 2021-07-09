#!/usr/bin/env python3

"""
该模块中函数用来检测规范是否满足一致性关系
"""

from typing import List

from confgraph import TsGraph
from core import State
from confgraph import ActionEnum
from ts import LTS
from ts import IOTS
from confgraph import lts_to_graph
from confgraph import iots_to_graph


def lts_traces(ts_graph: TsGraph) -> List[List[str]]:
    """
    从ITS对象生成的TsGraph中获得所有路径
    """

    def dfs(state: State):
        adj = ts_graph.adjlists[state]
        if not adj:
            return

        for s, act in adj:
            paths.append(act.action_name)
            traces.append(list(paths))
            dfs(s)
            paths.pop()

    traces = list()
    paths = list()
    dfs(ts_graph.init_vertex)

    return traces


def iots_traces(ts_graph: TsGraph) -> List[List[str]]:
    """
    从IOTS对象生成的TsGraph中获得所有路径
    """

    def dfs(state: State):
        adj = ts_graph.adjlists[state]
        if not adj:
            return

        for s, act in adj:
            if act.action_type == ActionEnum.OUTPUT or act.action_type == ActionEnum.INPUT:
                paths.append(act.action_name)
            else:
                paths.append(' ')

            traces.append(list(paths))

            dfs(s)
            paths.pop()

    traces = list()
    paths = list()
    dfs(ts_graph.init_vertex)

    return traces


def lts_traces_conformance(spec: LTS, imp: LTS) -> bool:
    """
    测试由LTS表示的实现是有满足前序路径一致性于规范spec

    :param spec: LTS表示的规范对象
    :param imp: LTS表示的实现对象
    :return: 满足返回TRUE，不满足返回False
    """
    imp_graph = lts_to_graph(imp)
    spec_graph = lts_to_graph(spec)

    imp_traces = lts_traces(imp_graph)
    spec_traces = lts_traces(spec_graph)

    imp_traces = set(['.'.join(t) for t in imp_traces])
    spec_traces = set(['.'.join(t) for t in spec_traces])

    return imp_traces <= spec_traces


def iots_traces_conformance(spec: IOTS, imp: IOTS) -> bool:
    """
    测试由LTS表示的实现是有满足前序路径一致性于规范spec

    :param spec: LTS表示的规范对象
    :param imp: LTS表示的实现对象
    :return: 满足返回TRUE，不满足返回False
    """
    imp_graph = iots_to_graph(imp)
    spec_graph = iots_to_graph(spec)

    imp_traces = iots_traces(imp_graph)
    spec_traces = iots_traces(spec_graph)

    imp_traces = set(['.'.join(t) for t in _traces_strip(imp_traces)])
    spec_traces = set(['.'.join(t) for t in _traces_strip(spec_traces)])

    return imp_traces <= spec_traces


def _traces_strip(traces: List[List[str]]) -> List[List[str]]:
    """
    该函数用来除去路径中的空格
    """
    return [[act for act in t if act != ' ']for t in traces]
