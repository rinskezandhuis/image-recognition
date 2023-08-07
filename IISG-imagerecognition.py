
from ultralytics import YOLO
model = YOLO("yolov8m.pt")

import pandas as pd
import os, os.path
from PIL import Image
import glob

path = "D:/Meerendonk"


image_list = []

for filename in glob.glob(path + "/**/*.tif"):
    im=Image.open(filename)
    image_list.append(im)
    #print(filename)
for filename in glob.glob(path + "/**/*.jpg"):
    im=Image.open(filename)
    image_list.append(im)
    #print(filename)

num_images = len(image_list)
print(num_images)

x = 0

#x:x+500
sub_list = image_list[x:x+10]

# < num_images
while x < 10:
    dataframe = pd.DataFrame({'image':[],'object':[],'probability':[],'coordinates':[]})
    
    for im in sub_list:
            
        results = model.predict(im)
        result = results[0]
        number_obj = len(result.boxes)

        x = x + 1

        if number_obj > 0:
                
            for box in result.boxes:
                class_id = box.cls[0].item()
                cords = box.xyxy[0].tolist()
                cords = [round(x) for x in cords]
                conf = round(box.conf[0].item(), 2)
                dataframe = dataframe.append({ 'image': im.filename[14:28], 'object' : class_id, 'probability' : conf, 'coordinates': cords}, ignore_index=True)
        
        print(dataframe.tail(1))
        print(x)

    name = 'data_Meerendonk' + str(x) + '.csv' 
    dataframe.to_csv(name) 
    sub_list = image_list[x:x+500]


#probability_mask = dataframe['probability'] > 0.7
#dataframe_high_probabilities = dataframe[probability_mask]
