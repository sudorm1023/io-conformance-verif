#!/usr/bin/env python3

from ia.state import State
from ia.transition import Transition
from typing import List
from ia.action import Action
from typing import Optional


class InterfaceAutomata:
    """
    the class represents Interface Automata
    """

    def __init__(self,
                 state_int: State,
                 states: List[State],
                 ins: List[Action],
                 outs: List[Action],
                 hides: List[Action],
                 trans: List[Transition]):
        """
        :param state_int: The initialize state of IA
        :param states: The list of State
        :param ins: The list of input actions
        :param outs: The list of output actions
        :param hides: The list of hide actions
        :param trans: The list of transitions
        """
        self.__state_init = state_int
        self.__states = states
        self.__ins = ins
        self.__outs = outs
        self.__hides = hides
        self.__transitions = trans

    @property
    def states(self) -> List[State]:
        return self.__states

    @states.setter
    def states(self, states: List[State]):
        self.__states = states

    def add_state(self, state):
        if isinstance(state, list):
            self.__states.extend(state)
        else:
            self.__states.append(state)

    @property
    def ins(self) -> List[Action]:
        return self.__ins

    @ins.setter
    def ins(self, inputs: List[Action]):
        self.__ins = inputs

    def add_in_action(self, inputs):
        if isinstance(inputs, list):
            self.__ins.extend(inputs)
        else:
            self.__ins.append(inputs)

    @property
    def outs(self) -> List[Action]:
        return self.__outs

    @outs.setter
    def outs(self, outputs: List[Action]):
        self.__outs = outputs

    def add_out_action(self, output):
        if isinstance(output, list):
            self.__outs.extend(output)
        else:
            self.__outs.append(output)

    @property
    def hides(self) -> List[Action]:
        return self.__hides

    @hides.setter
    def hides(self, hides: List[Action]):
        self.__hides = hides

    def add_hide_action(self, hide):
        if isinstance(hide, list):
            self.__hides.extend(hide)
        else:
            self.__hides.append(hide)

    @property
    def transitions(self) -> List[Transition]:
        return self.__transitions

    @transitions.setter
    def transitions(self, trans: List[Transition]):
        self.__transitions = trans

    def add_transition(self, tran):
        if isinstance(tran, list):
            self.__transitions.extend(tran)
        else:
            self.__transitions.append(tran)

    @property
    def state_init(self):
        """
        :return: The initial state of IA
        """
        return self.__state_init

    @state_init.setter
    def state_init(self, state: State):
        """
        :param state: Update new initial state
        :return: None
        """
        self.__state_init = state
