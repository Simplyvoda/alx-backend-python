#!/usr/bin/env python3
'''
This module contains a function
That has been duck typed
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Function returns none
    or first element of lst
    if available
    '''
    if lst:
        return lst[0]
    else:
        return None
