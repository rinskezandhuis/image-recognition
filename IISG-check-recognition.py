
import pandas as pd
import os.path
from PIL import Image
#import numpy as np
#import glob
import psutil

# before using this program you should create the right data using: IISG_creat_dataframe_check

#import a dataframe of the data from a csv-file
file_path ="C:/Users/20223396/Documents/IISG/data_Meerendonk_check.csv"
df_data_unchanged=pd.read_csv(file_path)
df_data_total = df_data_unchanged[['image','object','probability','coordinates','check']]
print(df_data_total)

mask = df_data_total['check'].isnull()
#print(mask)
df_data = df_data_total[mask]
#print(df_data)

print('')
print('You are going to check if our image recognition correctly recognized the object')
print('Answer with y for yes and n for no.')

for index, row in df_data.iterrows():
    
    image = row['image']
    path_file = "D:/Meerendonk/" + image + "/" + image + "_0001.tif"
    if os.path.isfile(path_file):
        path_file = path_file
    else:
        path_file = "D:/Meerendonk/" + image + "/" + image + "_0001.jpg"
    
    im = Image.open(path_file)
    #print('image number: ' + im.filename)
    cords = (row['coordinates'][1:-1])
    cords_list = list(cords.split(', '))
    cords_list = [int(x) for x in cords_list]
    #print("coordinates of this object: " + str(cords_list))
    image_crop = im.crop((cords_list[0], cords_list[1], cords_list[2], cords_list[3]))
    image_crop.show()
    print('')

    pd.set_option('mode.chained_assignment', None)
    
    while pd.isnull(df_data_total.at[index, 'check']) :
        check = input('Is this a(n) ' + str(row['object'] + "? "))
        if check == 'y':
            df_data_total.loc[index, 'check'] = True
        elif check == 'n':
            df_data_total.loc[index, 'check'] = False
        else:
            print('you should answer with y or n.')
    
    print('--------')
    print(df_data_total.loc[[index]])
    print('--------')

    # Killing the window showing the image. This proc.name is used for windows, You have to change this name fot other opperating systems. For Mac I think you have to use "Preview".
    # https://stackoverflow.com/questions/6725099/how-can-i-close-an-image-shown-to-the-user-with-the-python-imaging-library
    for proc in psutil.process_iter():
        if proc.name() == "Microsoft.Photos.exe":
            proc.kill()

    continuu = input("press enter if you want to continue, type save if you want to stop and save the progress ")
    if continuu == '':
        continue
    elif continuu == 'save':
        break

df_data_total.to_csv(file_path)
print('the progress is saved')





