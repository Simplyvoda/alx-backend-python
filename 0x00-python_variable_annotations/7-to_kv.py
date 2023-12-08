#!/usr/bin/env python3
'''
This module contains a function that takes
a string and an integer or float and returns
a tuple
'''
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    This function returns a tuple
    containing a string and square of
    second parameter
    '''
    computed_tuple = (k, v*v)
    return computed_tuple
