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

    Til denne Kursusgang skulle være lære om at arbejde med databaser med værktøjet SQL. Opgaveløsningen kan findes her: https://github.com/NikolajNim/AI_og_Data_miniprojekt/blob/8508b3e104e90466484f0d832dc59667113c0269/Kursusgang_2/sql.py

    Opgaven til denne kursusgang er delt op i 5 dele. Jeg skriver opgavens nr. og beskriver hvor i koden jeg har løst den.
    
    Opgave 1. Skriv et Python script der opretter en SQLite database ‘school.db’:
         Opgaven bliver løst på linje 1 til 14, hvor først så importer jeg librariet sqlite3, derefter definerer jeg create_connection funktionen, som modtager en path som parameter. Denne funktion opretter forbindelse til databasen, som ligger i den path, men hvis der ikke er nogen database til at starte, så laver den en ny database. 

    Opgave 2. Udvid scriptet til at oprette to tabeller ‘Students’ og ‘Courses’.
        For at kunne løse denne opgave, så skal jeg definere en funktion, som kan tage fat i forbindelsen til databasen, også udføre nogle forespørgelser, som i SQL hedder queries. Denne funktion bliver defineret på linje 16 til 23 og hedder execute_query(). Derefter skal der laves queries, som er en slags ordre til databasen. Til denne opgave skal jeg lave 2 queries. En til at tilføje en student tabel, som skal indeholde deres student id, navn og major. Den anden query skal oprette en course tabel, som skal indeholde course id, course navn og instruktør. Student querien kan ses konstrueret på linje 25 til 30, og course querien er kontrueret på linje 32 til 37. Disse queries består af strenge, der indeholder keywords, som kan læses med SQL for at udføre forespørgelsen, i dette tilfælde er CREATE TABLE keywordet der bliver brugt. De er derefter smidt ind i execute_query() funktionen som parametre sammen med forbindelsen til databasen, dette kan ses på linje 82 og 83. Dette tilføjer tabellerne til databasen.

    Opgave 3. Indsæt mindst 5 records i hver tabel:
        For så at tilføje data til mine tabeller, så skal igen konstruere nogle queries, som skal executes med execute_query() funktionen. Disse queries bruger INSERT INTO keywordsne til at tilgå den tabel dataen skal ind i, og derefter skrive keywordet VALUES for selve de datapunkter der skal indsættes. Student datapunkter bliver oprettet i querien på linje 50 til 59, og querien for coursesne bliver oprettet på linje 60 til 69. til sidst bliver disse queries executet i execute_query() funktionen på linje 84 og 85.
    
    Opgave 4. Opret en tredje tabel ‘Enrollments’ der opretter relationer mellem Students og Course:
        For at lave denne nye tabel, skal en ny query laves, som er magen til de tidligere, dog med den undtagelse, at når man vil oprette reletioner til andre tabeller, så skal man bruge andre keywords, som hedder FOREIGN KEY og REFERENCES, så man kan se at data punkt A i tabel A skal referere til datapunkt A i tabel B. Denne query der opretter denne tabel kan ses i linje 39 til 48. Jeg lavede også en query som tilføjer de forskellige datapunkter til enrollment tabellen i linje 71 til 80.
    
    Opgave 5. Lav forespørgsler (queries) der vælger alle kurser som en specific studerende er tilmeldt og vælger alle studerende der er tilmeldt et specifikt kursus:
        For at løse disse 2 dele af opgave, så lavede jeg 2 funktioner, som kan i linje 89 til 100 og linje 108 til 119. I disse funktioner opretter queries der bruger keywordsne SELECT FROM til at tilgå enrollment tabellen for den information der er brug for.
        Derefter får jeg funktioner til at retunere en liste af courses i en ene og en liste af studerende i den anden. Koden der gør alt dette kan ses fra linje 89 til 125.

Kursusgang 3:
    
    
    
        
        
        

        




        
    

