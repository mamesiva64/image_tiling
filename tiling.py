import numpy as np
import cv2
import glob
import os

def tiling(in_path, out_path):
    img = cv2.imread(in_path)
    height, width, c = img.shape
    base = np.zeros((height*3, width*3, 3))
    for y in range(3):
        for x in range(3):
            if x%2 == 0:
                if y%2 == 0:
                    tmp = img
                else:
                    tmp = cv2.flip(img, 0)
            else:
                if y%2 == 0:
                    tmp = cv2.flip(img, 1)
                else:
                    tmp = cv2.flip(img, -1)

            base[y*height:(y+1)*height,
                 x*width:(x+1)*width] = tmp

    base = cv2.rotate(base, cv2.ROTATE_180)
    #base = base[180:180+256, 480-200:480+200]
    cv2.imwrite(out_path, base)


files = glob.glob("./data/*")
for file in files:
    src = file
    dst = os.path.basename(file) + ".tile.png" 
    tiling(src, dst)
    
#xAxis = cv2.flip(img, 0)
#yAxis = cv2.flip(img, 1)
#xyAxis = cv2.flip(img, -1)
