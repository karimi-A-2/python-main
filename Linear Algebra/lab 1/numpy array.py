l = [1, 2, 3]
l

import numpy
a = numpy.array(l)
a
a[2] = 300
a

type(l)
type(a)

import numpy as np
a = np.array(l)
a

a = np.zeros(10)
a
a.dtype
a[2] = 4
a

a = np.zeros(10, dtype=np.int64)
a
a.dtype
a = np.ones(10)
a
a = np.ones(10) * -20
a
np.full(10, 222)
a = np.arange(10)
a
2 ** a
