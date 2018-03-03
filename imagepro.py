import cv2 as cv
img=cv.imread("/home/superadmin/Downloads/galaxy.py",0)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)
cv.imgshow("galaxy",img)
cv.waitkey(2000)
