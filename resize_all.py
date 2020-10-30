"""
File: resize_all.py
Author: Nrupatunga
Email: nrupatunga.s@byjus.com
Github: https://github.com/nrupatunga
Description: resize images
"""
import cv2
import imutils
from imutils import paths
from pathlib import Path


fr_dir = './images/fulls'
lr_dir = './images/thumbs'

for img_path in paths.list_images(fr_dir):
    img_path.replace('JPG', 'jpg')
    out_path = Path(lr_dir).joinpath(img_path.split('/')[-1])
    img = cv2.imread(img_path)
    img = imutils.resize(img, width=512)
    cv2.imwrite(str(out_path), img)
    cv2.imwrite(img_path, img)
