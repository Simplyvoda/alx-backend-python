#!/usr/bin/env python3
'''
This module contains a type annotated function
that takes a float as an argument
and returnds a function that multiplers float
by the param passed
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    this function returns a function that multiplies
    a float by the muliplier parameter
    '''
    def multiplier_function(x: float):
        return x * multiplier

    return multiplier_function
