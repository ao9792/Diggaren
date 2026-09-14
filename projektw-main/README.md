Användarmanual

Installationsinstruktioner
Steg 1. Extrahera den nedladdade zipfilen viktigt att den heter projektw.zip
Steg 2. Öppna den nedladdade mappen projektw i ditt programmeringsprogram.
Steg 3. Öppna en ny terminal i det program du programmerar i. 
Steg 4. Efter det skriver du in (pip install -r requirements.txt) eller (pip3 install -r requirements.txt)
(Steg 5.) Det kan ibland behövas installera spotipy uvicorn fastapi. pip install spotipy uvicorn fastapi eller pip3 install spotipy uvicorn fastapi 
Nu ska allt nödvändigt vara installerat för att kunna köra programmet.

!!! Vid körfel byt directory på nedan i main.py och pages.py till:

templates = Jinja2Templates(directory="../templates")
app.mount("/static", StaticFiles(directory="../static"), name="static")

Alternativ körning är:
Steg 1. Extrahera den nedladdade zipfilen viktigt att den heter projektw.zip
Steg 2. Öppna den nedladdade mappen projektw i mappen projektw i ditt programmeringsprogram.
Steg 3. Öppna en ny terminal i det program du programmerar i och skriv in: cd /Users/YOURNAME/Downloads/projektw/python (Viktigt att det står ditt användarnamn för din dator samt projektw och inte projektw 1 som det kan stå om det laddats ner tidigare.)
Steg 4. Efter det skriver du in (pip install -r requirements.txt) eller (pip3 install -r requirements.txt)
(Steg 5.) Det kan ibland behövas installera spotipy uvicorn fastapi. pip install spotipy uvicorn fastapi eller pip3 install spotipy uvicorn fastapi
Nu ska allt nödvändigt vara installerat för att kunna köra programmet.
Steg 6. efter det skriver du in i terminalen: python main.py eller python3 main.py (Då kan ovan ändring med directory behövas)

Körinstruktioner
Kör programmet main.py och skriv in http://127.0.0.1:8080/ i valfri webbläsare. Alternativt kör den via terminalen med ovan istruktioner (testa båda om ena inte fungerar)
Du möts av startsidan med enbart en knapp “Jag vill digga nu” som tar dig till nästa sida (tryck på den).
Nästa sida är sidan du kan välja ifall du vill kolla upp låtar på p2 eller p3. Tryck på en av dem.
Nu öppnas sidan upp för respektive p2 eller p3 där nuvarande låt som spelas på radion visas, samt föregående låt. Testa att trycka på “lyssna på Spotify", denna knapp ska visa upp samma låt på Spotify som visades på p2 eller p3.
Det finns även möjlighet att hitta våra kontaktuppgifter på “kontakta oss” samt gå tillbaka till startsidan på “Diggaren”.
Nu har du kört igenom hela vårt program!

