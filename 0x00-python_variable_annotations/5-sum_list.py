#!/usr/bin/env python3
'''
This module contains a type- annotated function
This function takes a list of floats
and returns their sum
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Returns sum of float list items
    '''
    return sum(input_list)
