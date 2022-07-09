import cv2

imgfile="C:/Users/hyebin/Desktop/OpenCV/imags/black_img.png"
img=cv2.imread(imgfile)
#img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_copy=img.copy()
print(img_copy.shape)

cv2.rectangle(img_copy,(150,100),(200,150),(0,255,0),3)
cv2.rectangle(img_copy,(150*2,100),(200*2,150),(255,12,21),3)
cv2.rectangle(img_copy,(100,200),(150,450),(102,102,255),3)

cv2.imshow("d",img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

cv2.imwrite("C:/Users/hyebin/PycharmProjects/OpenCV_Project/OpenCV_Basic/results/rectangle.jpg",
            img_copy)