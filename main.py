''' cb.txt  http://www.infojegyzet.hu/erettsegi/informatika-ismeretek/kozep-prog-2019okt/
• a bejegyzés percéhez tartozó óra, egész szám (6–13), például: 6
• a bejegyzés percértéke, egész szám (0–59), például 1
• a megadott percen belül a sofőr által indított adások száma, egész szám, például: 3
• a sofőr beceneve, szöveges adat, például: Bandi
﻿Ora;Perc;AdasDb;Nev
6;0;2;Laci
'''

class CB:
    def __init__(self, sor):
        s = sor.strip().split(';')
        self.ora =  int(s[0])
        self.perc = int(s[1])
        self.adas = int(s[2])
        self.nev =      s[3]

# 6. Készítsen AtszamolPercre azonosítóval egész típusú értékkel visszatérő metódust vagy függvényt, ami a paraméterként megadott óra- és percértéket percekre számolja át! Egy óra 60 percből áll. Például: 8 óra 5 perc esetén a visszatérési érték: 485 (perc).

def AtszamolPercre(ora, perc):
    return ora * 60 + perc 

with open("cb.txt") as sr:
    elsosor = sr.readline()
    lista = [CB(sor) for sor in sr]

# 3. Határozza meg és írja ki a képernyőre a minta szerint, hogy hány bejegyzés található a forrásállományban!

print(f"3. feladat: Bejegyzések száma: {len(lista)} db")

# 4. Döntse el és írja ki a képernyőre a minta szerint, hogy található-e a naplóban olyan bejegyzés, amely szerint a sofőr egy percen belül pontosan 4 adást indított! A keresést ne folytassa, ha az eredményt meg tudja határozni!

van_negy_adas = False
for item in lista:
    if (item.adas == 4):
        van_negy_adas = True
        break

if van_negy_adas:
    print(f"4. feladat: Volt négy adást indító sofőr.")
else:
    print(f"4. feladat: Nem volt négy adást indító sofőr.")
        
# 5. Kérje be a felhasználótól egy sofőr nevét, majd határozza meg a sofőr által indított hívások számát a napló bejegyzéseiből! Az eredményt a minta szerint írja ki a képernyőre! Ha olyan sofőr nevét adja meg a felhasználó, aki nem szerepel a naplóban, akkor a „Nincs ilyen nevű sofőr!” mondat jelenjen meg!

nev = input("5. feladat: Kérek egy nevet: ")
hivasok = [ sor.adas for sor in lista if sor.nev == nev ]
if hivasok: 
    print(f"        {nev} {sum(hivasok)}x használta a CB rádiót.")
else:
    print(f"        Nincs ilyen nevű sofőr.");

# 7. Készítsen szöveges állományt cb2.txt néven, melybe a forrásállományban található bejegyzéseket írja ki új formátumban! Az órákat és a perceket percekre számolja át az előző feladatban elkészített metódus (függvény) hívásával! Az új állomány első sorát és az adatsorokat a minta szerint alakítsa ki!

with open("cb2.txt", 'w') as sw:
        sw.writelines("Kezdes;Nev;AdasDb")
        for sor in lista:
            kezdes = AtszamolPercre( sor.ora, sor.perc)
            sw.writelines(f"{kezdes};{sor.nev};{sor.adas}")

# 8. Határozza meg és írja ki a minta szerint a sofőrök számát a forrásállományban található becenevek alapján! Feltételezheti, hogy nincs két azonos becenév.
        
statisztika = dict()
for sor in lista:
    statisztika[sor.nev] = statisztika.get(sor.nev, 0) + sor.adas
            
print(f"8. feladat: Sofőrök száma: {len(statisztika)} fő");

# 9. Határozza meg a legtöbb adást indító sofőr nevét! A sofőr neve és az általa indított hívások száma a minta szerint jelenen meg a képernyőn.
max_nev = max(statisztika, key=statisztika.get)
print(f"9. feladat: Legtöbb adást indító sofőr")
print(f"        Név: {max_nev}")
print(f"        Adások száma: {statisztika[max_nev]} alkalom")
