# -*- coding: utf-8 -*-
import numpy as np
import cv2

image = cv2.imread("strongbox.dng")
image_lab = cv2.cvtColor(image, cv2.COLOR_RGB2Lab)


image_lab2 = np.array(image_lab, dtype=np.float32) - 124
image_lab2[:, :, 2] *= 1.5
# image_lab2[:, :, 1] *= 1.05

image_lab2 += 124

i3 = np.array(image_lab2, dtype=np.uint8)

result = cv2.cvtColor(i3, cv2.COLOR_LAB2RGB)
cv2.imwrite("strongbox.jpg", result)
