import cv2
import numpy as np
from matplotlib import pyplot as plt
def valo(x):
    vintage(image,x)


def vintage(img,s):
    s=s*0.1
    global frame
    frame = img.copy()
    center = (img.shape[0] / 2.0, img.shape[1] / 2.0)
    max_distance = ((center[0] - img.shape[0]) ** 2 + (center[1] - img.shape[1]) ** 2)**s
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            dist = ((center[0] - i) ** 2 + (center[1] - j) ** 2)**s
            # new=result-dist/max_distance*result
            frame[i][j][0] = frame[i][j][0] - (dist / max_distance) * frame[i][j][0]
            frame[i][j][1] = frame[i][j][1] - (dist / max_distance) * frame[i][j][1]
            frame[i][j][2] = frame[i][j][2] - (dist / max_distance) * frame[i][j][2]



cap = cv2.VideoCapture(0)

ret, image = cap.read()
frame=image.copy()
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,10,valo)
while (True):

    cv2.getTrackbarPos('R', 'image')
    cv2.imshow("image",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

