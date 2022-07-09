import cv2

imgfile="C:/Users/hyebin/Desktop/OpenCV/imags/black_img.png"
img=cv2.imread(imgfile)
# img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_copy=img.copy()
print(img_copy.shape)

cv2.line(img_copy,(50,100),(400,100),(0,255,0))
cv2.line(img_copy,(474,0),(0,474),(255,51,51),3)

cv2.imshow("diagonal,straight line",img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

# cv2.imwrite("C:/Users/hyebin/PycharmProjects/OpenCV_Project/OpenCV_Basic/results/line.jpg",img_copy)

