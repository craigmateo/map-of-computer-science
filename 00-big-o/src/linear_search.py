from typing import TypeVar, Optional
from counter import CountedList, Ops, eq

T = TypeVar("T")

def linear_search(arr: CountedList[T], target: T, ops: Ops) -> Optional[int]:
    for i in range(len(arr)):
        ops.loops += 1
        if eq(arr[i], target, ops):
            return i
    return None