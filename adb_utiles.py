import adbutils
import cv2
import numpy as np
import time

class AdbUtiles():
    def __init__(self):
        self.adb = adbutils.adb.device()

    def screenshot(self):
        pilimg = self.adb.screenshot()
        pilimg = np.array(pilimg)

        pilimg = cv2.cvtColor(pilimg, cv2.cv2.COLOR_BGR2GRAY)

        return pilimg

    def click(self, coordinate):
        self.adb.click(coordinate[0], coordinate[1])
        time.sleep(1)

    def swip(self):
        self.adb.swipe(1000, 800, 1000, 200, 0.5)
        time.sleep(1)
              




# adbs = adbutils.AdbClient(host="127.0.0.1", port=5555)





# result = adb.shell(['screencap', '-p'], stream=True, timeout=10)

# raa = recv_all(result)

# ccc = adbutils.adb.device_list()

# adb = adbutils.adb.device()



# pilimg = adb.screenshot()

# pilimg = np.array(pilimg)

# cv2.imshow('gray', pilimg)

# cv2.waitKey(0)
# pilimg.show()

# gray = cv2.cvtColor(pilimg, cv2.COLOR_BGR2GRAY)

# cv2.imshow('gray', gray)
# cv2.waitKey(0)

# ccc = adb.swipe(600, 200, 300, 200, 0.5)

# print("haha")


    
