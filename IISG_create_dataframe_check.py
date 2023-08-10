
import pandas as pd
import numpy as np

file_data ="C:/Users/20223396/Documents/IISG/data_Meerendonk_totaal.csv"
df_data_unchanged=pd.read_csv(file_data)
df_data_raw = df_data_unchanged[['image','object','probability','coordinates']]
print(df_data_raw)

#import a dataframe of the objects id-numbers and their Q-number from wikidata.org
file_name_obj = "C:/Users/20223396/Documents/IISG/ow_Qnr.csv"
df_name_obj=pd.read_csv(file_name_obj)
#make a dictionary from the dataframe
df_nameobj = df_name_obj.drop(columns=['Q-number'])
dict_nameobj = df_nameobj.set_index('id-number').to_dict()
dict_object = dict_nameobj['object1']
print(dict_object)

#change the objects id-numbers into their Q-number
df_data = df_data_raw.replace(dict_object)
print(df_data)

df_data['check'] = np.nan
print(df_data)

name = 'data_Meerendonk_check.csv' 
df_data.to_csv(name)
