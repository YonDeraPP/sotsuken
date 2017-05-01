import io
import picamera
import cv2

import numpy as np

# 正面の顔の情報データ
cascade_path = "/ usr / share / opencv / haarcascades / haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)

stream = io.BytesIO()

# カメラの解像度を設定
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

#
color = (255, 255, 255)
camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)

# カメラで何回写真を取るかのループ
for i in xrange(5):
    # 写真を撮る！
    camera.capture(stream, format='jpeg')
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data, 1)

    # エラーになるのでコメントアウト(ウィンドウに表示)
    #        cv2.imshow('image',image)
    #        cv2.waitKey(16)

    # 解析しやすくするために灰色にする
    image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
    # ライブラリに顔検出してもらう
    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

    image_output = image
    # 顔が１つ以上あったら
    if len(facerect) > 0:
        # 顔検出した部分を、四角で囲む
        for rect in facerect:
            cv2.rectangle(image_output, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)
        #
        print "found"
    # エラーになるのでコメントアウト(ウィンドウに表示)
    #        cv2.imshow('image_out',image_output)
    #        cv2.waitKey(16)

    # jpgファイルに保存
    cv2.imwrite(str(i) + '.jpg', image)

    # 写真領域をクリア(コレをしないと、ずっと同じ写真になる)
    stream.seek(0)

    print "captured % d "% (i)