import pandas as pd
import glob
import os 

#create an empty dataframe
dataframe = pd.DataFrame({'image':[],'object':[],'probability':[],'coordinates':[]})

#add all files within the folder into a list
path = "C:/Users/20223396/Documents/IISG/data"
all_files = glob.glob(os.path.join(path, "*.csv"))

#add all data from the different files into the dataframe
for file in all_files:
    file_name = os.path.splitext(os.path.basename(file))[0]
    print(file_name)
    df = pd.read_csv(path + '/' + file_name + '.csv')
    dataframe = dataframe.append(df)

#create a new file with all data
dataframe.to_csv('data_Meerendonk_totaal.csv') 