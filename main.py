import cv2

image = cv2.imread('assets/valo.jpg')
convert_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_Valo_Img", convert_img)
cv2.waitKey(0)
