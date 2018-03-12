import SimpleCV
from SimpleCV import Camera
import time
cam=Camera()
while True:
    img=cam.getImage()
    cropped=img.crop(200,200,200,200)
    cropped.show()
    color=cropped.meanColor()
    print color
    time.sleep(1)
