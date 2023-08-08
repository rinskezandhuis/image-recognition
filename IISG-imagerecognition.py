
from ultralytics import YOLO
model = YOLO("yolov8m.pt")

import pandas as pd
import os, os.path
from PIL import Image
import glob

#create an empty list
image_list = []
path = "D:/Meerendonk"

#fill the list with all the images
for filename in glob.glob(path + "/**/*.tif"):
    im=Image.open(filename)
    image_list.append(im)
    #print(filename)
for filename in glob.glob(path + "/**/*.jpg"):
    im=Image.open(filename)
    image_list.append(im)
    #print(filename)

#check whether all images are added into the list
number_images = len(image_list)
print(number_images)

#from which image in the list do you want to start
#you have to change this number by hand after 1500 images.
x = 1500

#create a sublist containing a slice of the whole list
sub_list = image_list[x:x+500]

# after how many images do you want to break
# Our experience was that after around 1800-1900 images/ 60000 detections YOLO could not process anymore information and shut down.
# you have to change this number by hand if you are doing more than this amount of images. 
end = number_images

# create a whileloop, whom creates a dataframe and csv-file for every sublist
while x < end:
    #create an empty dataframe
    dataframe = pd.DataFrame({'image':[],'object':[],'probability':[],'coordinates':[]})
    
    #create an forloop for every image in the sublist
    for im in sub_list:

        #do the magic imagerecognition    
        results = model.predict(im)
        result = results[0]
        number_obj = len(result.boxes)

        x = x + 1

        #make shure something is recognized
        if number_obj > 0:

            # make a forloop who adds the information of every recognized item in a row of the dataframe  
            for box in result.boxes:
                class_id = box.cls[0].item()
                cords = box.xyxy[0].tolist()
                cords = [round(x) for x in cords]
                conf = round(box.conf[0].item(), 2)
                dataframe = dataframe.append({ 'image': im.filename[14:28], 'object' : class_id, 'probability' : conf, 'coordinates': cords}, ignore_index=True)
        
        print(dataframe.tail(1))
        print(x)
    
    #create the csv-file of the created dataframe with all regocnized items
    name = 'data_Meerendonk' + str(x) + '.csv' 
    dataframe.to_csv(name)
    
    #change the sublist with the next 500 images 
    sub_list = image_list[x:x+500]

