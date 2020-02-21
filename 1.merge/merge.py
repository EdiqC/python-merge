# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

#建立顯示圖片的函數

def show(image):
 plt.imshow(image)
 plt.axis('off')
 plt.show()

 

#導入前景圖
img=cv2.imread('img.png') #圖片導入

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #轉換顏色模型
print(img.shape) #列印圖片規格
show(img) #顯示圖片

#導入背景圖
back_img = cv2.imread('back_img.jpg') #圖片導入

back_img = cv2.cvtColor(back_img,cv2.COLOR_BGR2RGB) #轉換顏色模型
print(back_img.shape) #列印圖片規格
show(back_img) #顯示圖片

#裁剪圖片
img = img[0:1000,150:550] #裁剪圖片大小
show(img) #顯示圖片

#縮放圖片
print(img.shape) #列印圖片規格
img=cv2.resize(img,None,fx=0.9,fy=0.9) #圖片縮小10%
print(img.shape) #列印圖片規格

#拆分圖片信息
rows,cols,channels = img.shape #拆分圖片信息

#轉換格式
img_hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV) #把圖片轉換成HSV格式，用於摳圖
show(img_hsv) #顯示圖片

#摳圖
lower_blue=np.array([0,0,0]) #獲取最小閾值
upper_blue=np.array([0,255,255]) #獲取最大閾值
mask = cv2.inRange(img_hsv, lower_blue, upper_blue) #創建遮罩
show(mask) #顯示遮罩
erode=cv2.erode(mask,None,iterations=3) #圖像腐蝕
show(erode) #顯示圖片
dilate=cv2.dilate(erode,None,iterations=1) #圖像膨脹
show(dilate) #顯示圖片
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8,8))) #開運算
show(opening) #顯示圖片

center = [0,0] #設置前景圖開始位置
print(back_img.shape)
print(center[0])
for i in range(rows):
    for j in range(cols):
        if opening[i,j]==0: #代表黑色
            back_img[center[0]+i,center[1]+j] =img[i,j] #賦值顏色
show(back_img) #顯示圖片

back_img = cv2.cvtColor(back_img,cv2.COLOR_RGB2BGR) #圖像格式轉換
back_img=cv2.resize(back_img,None,fx=0.8,fy=0.8) #圖像縮放20%
cv2.imwrite('result.png',back_img) #保存圖像