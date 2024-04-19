import time
import numpy as np

N = 10**8
a = []
# list of 10 million numbers
for _ in range(N):
  a.append(random.randint(1, N))

start = time.perf_counter()
a.sort()
end = time.perf_counter()
print(f"classic took {end-start}")

a = np.random.randint(1, N, N)
start = time.perf_counter()
a.sort()
end = time.perf_counter()
print(f"NumPy took {end-start}")


import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a, type(a))
print(a+2)
print(a/2)
print(a+a)
print(a**2)
a

a = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10]])
print(a)
print(f"{a.ndim}, {a.size}, {a.shape}, {a.dtype}\n")

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a)
print(f"{a.ndim}, {a.size}, {a.shape}, {a.dtype}")

[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
2, 10, (2, 5), int64

[[1 2 3]
 [4 5 6]
 [7 8 9]]
2, 9, (3, 3), int64

a0 = np.zeros((4,10))
a1 = np.ones((2, 3, 4))
print(a0)
print(a1)
a11 = np.ones((2, 3, 4), dtype=np.int16)
print(a11)
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
[[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]]
[[[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]

 [[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]]
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print(a1+a2, a1*a2, "\n")
a1 = np.array([[1, 2, 3], [4, 5, 6]])
print(a1+a2)
print("\n\n")


print(10/a1)
print(a1 * 2.5)
print(a1 > 3)