import numpy as np
import cv2 as cv
 
# img = cv.imread("./image/rona.jpg", cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# rows,cols = img.shape
 
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv.warpAffine(img,M,(cols,rows))
 
# cv.imshow('img',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

img = cv.imread("iso.PNG", cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols = img.shape
 
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))