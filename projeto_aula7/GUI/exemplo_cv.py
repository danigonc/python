#pip install opencv-python
#pip install scikit-image

import cv2
from skimage import io

def mostraImagemWeb():
    imagem = io.imread('https://softgraf.com/img/img1.jpg')
    cv2.imshow('Imagem da web',imagem)

mostraImagemWeb()

