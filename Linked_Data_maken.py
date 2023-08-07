
import pandas as pd 
import numpy as np
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD #most common namespaces
import urllib.parse #for parsing strings to URI's

#file_data ="C:/Users/20223396/Documents/IISG/data_Meerendonk10.csv"
#df_data=pd.read_csv(file_data)
#print(df_data)

#file_ow_Qnr = "C:/Users/20223396/Documents/IISG/ow_Qnr.csv"
#df_ow_Qnr=pd.read_csv(file_ow_Qnr)
#print(df_ow_Qnr)

# QUERY schrijven die van het oorspronkelijke dataframe een dataframe maakt met de https adressen, dus colom (1 en) 3 koppelt

file_data ="C:/Users/20223396/Documents/IISG/data_Meerendonk10 _Qnummers.csv"
df_data=pd.read_csv(file_data)
print(df_data)

#otonummer = df_data['image']
#Qnummer = df_data['object']

g = Graph()
Imagenr = Namespace("http://hdl.handle.net/10622/")
Qnummer = Namespace("http://wikidata.org/entity/")
schema = Namespace("http://schema.org/")

#g.add((subject, contains, object))

for index, row in df_data.iterrows:
    subject = URIRef(Imagenr+ row['image'] + "?locatt=view:master")
    contains = URIRef(schema+'contains')
    object = URIRef(Qnummer + row['object'])
    g.add((subject, contains, object))

#for index, row in df_data.iterrows:
    #g.add(URIRef(Imagenr+ row['image']), URIRef(schema+'contains'), URIRef(Qnummer + row['object']))

g.serialize('Meerendonk_linked_data.ttl', format='turtle')
#print(g.serialize(format = 'turtle').decode('UTF-8'))