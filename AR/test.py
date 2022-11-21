import cv2
import numpy as np

#関数化、何を受け取って出力するか
#カメラの設定　デバイスIDは0
def circle_detection():
    cap = cv2.VideoCapture(0)

    #繰り返しのためのwhile文
    while True:
        #カメラからの画像取得
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 認識の精度を上げるために画像を平滑化
        gray = cv2.GaussianBlur(gray, (33,33), 1)
                # 表示用イメージ
        colimg = frame.copy() #cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        # 円検出
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 60, param1=10, param2=85, minRadius=10, maxRadius=80)
        if np.any(circles):
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                # 囲み線を描く
                cv2.circle(colimg,(i[0],i[1]),i[2],(255,255,0),2)
                # 中心点を描く
                cv2.circle(colimg,(i[0],i[1]),2,(0,0,255),3)

        #カメラの画像の出力
        cv2.imshow('camera' , colimg)


        #繰り返し分から抜けるためのif文
        key =cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break
circle_detection()