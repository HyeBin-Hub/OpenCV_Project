import cv2

imgfile="C:/Users/hyebin/Desktop/OpenCV/imags/black_img.png"
img=cv2.imread(imgfile)
#img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_copy=img.copy()
print(img_copy.shape)

(c_x,c_y)=(int(img_copy.shape[1]/2),int(img_copy.shape[0]/2))
print(c_x,c_y)

for r in range(0,250,25):
    cv2.circle(img_copy,(c_x,c_y),r,(255,255,255))

cv2.imshow("circle_1",img_copy)

img_copy_2=img.copy()

cv2.circle(img_copy_2,(145,450),25,(255,0,0),-1)
cv2.circle(img_copy_2,(250,250),10,(0,255,255),0)
cv2.circle(img_copy_2,(350,250),60,(102,102,255),-1)
cv2.circle(img_copy_2,(100,100),50,(255,0,255),-1)
cv2.circle(img_copy_2,(450,450),102,(255,51,51),0)

cv2.imshow("circle_2",img_copy_2)

img_copy_3=img.copy()

img=cv2.ellipse(img_copy_3,((200,200),(200,200),0),(255,0,255),2)
img=cv2.ellipse(img_copy_3,((200,200),(50,150),0),(255,153,0),2)
img=cv2.ellipse(img_copy_3,((200,200),(100,400),0),(153,255,204),2)

cv2.imshow("circle_3",img)

img_copy_4=img.copy()

img=cv2.ellipse(img_copy_4,((200,200),(200,200),45),(255,0,255),2)
img=cv2.ellipse(img_copy_4,((200,200),(50,150),45),(255,153,0),2)
img=cv2.ellipse(img_copy_4,((200,200),(100,400),45),(153,255,204),2)

cv2.imshow("circle_4",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

color=[(0,255,255),(255,0,0),(255,0,255),(0,255,0)]

# cv2.imwrite("C:/Users/hyebin/PycharmProjects/OpenCV_Project/OpenCV_Basic/results/circle.jpg",
#             img_copy_2)

cv2.imwrite("C:/Users/hyebin/PycharmProjects/OpenCV_Project/OpenCV_Basic/results/circle_1.jpg",img_copy_3)
cv2.imwrite("C:/Users/hyebin/PycharmProjects/OpenCV_Project/OpenCV_Basic/results/circle_2.jpg",img_copy_4)
