from PIL import Image as image
import cv2

img = cv2.imread('93.jpg')
dh, dw, _ = img.shape
text = open('93.txt',"r")
for line in text:
    zero , x, y, w, h = line.split(" ")
    l = (float(x) - float(w )/ 2 )* dw
    r = (float(x )+ float(w )/ 2 )* dw
    t = (float(y )- float(h )/ 2) * dh
    b = (float(y )+ float(h) / 2 )* dh
    
    if l < 0:
        l = 0
    if r > dw - 1:
        r = dw - 1
    if t < 0:
        t = 0
    if b > dh - 1:
        b = dh - 1
    
    x = (float(l)+float(r))/2
    y = (float(t)+float(b))/2 
    img = cv2.circle(img, (int(x),int(y)),0, (0, 0, 0),5)
    cv2.imshow('image',img)
    cv2.waitKey(0)


