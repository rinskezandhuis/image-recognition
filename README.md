31/07/2023 – 11/08/2023

Internationaal Instituut voor Sociale Geschiedenis (IISG), Amsterdam
International Institute for Social History (IISH), Amsterdam

Nederlands:

Het IISG is een onderzoeks instittuut, maar is daarnaast ook beheerder van vele archiefstukken, waaronder duizenden afbeelding. Vele van deze afbeeldingen zijn gedigitaliseerd maar kunnen nog niet gevonden worden in een zoekfunctie omdat ze nog weinig tot geen metadata bevatten.
In twee weken heb ik geprobeerd om met imagerecognition vast te stellen wat er op foto’s staat. YOLO werd toegepast op de foto's (zo’n 2300) gemaakt door Ben van Meerendonk. YOLO kan onderwerpen herkennen uit een lijst van 80 onderwerpen waarop hij is getraint. Dit omvat bijvoorbeeld personen, auto's en stoelen. Bij iedere detectie van een onderwerp hoort een kans dat dit item daadwerkelijk op de afbeelding staat en zijn coordinaten. Het resultaat is een dataframe met vier kolommen: de afbeelding, het gedetecteerde item, de kans en de coordinaten.

De code die ik hiervoor heb beschreven kun je vinden onder de naam IISG-imagerecognition.py

Omdat het script niet kan runnen voor grote aantallen foto's, lees meer dan 1800, is ook een script geschreven dat csv-bestanden aan elkaar plakt tot één groot bestand.

Deze code kun je vinden on de naam IISG-adding-files.py

Van de data in een csv-bestand is linked data gemaakt. Hiervoor werden relaties gemaakt tussen:
- een afbeeling, beeld af, een id voor het gedetecteerde
- de link van de afbeelding binnen het IISG, heeft relatie met, het gedetecteerde 
- het gedetecteerde, heeft als resultaat, een bepaald object (bijvoorbeeld een auto en auto heeft als Qnummer x)
- het gedetecteerde, heeft de coordinaten, coordinaten (string van getallen)
- het gedetecteerde, heeft als kans, de kans (een decimaal getal)

Deze code heeft de naam IISG-linked-data.py

Tegen het eind van het project in een programma geschreven waarmee een mens kan controlen of dat wat YOLO heeft herkent juist is. Hiervoor wordt het herkende uit de afbeelding geknipt en getoont, een gebruiker geeft aan of dat de herkenning juist is, waarna in een kolom van het datafram met TRUE of FALSE wordt aangeduid of de herkenning juist is. Het programma gaat vervolgens door naar de volgende herkenning. Voor een goede werking word eerst een nieuw dataframe gemaakt door middel van: IISG_create_dataframe_check.py

De code voor dit programma heet IISG-check-recognition.py


English:

The IISH is a research institute but also holds many archive documents, including thousands of images. Many of these images have been digitized but cannot yet be found in a search function because they still contain little to no metadata.
In two weeks I tried to use image recognition to determine what is in photos. YOLO was applied to the photos (about 2300) made by Ben van Meerendonk. YOLO can recognize subjects from a list of 80 items he has been trained for. This includes, for example, persons, cars and chairs. Every recognition of a subject has a chance that this is actually on the image and has coordinates. The result is a data frame with four columns: the image(number), the detected item, the probability of occurrence, and the coordinates.

The code I described above can be found under the name IISG-imagerecognition.py

Because the script cannot run for large numbers of photos, around more than 1800, a script that adds CSV files into one large file has also been written.

This code can be found under the name IISG-adding-files.py

Linked data was created from the data in a CSV file. For this, relationships were made between:
- an image, depicts, an id voor the detected
- the link of the image within resources of the IISH, relates with, the detected
- the detected, has as result, a certain object (for example a car and a car has Qnumber x)
- the detected, has the coordinates, coordinates (a string of numbers)
- the detected, has the probability, the probability (a decimal number)

This code is named IISG-linked-data.py

Towards the end of the project, a program was written with which a human can check if the recognition by YOLO is correct. The recognized item is cut from the image and displayed, a user indicates whether the recognition is correct, and in a column of the dataframe is stated with TRUE or FALSE whether the recognition is correct. The program then proceeds to the next recognition. For proper operation, a new data frame is first created by means of: IISG_create_dataframe_check.py

The code for this program is called IISG-check-recognition.py
