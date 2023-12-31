#!/usr/bin/env python3
'''
This module contains a type-annotated function
that takes a list of integer and floats
and returns their sum as a float
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    This function returns the sum of a mixed type
    list
    '''
    return float(sum(mxd_lst))
