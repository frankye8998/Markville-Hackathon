import cv2
from os import rename
import numpy as np
import time
import svgwrite

THRESHOLD = 220
SLEEPYTIME = 2

video = cv2.VideoCapture(0)

#app = QApplication([])
#svg = QSvgWidget()

def convertGray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dwg = svgwrite.Drawing('tmp.svg', profile='full')

#app.exec_()

while True:
    #img_colour = cv2.imread('./dave.jpg',0)
    print("BEGIN")
    img_colour = video.read()[1]
    print(1)
    img = cv2.cvtColor(img_colour, cv2.COLOR_BGR2GRAY)
    print(2)
    #img = cv2.VideoCapture(0).read()[1]
    ret, thresh1 = cv2.threshold(img, THRESHOLD, 255, cv2.THRESH_BINARY)
    print(3)
    image, contours, hierarchy = cv2.findContours(
        thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(4)
    #images = [img_colour, thresh1, thresh2, thresh3, thresh4, thresh5, image]
    #images = list(map(convertGray, images))
    # for i in range(len(images)):
    #    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    #    plt.title(titles[i])
    #    plt.xticks([]),plt.yticks([])
    print(5)
    for contour in contours:
        numpoints = 0
        for point in contour:
            dwg.add(dwg.circle(center=(float(point[0][0]), float(point[0][1])), r=2, fill="white"))
            numpoints += 1
        print(numpoints, end=" ")

    print(6)
    print(7)
    # plt.pause(SLEEPYTIME)
    dwg.save()
    rename("tmp.svg", "test.svg")
    print("SAVED!")
    try:
        time.sleep(SLEEPYTIME)
    except KeyboardInterrupt:
        break
