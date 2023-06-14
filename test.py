import numpy as np
import imutils
import cv2
import adb_utiles as adbu

# adb = adbu.AdbUtiles()

# back = adb.screenshot()

# one = cv2.cvtColor(cv2.imread("C://Users//Administrator//Desktop//pyimg//one.png"), cv2.COLOR_BGR2GRAY)
# two = cv2.cvtColor(cv2.imread("C://Users//Administrator//Desktop//pyimg//two.png"), cv2.COLOR_BGR2GRAY)

# oth, otw = one.shape[:2]
# tth, ttw = two.shape[:2]

# result_one = cv2.matchTemplate(back, one, cv2.TM_CCOEFF_NORMED)
# result_two = cv2.matchTemplate(back, two, cv2.TM_CCOEFF_NORMED)

# _, one_maxval,_ ,one_maxLoc = cv2.minMaxLoc(result_one)
# _, two_maxval,_ ,two_maxLoc = cv2.minMaxLoc(result_two)

# clone = np.dstack([back, back, back])
# cv2.rectangle(clone, (one_maxLoc[0], one_maxLoc[1]), (one_maxLoc[0] + otw, one_maxLoc[1] + oth), (0, 0, 255), 2)
# cv2.rectangle(clone, (two_maxLoc[0], two_maxLoc[1]), (two_maxLoc[0] + ttw, two_maxLoc[1] + tth), (0, 0, 255), 2)
# cv2.imshow("Visualize", clone)
# cv2.waitKey(0)

def testCV2():
    urlList = ["./images/mystery.png"]
    adb = adbu.AdbUtiles()
    back = adb.screenshot()
    
    clone = np.dstack([back, back, back])
    for url in urlList:
        image = cv2.cvtColor(cv2.imread(url), cv2.COLOR_BGR2GRAY)
        oth, otw = image.shape[:2]
        result = cv2.matchTemplate(back, image, cv2.TM_CCOEFF_NORMED)
        _, one_maxval,_ ,one_maxLoc = cv2.minMaxLoc(result)
        print(str(one_maxval))

        cv2.rectangle(clone, (one_maxLoc[0], one_maxLoc[1]), (one_maxLoc[0] + otw, one_maxLoc[1] + oth), (0, 0, 255), 2)
    
    cv2.imshow("Visualize", clone)
    cv2.waitKey(0)
    
def testADB():
    adb = adbu.AdbUtiles()
    

if __name__ == "__main__":
    while 1:
        count = int(input("1.测试ADB \n2.测试模板匹配\n3.退出\n"))
        if count == 1:
            testADB()
            
        elif count == 2:
            testCV2()
            
        elif count == 3:
            break
        else:
            print("fail")    
    

# cc = nm.linspace(0.2, 1.0 , 20)[::-1]

# print(cc)

# image = cv2.imread("C://Users//Administrator//Desktop//pyimg//aa.png")

# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# th, tw = image.shape[:2]


# print("haha")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# canny_gray = cv2.Canny(gray, 50, 150)


# gau = cv2.GaussianBlur(gray, (3,3), 0)
# canny_gau = cv2.Canny(gau, 50, 150)

# cv2.imshow('gray', canny_gray)
# cv2.imshow('gau', canny_gau)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(gray.shape)

# cv2.imshow('image', image)
# cv2.waitKey(0)

# canny = cv2.Canny(image, 50, 150)
# cv2.imshow('canny', canny)



# dsa = nm.dstack([canny, canny, canny])
# cv2.imshow('dsa', dsa)
# cv2.waitKey(0)

# print("haha")

# ass = [
#     [
#         [ 0,  1,  2,  3,  4],
#         [ 5,  6,  7,  8,  9]
#     ],
#     [
#         [10, 11, 12, 13, 14],
#         [15, 16, 17, 18, 19]
#     ],
#     [
#         [20, 21, 22, 23, 24],
#         [25, 26, 27, 28, 29]
#     ]
# ]

