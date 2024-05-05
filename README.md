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
    Opgave 1.
        Til denne opgave har jeg lavet et script, som kan findes her: https://github.com/NikolajNim/AI_og_Data_miniprojekt/blob/main/Kursusgang_3/opgave_1.py
        Det første der skal gøres i denne opgave, det er tage et gråskala billede og tilføje impulsiv støj/salt and pepper noise. Jeg har valgt at bruge det klassiske image processing billede lena.jpg.
        For at tilføje denne støj, så lavede jeg en funktion som modtager billede og en noise_ratio som parametre. Grunden til noise_ratio parameteren er, at det gør det muligt at ændre volumen af støj nemt. Funktionen kan ses fra linje 5 til 19. Den udregner mængden af støjpunkter baseret på noise_ratio, og derefter bruger den et for-loop til at tilfældigt tilføje støj til billedet.
        Den næste del af opgaven går ud på at implementere et middelværdisfilter, som bruger en kernal på 3x3. Dette filter skal da bruges på det støjfulde billede, for at prøve at reducere støjen, middelværdisfilteret bliver implementeret med en funktion på linje 21 til 22.
        Efter middelværdisfilteret, så skal der implementeres et medianværdisfilter, som også skal bruges på det stæjfulde billede for at reducere støj. Funktionen til dette filter kan ses på linje 24 til 25.
        Til sidst i scriptet bliver alle fire variationer af billedet vist. Det originale, det støjfulde, det middelværdisfilterede og det medianværdisfilterede. Og som man kan se, så virker medianfiltrering meget bedre i dette tilfælde til at fjerne støjen fra billedet.

    Opgave 2. 
        Til denne opgave har jeg lavet et nyt script, som kan findes her: https://github.com/NikolajNim/AI_og_Data_miniprojekt/blob/main/Kursusgang_3/opgave_2.py
        Til denne opgave har jeg igen brugt lena.jpg til at lave image processing. Jeg har lavet en funktion, som tager billedet, en mean og sigma som parameter til at tilføje gaussisk støj til billedet. Denne funktion kan ses på linje 4 til 8. Derefter lavede jeg de samme funktioner som i sidste opgave til middelværdisfilter og medianværdisfilter, disse funktioner kan ses på linje 10 til 11 og linje 13 til 14.
        Outputtet af dette script viser så, i forhold til den tidligere opgave, at middelværdisfilteret og medianfilteret ikke har den største effekt på billedet med gaussisk støj. Der kan være flare årsager til dette. En af årsagerne kan f.eks være at kernalen ikke er stor nok til at udføre filtreringen.

    Opgave 3.
        Til denne opgave skal jeg følge en guide til at forstå hvordan PCA kan bruges til støjreduktion. Guiden har noget kode, som man skal bruge til dette. Koden kan ses her: https://github.com/NikolajNim/AI_og_Data_miniprojekt/blob/da2b57a1ca6c916b4b2c6ca9a5b23e1909477d94/Kursusgang_3/opgave_3.py
        I denne guide bliver der både lavet en lineær PCA og en kernal PCA. Selve opgaven her vil fokusere på at forstå lineær PCA. Det første der sker er, at PCA'en bliver trænet med fit() funktionen til det noisey data, og det gør den ved en beregning af hovedkomponenterne. Det næste indebærer at bruge transform() funktionen til at transformere datasættet, ved at projectere data'en ned på et nyt koordinatsystem, hvor de nye koordinater er projektionerne af dataen på de identificerede hovedkomponenter. For så at kunne se hvilken effekt på billederne denne tranformation har haft, så bruger inverse_transform() funktionen til at reconstruere data'en, så det bliver til billeder man plotte. Og meningen er så, at efter inverse_transform(), så burde data'en været reduceret for støj. I denne specifikke opgave, jeg har valgt at kigge lege lidt med mængden af komponenter og variancen mellem hver komponent. Det viser jeg, at der i alt er 256 komponenter, hvis man ikke sætte n_components parameteren til noget i PCA'en. Dette betyder, at variancen er spredt meget ud, hvilken kan have en effekt på hvor godt PCA'en reducerer støj. På linje 38 i koden printer jeg pca.explained_varience_ratio_*100 variablen for at se hvor mange procent hver af komponenter repræsenterer. De først 17 komponenter repræsenterer næsten 50% ud af alle 256, hvilket betyder af 239 sidste komponenter ikke har nogen stor inflydelse.


    

