from numba import jitclass, float32


# 2D point class with constructor
class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(x=' + str(self.x) + ', y=' + str(self.y) + ')\n'

# Here we are creating the instance of the class Point2D
p1 = Point2D(10.0, 10.0)
print(p1)  # Printing invokes __str__

# Here we are creating the instance of Point2D which is compiled by Numba
compiled_class = jitclass([('x', float32), ('y', float32)])(Point2D)  # Compiling in this line
p2 = compiled_class(10.0, 10.0)  # Creating the instance of compiled class
print(p2)  # Invocation of __str__ is not implemented in Numba
print('(x=' + str(p2.x) + ', y=' + str(p2.y) + ')')   # Workaround to print representation of the object
