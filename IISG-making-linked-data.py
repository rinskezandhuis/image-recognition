
import pandas as pd 
import numpy as np
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD #most common namespaces
import urllib.parse #for parsing strings to URI's

#import a dataframe of the data from a csv-file
file_data ="C:/Users/20223396/Documents/IISG/data_Meerendonk_totaal.csv"
df_data_unchanged=pd.read_csv(file_data)
df_data_raw = df_data_unchanged[['image','object','probability','coordinates']]
print(df_data_raw)

#import a dataframe of the objects id-numbers and their Q-number from wikidata.org
file_subject_Qnumber = "C:/Users/20223396/Documents/IISG/ow_Qnr.csv"
df_subject_Qnumber=pd.read_csv(file_subject_Qnumber)
#make a dictionary from the dataframe
df_Qnumber = df_subject_Qnumber.drop(columns=['object1'])
dict_Qnumber = df_Qnumber.set_index('id-number').to_dict()
dict_Qnummer = dict_Qnumber['Q-number']
print(dict_Qnummer)

#change the objects id-numbers into their Q-number
df_data = df_data_raw.replace(dict_Qnummer)
print(df_data)

#creat an empty graph and some Namespaces
g = Graph()

#for objects/subjects
Imagenumber = Namespace("https://hdl.handle.net/10622/")
Qnumber = Namespace("https://wikidata.org/entity/")
recognition = Namespace("https://iisg.amsterdam/id/recognition/rinskezandhuis/")

#for predicates
result = Namespace("https://schema.org/result")
resulting = URIRef(result)

hascords = Namespace("https://www.w3.org/ns/dcat#bbox")
has_cords = URIRef(hascords)

probability = Namespace("http://sparql.cwrc.ca/ontologies/cwrc#hasCertainty")
certainty = URIRef(probability)

#creat the triples
for index, row in df_data.iterrows():
    image = URIRef(Imagenumber + row['image'])
    determination = URIRef(recognition + str(index))
    object = URIRef(Qnumber + row['object'])
    coordinates = Literal(row['coordinates'], datatype=XSD.string)
    probs = Literal(row['probability'], datatype=XSD.decimal)
    g.add((image, FOAF.depicts, determination))
    g.add((image, RDF.type, FOAF.Image))
    g.add((determination, resulting, object))
    g.add((determination, has_cords , coordinates))
    g.add((determination, certainty , probs))

#create a ttl-file with the linked data
g.serialize('Meerendonk_linked_data_totaal.ttl', format='turtle')

