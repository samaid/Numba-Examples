from numba import jitclass
from numba import types
from numba.typed import Dict

'''' 
dict_type = types.DictType(types.intp, types.int32)
@jitclass([('dict', dict_type)])
class MyDict(object):
    def __init__(self, dict):
        self.dict = dict

    def append(self, key, value):
        self.dict[key].append(value)
'''

# The Dict.empty() constructs a typed dictionary.
# The key and value typed must be explicitly declared.
d[1] = (1.1, 1.2)
d[2] = (2.2, 2.2)
#d[3] = (3.3, 3.4, 3.5)
print(d)
