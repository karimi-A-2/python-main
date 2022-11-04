# works fine in pycharm but gives the warning:
# MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
#   plt.plot(np.arange(N), scale)
import matplotlib
matplotlib.use('macosx')

import numpy as np
import matplotlib.pyplot as plt

N = 10
scale = 2 ** np.linspace(-2, 4, N)

plt.plot(np.arange(N), scale)
plt.show()
