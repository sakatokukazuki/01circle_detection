import cv2
import numpy as np
import copy

#関数化、何を受け取って出力するか
#カメラの設定　デバイスIDは0
def image_circle_detection(image):
    #グレースケール
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 認識の精度を上げるために画像を平滑化
    gray = cv2.GaussianBlur(gray, (33,33), 1)
    # 表示用イメージ
    colimg = image.copy() #cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # 円検出
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 60, param1=10, param2=85, minRadius=10, maxRadius=80)
    return circles

def bake_circle(image, circle_list):
    baked_image = copy.deepcopy(image)
    if np.any(circle_list):
        circle_list = np.uint16(np.around(circle_list))
        for i in circle_list[0,:]:
            # 囲み線を描く
            cv2.circle(baked_image, (i[0], i[1]), i[2], (255, 255, 0), 2)
            # 中心点を描く
            cv2.circle(baked_image,(i[0],i[1]),2,(0,0,255),3)
    
    return baked_image

input_image = cv2.imread(f"images/japan.png")
circle_list = image_circle_detection(input_image)
baked_image = bake_circle(input_image, circle_list)
cv2.imshow("input", input_image)
#繰り返し分から抜けるためのif文
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
    
cv2.imshow("output", baked_image)
#繰り返し分から抜けるためのif文
key =cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
