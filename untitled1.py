# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12moBFwkclJHvUyp5LMYszqC6rXwU8r8K
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread('image.png')
cv2_imshow(rasm)

oqqora= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread('image1.jpg')
cv2_imshow(rasm)

oqqora= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread('image2.jpg')
cv2_imshow(rasm)

oqqora= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread('image4.jpg')
cv2_imshow(rasm)

oqqora= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread('image6.jpg')
cv2_imshow(rasm)