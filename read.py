import cv2
from pyzbar.pyzbar import decode
from PIL import Image


def read_qr_code(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path)

    # QRコードをデコード
    decoded_objects = decode(image)

    # 結果を表示
    qr_codes = []
    for obj in decoded_objects:
        qr_codes.append(obj.data.decode('utf-8'))  # QRコードのデータを文字列にデコード
        print(f"QRコードの内容: {obj.data.decode('utf-8')}")
    
    return qr_codes

# 画像ファイルを指定
image_path = "./data/google.com.png"
qr_data = read_qr_code(image_path)
if not qr_data:
    print("QRコードが見つかりませんでした。")