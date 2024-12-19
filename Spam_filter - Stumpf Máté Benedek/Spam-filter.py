#Algoritmusok tervezése és elemzése - Spam filter
#Készítette: Stumpf Máté Benedek - HWS19X

import re
import sys

# Gyakori spam kulcsszavak és kifejezések
spam_kulcsszavak = ["nyeremény","nyereményjáték", "ingyen", "kattints ide", "ajánlat", "gyors pénz", "növeld a bevételed", "pénzkeresési lehetőség"]

# URL-ek keresésére használt minta
url_minta = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}"

def bemenet_olvasasa():
    #Beolvassa a teljes bemenetet és megtisztítja.
    print("Kérlek, másold be a szöveget (több soros is lehet). Ha végeztél, nyomd meg a Ctrl+D-t (pycharm IDE) vagy a Ctrl+Z-t:")
    bemenet = sys.stdin.read()  # Beolvassa az összes sort nyers bemenettel, így tudunk több sort egyszerre bevinni
    return bemenet.strip().replace("\n", " ")  # A sortöréseket szóközzé tesszük

def spam_filter(szoveg):

    #Ellenőrzi, hogy a szöveg spam-e, és visszaadja a talált gyanús elemeket (kulcsszavak és URL-ek).

    szoveg = szoveg.lower()  # Kisbetűsre alakítjuk a szöveget
    talalt_kulcsszavak = {} #kulcsszavak tárolásához szükséges lista


    # Kulcsszavak keresése és a megjelenésük megszámlálása
    for kulcsszo in spam_kulcsszavak:
        elofordulas = szoveg.count(kulcsszo)
        if elofordulas > 0:
            talalt_kulcsszavak[kulcsszo] = elofordulas

    # URL-ek keresése
    talalt_url = re.findall(url_minta, szoveg)

    # Ellenőrizzük, hogy van-e 'http' URL és figyelmeztessünk a nem biztonságos tanúsítványra
    nem_biztonsagos_url = [url for url in talalt_url if url.startswith("http://")]

    # A szöveg spam, ha találunk kulcsszavakat vagy URL-eket
    is_spam = bool(talalt_kulcsszavak or nem_biztonsagos_url)

    return is_spam, talalt_kulcsszavak, talalt_url, nem_biztonsagos_url

def main():
    # Bemenet beolvasása és tisztítása
    szoveg = bemenet_olvasasa()

    # Spam szűrés
    is_spam, talalt_kulcsszavak, talalt_url, nem_biztonsagos_url = spam_filter(szoveg)

    # Eredmény kiírása
    if is_spam:
        print("Az email valószínűleg SPAM!")
    else:
        print("Az email valószínűleg NEM SPAM.")

    # Talált kulcsszavak és URL-ek listázása
    if talalt_kulcsszavak:
        print("Talált spam-re utaló kulcsszavak és előfordulásaik:")
        for kulcsszo, db in talalt_kulcsszavak.items():
            print(f"- {kulcsszo}: {db} alkalommal")

    #itt az URL-eket akkor listázza ki ha az email spamnek minősül
    if talalt_url and is_spam:
        print("Talált gyanús URL-ek:")
        for url in talalt_url:
            print(f"- {url}")

    # Nem biztonságos http URL-ek figyelmeztetése
    if nem_biztonsagos_url:
            print("Figyelmeztetés: A következő URL-ek tanúsítványa nem biztonságos:")
            for url in nem_biztonsagos_url:
                print(f"- {url}")

if __name__ == "__main__":
    main()
