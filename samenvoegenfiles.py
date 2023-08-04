import pandas as pd
import glob
import os 

dataframe = pd.DataFrame({'image':[],'object':[],'probability':[],'coordinates':[]})
dataframe

path = "C:/Users/20223396/Documents/IISG/data"
all_files = glob.glob(os.path.join(path, "*.csv"))

for file in all_files:
    file_name = os.path.splitext(os.path.basename(file))[0]
    print(file_name)
    df = pd.read_csv(path + '/' + file_name + '.csv')
    #print(df)
    dataframe = dataframe.append(df)
    #print(dataframe)

dataframe.to_csv('data_Meerendonk_totaal.csv') 