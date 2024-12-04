import cv2
from pyzbar.pyzbar import decode

image = cv2.imread("data/0.png")

decoded_objects = decode(image)

for obj in decoded_objects:
    print("デコードされたデータ:", obj.data.decode("utf-8"))
    print("QRコードの種類:", obj.type)

cv2.imshow("QRコード画像", image)
cv2.waitKey(0)
cv2.destroyAllWindows()