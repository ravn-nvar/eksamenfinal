
import random
import difflib
#jeg har tænkt mig at lave et quizz program, så det er meget simplet. Brugeren vælger hvor mange spørgsmål og svare så på de spørgsmål.
while True:
    klar = input("er du klar til en quiz?! (ja/nej)").lower().strip()
    if klar == "ja":
        print("alrighty, lad spillet begynde!")
        break
    elif klar == "nej":
        print ("okay så....")
        break
    else:
        print("Du skal svare ja/nej din numse!")

Spørsgmål = [
    "hvad er danmarks hovedstad?",
    "hvad er er python?",
    "hvad er forkortelsen for en computer?",
    "hvad er verdens største land?",
    "hvad er hovedstaden i tyskland?",
    "Hvor ligger paris?"
]
#Meget simple spørgsmål, så kreativ er jeg heller ikke.
Svar = [
    "København",
    "Et programmeringssprog",
    "Pc",
    "Rusland",
    "Berlin",
    "Frankrig"
]

score = [0]
#score. så ved vi hvor mange gange vi svare rigtigt.
while True:
    antal = int(input("Hvor mange spørgsmål vil du have? (1-6) "))
    if 1 <= antal <= 6:
        print("du har valgt", antal, " spørgsmål")
        break
    else:
        print("Du skal vælge et tal mellem 1 og 6")

for i in range(antal):
    tilfældig = random.randint(0, len(Spørsgmål) - 1)
    print("Spørgsmål", i + 1, ":", Spørsgmål[tilfældig])
    svar = input("Dit svar: ").strip().lower()
    
    korrekt = Svar[tilfældig].lower()
    if difflib.SequenceMatcher(None, svar, korrekt).ratio() > 0.6 or korrekt in svar:
        print("Korrekt!")
        score[0] += 1
    else:
        print("Forkert! Det korrekte svar er:", Svar[tilfældig])
    del Spørsgmål[tilfældig]
    del Svar[tilfældig]
#UHA! den er ny, difflib. det gør simpelt hen bare at den sammenligner brugerens input med det rigtige svar, og hvis det er over 60% sammenligning så går det igennem. 
#det gør at den er ordblind venlig og at hvis man manngler et mellem rum eller et bogstav så går det stadig igennem.
print("Din score er:", score[0], "ud af", antal)
if score[0] == antal:
    print("Fantastisk! Du fik alle spørgsmål rigtigt!")
print("Tak for spillet!")
