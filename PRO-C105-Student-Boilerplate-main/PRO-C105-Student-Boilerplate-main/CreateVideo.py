import os
from re import I
from turtle import width
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height,width,channel = frame.shape
size = (width,height)
#sreedevi ma'am high - five * 5
print(size)

out = cv2.VideoWriter('project2.mp4',cv2.VideoWriter_fourcc(*'DIVX'),60,size)
for i in range(0,count-1) :
    frame = cv2.imread(images[i])
    out.write(frame)
    
out.release()
print('done')

