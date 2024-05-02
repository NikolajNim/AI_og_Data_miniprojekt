# AI_og_Data_miniprojekt
Dette er mit repo for miniprojektet i AI og Data på Design og Anvendelse af Kunstig Intelligens 2024

Kursusgang 1:
Opgave 1:
    Link til opgaveløsning: https://github.com/NikolajNim/AI_og_Data_miniprojekt/blob/main/Kursusgang_1/opgave_1.py

    Første opgave går ud på at følge en tutorial fra RealPython for at lære om wepscraping. Dette er linket til selve tutorialen: https://realpython.com/python-web-scraping-practical-introduction/

    Webscraping er et værktøj til at udtrække information fra en hjemmeside. Dette kan lade sig gøre ved at bruge library'et urllib. I opgaveløsningen kan det ses, at i linje 1 bliver urlopen modulet importet fra urllib.request. Linje 3 til 7 viser, at man kan tage et url også læse det ved hjælp af urlopen til at udtrække html-koden, som bliver printet som en streng.
    Ud fra dette er det så muligt at tilgå hvad der står på hjemmesiden. Dette er demonstreret fra linje 8 til 12.

    Den næste del af tutoriallen præsenterer Regular Expressions(re). For at arbejde med Regular Expressions i python, så skal modulet re importeres. Afsnittet forklarer, at re er mønstre, som man bruger i strenge til at søge efter information der står i dem. I opgave_1.py kan nogle af de forskellige metoder og specialkarakterer ses blive brugt fra linje 16 til 29.

    Den næste del handler om at overfører sin viden om re til at kunne udtrække information fra en hjemmeside. Jeg har valgt at løse den Exercise der er på siden, for at vise konceptet. Exercise: Scrape data from a website bliver løst på linje 31 til 51 i opgave_1.py.

    I den næste del af tutoriallen lærer man om HTML parsers, og dertil er der nogle libraries som kan bruges til dette. Librariet som bliver brugt her er BeautifulSoup, og for at demonstrere hvad jeg har lært, så løser jeg  Exercise: Parse HTML with BeautifulSoup fra linje 62 til 74.

    Næste del handler om at lære at bruge librariet MechanicalSoup til at interegere med en hjemmeside. Tutoriallen viser hvordan man kan logge ind på en hjemmeside via koden. Dette kan ses gjort i opgave_1.py linje 77 til 89.

    Sidste del af tutoriallen demonstrerer bare hvordan man kan scrape en hjemmeside i real-time. Dette vises ved at bruge en hjemmeside der "ruller" en terning hver gang den er reloaded. I opgave_1.py linje 93 til 109 viser jeg koden, man kan bruge til at reloade samme side, og få nye resultater ud. time.sleep() bliver bare brugt til at lave et lille delay mellem hver iteration af loppet.

Opgave 2
    Link til opgaveløsning: https://github.com/NikolajNim/AI_og_Data_miniprojekt/blob/main/Kursusgang_1/opgave_2.py

    Opgave 2 går ud på at optage lyd og billede via python. Det jeg valgte at gøre var, at skabe 2 klasser. en til video, og en til lyd. Derefter lavede jeg bare en simple funktion, som kan initialisere begge klasser og starte optagelserne af både lyd og video på samme tid.

Kursusgang 2:

    Til denne Kursusgang skulle være lære om at arbejde med databaser med værktøjet SQL. Opgaveløsningen kan findes her: 
        

        




        
    

