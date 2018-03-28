import numpy
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('image.jpg')
#img1 = cv2.flip(img, 1) 
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)

#Применить различные линейные преобразования к картинке.
#Применим сглаживание или размытие (blurring).

#1. Применение однородного размытия (Blur).
blur = cv2.blur(img, (7, 7))
cv2.imshow('Blur', blur)

#2. Гауссовский фильтр (Gaussian Filter).
gaussian = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow('Gaussian Filter', gaussian)

#3. Средний фильтр (Median Filter).
median = cv2.medianBlur(img, 7)
cv2.imshow('Median Filter', median)

#4. Двусторонний фильтр (Bilateral Filter).
bilateral = cv2.bilateralFilter(img, 7, 27, 3)
cv2.imshow('Bilateral Filter', bilateral)

#Построить гистограмму - распределение цветов.
color = ('b','g','r')
for i, col in enumerate(color):
   hist = cv2.calcHist([img], [i], None, [256], [0, 256])
   plt.plot(hist, color = col)
   plt.xlim([0, 256])

hist = cv2.calcHist(img, [0], None, [256], [0, 256])
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
