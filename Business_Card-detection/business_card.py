import wget
import cv2
import numpy as np
from PIL import Image
import pytesseract

url="http://web.cs.wpi.edu/~claypool/mmsys-dataset/2011/stanford/mvs_images/business_cards/Droid/019.jpg"
filepath="C:/Users/hyebin/PycharmProjects/OpenCV_Project/Business_Card-detection/images"
# wget.download(url,filepath)

imgfile="C:/Users/hyebin/PycharmProjects/OpenCV_Project/Business_Card-detection/images/019.jpg"
img=cv2.imread(imgfile)

img_h,img_w=img.shape[:2]

r=1000.0/img_h
img_resize=cv2.resize(img,(int(r*img_w),1000))
img_gray=cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)

#cv2.imshow("img",img_resize)

blur=cv2.GaussianBlur(img_gray,(9,9),0)
edge=cv2.Canny(blur,100,10)

img_copy=img_resize.copy()

contours,hierarchy=cv2.findContours(edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cont in contours:
    approx=cv2.approxPolyDP(cont,cv2.arcLength(cont,True)*0.02,True)
    if len(approx)==4:
        color=[(0,255,255),(255,0,0),(255,0,255),(0,255,0)]
        for ind,c in enumerate(approx):
            c_x = int(c[0][0])
            c_y = int(c[0][1])
            cv2.circle(img_copy, (c_x, c_y), 15, color[ind], -1)

        left_1,  top_1 = approx[0][0][0], approx[0][0][1]
        left_2, bottom_1 = approx[1][0][0], approx[1][0][1]
        right_1, bottom_2 = approx[2][0][0], approx[2][0][1]
        right_2,  top_2 = approx[3][0][0], approx[3][0][1]
        cv2.line(img_copy, (int(left_1),int(top_1)),(int(right_2),int(top_2)),(255,153,204),3)
        cv2.line(img_copy, (int(right_2), int(top_2)), (int(right_1), int(bottom_2)), (102, 204, 255), 3)
        cv2.line(img_copy, (int(right_1), int(bottom_2)), (int(left_2), int(bottom_1)), (255, 255, 102), 3)
        cv2.line(img_copy, (int(left_2), int(bottom_1)), (int(left_1), int(top_1)), (0, 51, 255), 3)


left_top = [approx[0][0][0], approx[0][0][1]]
left_bottom=[approx[1][0][0], approx[1][0][1]]
right_bottom=[approx[2][0][0], approx[2][0][1]]
right_top=[approx[3][0][0], approx[3][0][1]]

pts1=np.float32([left_top,right_top,right_bottom,left_bottom])

w1=abs(right_bottom[0]-left_bottom[0])
w2=abs(left_top[0]-right_top[0])
h1=abs(left_top[1]-left_bottom[1])
h2=abs(right_top[1]-right_bottom[1])
minW=min([w1,w2])
minH=min([h1,h2])

pts2=np.float32([[0,0],[minW-1,0],[minW-1,minH-1],[0,minH-1]])

M=cv2.getPerspectiveTransform(pts1,pts2)

wrap=cv2.warpPerspective(img_copy,M,(int(minW),int(minH)))

cv2.imshow("wrap",wrap)

warped = cv2.cvtColor(wrap, cv2.COLOR_BGR2GRAY)
th3 = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)

with open("C:/Users/hyebin/PycharmProjects/OpenCV_Project/Business_Card-detection/result_txt/1.txt","w") as f:
    text = pytesseract.image_to_string(th3)
    f.write(text)

print(text.strip())


cv2.imshow("warped",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)







