# coding=utf-8
from numba import jitclass, float32

from numba import jitclass
from numba import types
from numba.typed import Dict


@jitclass([('d', types.DictType(types.intp, types.float64))])
class DictWrapper(object):
    def __init__(self):
        d = Dict()
        d[1] = 1.2
        self.d = d


dw = DictWrapper()
print(dw.d)

def main():


if __name__ == '__main__':
    main()
