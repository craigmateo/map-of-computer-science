from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, List, Optional, TypeVar, Callable

T = TypeVar("T")

@dataclass
class Ops:
    accesses: int = 0
    comparisons: int = 0
    writes: int = 0
    loops: int = 0

    def reset(self) -> None:
        self.accesses = self.comparisons = self.writes = self.loops = 0

class CountedList(Generic[T]):
    """
    Wraps a list and increments counters on read/write.
    This does NOT count every Python-level operation—only the ones we care about.
    """
    def __init__(self, data: Iterable[T], ops: Ops):
        self._data: List[T] = list(data)
        self.ops = ops

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, i: int) -> T:
        self.ops.accesses += 1
        return self._data[i]

    def __setitem__(self, i: int, value: T) -> None:
        self.ops.writes += 1
        self._data[i] = value

    def to_list(self) -> List[T]:
        return list(self._data)

def lt(a: T, b: T, ops: Ops) -> bool:
    ops.comparisons += 1
    return a < b

def le(a: T, b: T, ops: Ops) -> bool:
    ops.comparisons += 1
    return a <= b

def gt(a: T, b: T, ops: Ops) -> bool:
    ops.comparisons += 1
    return a > b

def ge(a: T, b: T, ops: Ops) -> bool:
    ops.comparisons += 1
    return a >= b

def eq(a: T, b: T, ops: Ops) -> bool:
    ops.comparisons += 1
    return a == b
