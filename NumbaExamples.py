# coding=utf-8
from numba import jitclass, float32, njit, prange
from numba.typed import List
import numpy.random as rn

# For @jitclass explicit specification of the class argument types is required
# __str__ and __repr__ are not supported by Numba - https://github.com/numba/numba/issues/1606
@jitclass([('x', float32), ('y', float32)])
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(x=' + str(self.x) + ', y=' + str(self.y) + ')\n'

    def __repr__(self):
        return str(self)


@njit(parallel=True)
def init_2d_points(n):
    p = []
    for i in prange(n):
        x = rn.uniform(0.0, 1.0)
        y = rn.uniform(0.0, 5.0)
        p.append(Point2D(x, y))
    return p


# We cannot jit class with List members
# @jitclass(['lst', List])
class MyList:
    def __init__(self, lst):
        self.lst = lst

    def append(self, lst):
        self.lst = self.lst + lst


N_POINTS = 100


def main():
    p = init_2d_points(N_POINTS)
    print(p)
    for i in range(N_POINTS):
        print(p[i].x, p[i].y)

    lst = MyList([1, 2, 3])
    lst.append([4, 5, 6])
    print(lst.lst)


if __name__ == '__main__':
    main()
