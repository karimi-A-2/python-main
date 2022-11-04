# Numpy array basic properties
import numpy as np
a = np.ones(10000)
len(a)
a.shape  # (10000, )
type(a)
a.size  # 10000
a.ndim  # dimension = 1
a.dtype  # dtype('float64')
a.nbytes  # 80000
import sys
sys.getsizeof(a)  # 80112
