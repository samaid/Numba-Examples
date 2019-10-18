from numba.typed import Dict
from numba import types, njit
import numpy as np

# Using Python dictionary
d = dict()
d[1] = [1.1, 1.2]
d[2] = [2.2]
d[3] = [3.3, 3.4, 3.5]
print(d)


# Using Numba dictionary is more efficient for passing into compiled region due to lower unboxing overheads
# The Dict.empty() constructs a typed dictionary.
# The key and value typed must be explicitly declared.
nd = Dict.empty(
    key_type = types.int64,
    value_type = types.float64[:]
)

# Assigning key-values using Numpy arrays
nd[1] = np.asarray([1.1, 1.2], dtype='f8')
nd[2] = np.asarray([2.2], dtype='f8')
nd[3] = np.asarray([3.3, 3.4, 3.5], dtype='f8')
print(nd)


@njit
def foo( nd ):
    nd[4] = np.asarray([4.4, 4.5], dtype='f8')
    return nd

print(foo(nd))
