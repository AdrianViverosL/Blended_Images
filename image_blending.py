#Photo album slide transition program with OpenCV 
#Blending Image
#Adrian Viveros Lúques
#Python 3.6
import cv2
import numpy as np 
import os, time 
import glob
#reading all the .jpg files in folder called 'images' 
files = glob.glob('images/*.jpg')
#flag for KeyboardInterrupt 
flag = 0
#Open one by one file founded and store it in a empty list called imgs. 
imgs=[]
for f in files:
    img = cv2.imread(f) 
    imgs.append(img)
#del imgs[0]
total = len(imgs)
print(total) #all files foundend #print(imgs)
#resize the images into 480x640 scale and stores them into a new list. 
imgs_rs=[]
for i in imgs:
    i = cv2.resize(i, (480, 640)) 
    imgs_rs.append(i)
ttl= len(imgs_rs)
#print(ttl) 
#verify all the file were resized successfully 
#print(imgs_rs)
#Slide loop 
while (flag == 0):
    for index, val in enumerate(imgs): 
        for i in range(10):
            prev_idx = index + 1
            a = i/10
            b = 1-a
            if (prev_idx) == (len(imgs_rs)):
                prev_idx = 0
            cv2.imshow('blending images', cv2.addWeighted(imgs_rs[prev_idx], a, imgs_rs[index], b, 0.0))
            time.sleep(0.2) #delay for the transition 
            if cv2.waitKey(1) & 0xff == ord('q'):
                flag = 1
                break
            if cv2.waitKey(1) & 0xff == ord('q'):
                cv2.destroyAllWindows() 
                flag = 1
                break
    cv2.destroyAllWindows()
