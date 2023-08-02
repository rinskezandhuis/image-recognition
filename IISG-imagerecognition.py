
from ultralytics import YOLO
model = YOLO("yolov8m.pt")

import pandas as pd
import os, os.path
from PIL import Image
import glob
from pathlib import Path

image_list = []
for filename in glob.glob("D:/50fotos/**/*.tif"):
    im=Image.open(filename)
    image_list.append(im)
for filename in glob.glob("D:/50fotos/**/*.jpg"):
    im=Image.open(filename)
    image_list.append(im)


num_images = len(image_list)
print(num_images)

dataframe = pd.DataFrame({'image':[],'object':[],'probability':[],'coordinates':[]})

for im in image_list:
    
    results = model.predict(im)
    result = results[0]
    number_obj = len(result.boxes)

    if number_obj > 0:
         
        for box in result.boxes:
          class_id = result.names[box.cls[0].item()]
          cords = box.xyxy[0].tolist()
          cords = [round(x) for x in cords]
          conf = round(box.conf[0].item(), 2)
          dataframe = dataframe.append({ 'image': im.filename, 'object' : class_id, 'probability' : conf, 'coordinates': cords}, ignore_index=True)


dataframe.to_csv('data.csv')