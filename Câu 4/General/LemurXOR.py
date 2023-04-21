import cv2

flag = cv2.imread("flag.png")
lemur = cv2.imread("lemur.png")

key = cv2.bitwise_xor(flag, lemur)
cv2.imshow("xored data", key)
cv2.waitKey(0)
cv2.destroyAllWindows()