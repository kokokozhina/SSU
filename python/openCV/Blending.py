import cv2
import numpy as np,sys
from numpy.core.tests.test_mem_overlap import xrange

A = cv2.imread('Eris.png')
B = cv2.imread('mars.png')
# B = cv2.imread('Mercury.png')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:, 0: int(cols/2)], lb[:, int(cols/2):]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in xrange(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:, : int(cols/2)], B[:, int(cols/2):]))

ls_ = cv2.addWeighted(ls_,0.5,B,0.5,0)
ls_ = cv2.addWeighted(ls_,0.5,A,0.5,0)

cv2.imwrite('Pyramid_blending2.png', ls_)
cv2.imwrite('Direct_blending.png', real)
