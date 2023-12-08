#!/usr/bin/env python3
'''
Task 9 of AlX
Variable annotations
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Function returns an
    iterable
    '''
    return [(i, len(i)) for i in lst]