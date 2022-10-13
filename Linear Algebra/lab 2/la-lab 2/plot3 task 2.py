import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
matplotlib.use('macosx')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plot multiple points
u = np.array([1, 2, 3])
v = np.array([2, 0, -2])

xs = [u[0], v[0]]
ys = [u[1], v[1]]
zs = [u[2], v[2]]

# base of the vectors set to the origin
tail_x = [0, 0]
tail_y = [0, 0]
tail_z = [0, 0]

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)

ax.quiver(tail_x, tail_y, tail_z, xs, ys, zs, color='r')

for _ in range(200):
    a, b = np.random.randn(2)
    w = a * u + b * v
    ax.scatter(w[0], w[1], w[2], color='b')

plt.show()

'''
randn(d0, d1, ..., dn)
Return a sample (or samples) from the "standard normal" distribution.
Note
This is a convenience function for users porting code from Matlab, and wraps standard_normal.
That function takes a tuple to specify the size of the output, which is consistent with other NumPy functions like numpy.zeros and numpy.ones.
Note
New code should use the standard_normal method of a default_rng() instance instead; please see the random-quick-start.
If positive int_like arguments are provided,
 randn generates an array of shape (d0, d1, ..., dn),
  filled with random floats sampled from a univariate "normal" (Gaussian) distribution of mean 0 and variance 1.
   A single float randomly sampled from the distribution is returned if no argument is provided.
d0, d1, ..., dn : int, optional
The dimensions of the returned array, must be non-negative. If no argument is given a single Python float is returned.
Z : ndarray or float
A (d0, d1, ..., dn)-shaped array of floating-point samples from the standard normal distribution, or a single such float if no parameters were supplied.
standard_normal : Similar, but takes a tuple as its argument. normal : Also accepts mu and sigma arguments. random.Generator.standard_normal: which should be used for new code.
For random samples from N(μ, σ2), use:
sigma * np.random.randn(...) + mu
>>> np.random.randn()
2.1923875335537315  # random
Two-by-four array of samples from N(3, 6.25):
>>> 3 + 2.5 * np.random.randn(2, 4)
array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
       [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
Returns:
A ``(d0, d1, ..., dn)``-shaped array of floating-point samples from the standard normal distribution, or a single such float if no parameters were supplied.
'''