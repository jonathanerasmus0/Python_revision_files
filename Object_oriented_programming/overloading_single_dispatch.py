from functools import singledispatch, singledispatchmethod
from typing import Any

@singledispatch #decorator
def func(arg: Any, Verbose=False):
    raise NotImplementedError(f'Type: {type(arg)} cannot be used with functions
    