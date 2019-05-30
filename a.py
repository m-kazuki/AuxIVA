import numpy as np

A=np.array([[1,2,3],[-2,3,-1],[-3,-1,5]])
a = np.array([1,2,3])
b = np.array([-2,3,-1])
c = np.array([-3,-1,5])


print(np.linalg.norm(A,2))
print(np.linalg.norm(a,2)+np.linalg.norm(b,2)+np.linalg.norm(c,2))
print(np.zeros(3).shape)