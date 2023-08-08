31/07/2023 – 11/08/2023
Internationaal Instituut voor Sociale Geschiedenis (IISG), Amsterdam

Nederlands:
Het IISG is een onderzoeks instittuut, maar is daarnaast ook beheerder van vele archiefstukken, waaronder duizenden afbeelding. Vele van deze afbeeldingen zijn gedigitaliseerd maar kunnen nog niet gevonden worden in een zoekfunctie omdat ze nog weinig tot geen metadata bevatten.
In twee weken heb ik geprobeerd om met imagerecognition vast te stellen wat er op foto’s staat. YOLO werd toegepast op de foto's (zo’n 2300) gemaakt door Ben van Meerendonk. YOLO kan onderwerpen herkennen uit een lijst van 80 onderwerpen waarop hij is getraint. Dit omvat bijvoorbeeld personen, auto's en stoelen. Bij iedere detectie van een onderwerp hoort een kans dat dit item daadwerkelijk op de afbeelding staat en zijn coordinaten. Het resultaat is een dataframe met vier kolommen: de afbeelding, het gedetecteerde item, de kans en de coordinaten.
De code die ik hiervoor heb beschreven kun je vinden onder de naam IISG-imagerecognition.py

Omdat het script niet kan runnen voor grote aantallen foto's, lees meer dan 1800, is ook een script geschreven dat csv-bestanden aan elkaar plakt tot één groot bestand.
Deze code kun je vinden on de naam IISG-adding-files.py

Om het project af te ronden werd van de data in een csv-bestand linked data gemaakt. Hiervoor werden relaties gemaakt tussen ...
Deze code heeft de naam IISG-linked-data.py

De resultaten/data van de foto's is terug te vinden op de website van het IISG

English:
The IISG is a research institute but is also the holder of many archive documents, including thousands of images. Many of these images have been digitized but cannot yet be found in a search function because they still contain little to no metadata.
In two weeks I tried to use image recognition to determine what is in photos. YOLO was applied to the photos (about 2300) made by Ben van Meerendonk. YOLO can recognize subjects from a list of 80 items he has been trained for. This includes, for example, persons, cars and chairs. Every recognition of a subject has a chance that this is actually on the image and has coordinates. The result is a data frame with four columns: the image(number), the detected item, the probability of occurrence, and the coordinates.
The code I described above can be found under the name IISH-imagerecognition.py

Because the script cannot run for large numbers of photos, around more than 1800, a script has also been written that adds CSV files into one large file.
This code can be found under the name IISG-adding-files.py

To complete the project, linked data was created from the data in a CSV file. For this, relationships were made between ...
This code is named IISG-linked-data.py
