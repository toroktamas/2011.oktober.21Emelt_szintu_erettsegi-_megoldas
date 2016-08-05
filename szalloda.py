#!/usr/bin/python3
# -*- codnig:utf-8 -*-
print("1. feladat")
"""Be kell olvasni a pitypang.txt egy szotarba ami a kovetkezo keppen nez ki.
szalloda = {
foglalass sorszama{
"szoba szam":(1-27)
"erkezes napjanak sorszama":datetime
"tavozas nepjanak sorszama": datetime
"vendeg szam":(max 3)
"Ker-e reggelit":1=igen vagy 0=nem
"Foglalast vegzo vendeg neve":25karakter max
"Fizetendo osszeg" = kikell szamolni
 }
}
"""
from datetime import datetime, timedelta
szalloda = {}
n = 0
kezdes = datetime(2011,1,1,1,1,1)
with open("pitypang.txt", "rt+", encoding="utf-8") as f:
    for s in f:
        sor = s.replace("\n", "").split(" ")
        n+=1
        if n > 1:
            key = sor[0]
            erkezes = kezdes+timedelta(days=int(sor[2]))
            tavozas = erkezes+timedelta(days=int(sor[3]))
            szalloda[key] = {}
            szalloda[key]["szoba szam"] = sor[1]
            szalloda[key]["erkezes sorszam"] = sor[2]
            szalloda[key]["tavozas sorszam"] = sor[3]
            szalloda[key]["erkezes napjanak sorszama"] = erkezes
            szalloda[key]["tavozas napjanak sorszama"] = tavozas
            szalloda[key]["napok szama"] = int(sor[3])-int(sor[2])
            szalloda[key]["vendegek szam"] = int(sor[4])
            szalloda[key]["Ker-e reggelit"] = sor[5]
            szalloda[key]["neve"] = sor[6:]
            fizetendo = 0
            if erkezes.month == 12 or erkezes.month == 11 or erkezes.month == 10 or erkezes.month == 9:  
                fizetendo+=(8000*int(sor[3])-int(sor[2]))
                if sor[4] == 3:
                    fizetendo+=(2000*int(sor[3])-int(sor[2]))
                if sor[5] == 1:
                    fizetendo+=((1100*int(sor[3])-int(sor[2]))*int(sor[4]))
            elif erkezes.month == 8 or erkezes.month == 7 or erkezes.month == 6 or erkezes.month == 5:
                fizetendo+=(10000*int(sor[3])-int(sor[2]))
                if sor[4] == 3:
                    fizetendo+=(2000*int(sor[3])-int(sor[2]))
                if sor[5] == 1:
                    fizetendo+=((1100*int(sor[3])-int(sor[2]))*int(sor[4]))
            elif erkezes.month == 4 or erkezes.month == 3 or erkezes.month == 2 or erkezes.month == 1:
                fizetendo+=(9000*int(sor[3])-int(sor[2]))
                if sor[4] == 3:
                    fizetendo+=(2000*int(sor[3])-int(sor[2]))
                if sor[5] == 1:
                    fizetendo+=((1100*int(sor[3])-int(sor[2]))*int(sor[4]))
            szalloda[key]["Fizetendo osszeg"] = fizetendo
            
            
            
#print(szalloda)
with open("sem.txt", "wt",encoding="utf-8") as f:
    for k, v in szalloda.items():
        f.write(str(k)+":"+str(v)+"\n")
        
print("2. feladat")
"""Lehosszabb tartozkodast ki kell venni """
legnagyobb = []
for a in szalloda.values():
    if a["napok szama"] not in legnagyobb:
        legnagyobb.append(a['napok szama'])
for f in szalloda.values():
    if max(legnagyobb) == f['napok szama']:
        print("{0} ({1}) - {2}".format(" ".join(f["neve"]),f['erkezes sorszam'],max(legnagyobb)))
print("3. feladat")
"""Ki kell fajlba irni hogy mennyit kell fizetni eggyes vendegeknek es a kepernyore hogy menyi volt az ossz bevetel."""
with open("bevetel.txt", "wt",encoding="utf-8") as f:
    for k, v in szalloda.items():
        f.write(str(k)+":"+str(v["Fizetendo osszeg"])+"\n")
        
bevetel = 0
for a in szalloda.values():
    bevetel+=int(a["Fizetendo osszeg"])
print("Ossz bevetel: {} Ft".format(bevetel))
print("4. feladat")
"""Statisztikat kell kesziteni hogy havonta mennyi volt a vendegeszaka """
""" vendegeszaka egy ember egy eszakat tolt el
csinalok hozza egy szotarat mai igy nezne ki:
statisztika = {honap:ejszakak szama}
"""
statisztika = {}
honap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for f in szalloda.values():
    ejszakak_szama = 0
    for a in honap:
        if a not in statisztika.keys():
            if f['vendegek szam'] == 1:
                ejszakak_szama+=f['napok szama']
            elif f['vendegek szam'] == 2: 
                ejszakak_szama+=f['napok szama']+f['napok szama']
            elif f['vendegek szam'] == 3:
                ejszakak_szama+=f['napok szama']+f['napok szama']+f['napok szama']
            statisztika[a] = ejszakak_szama
        else:
            if f['vendegek szam'] == 1:
                ejszakak_szama+=f['napok szama']
            elif f['vendegek szam'] == 2: 
                ejszakak_szama+=f['napok szama']+f['napok szama']
            elif f['vendegek szam'] == 3:
                ejszakak_szama+=f['napok szama']+f['napok szama']+f['napok szama']
            statisztika[a] += ejszakak_szama
            
for c ,d in statisztika.items():
    print("{0}: {1} vendegej".format(c, d))
    
print("5. feladat")
"""Be kell kerni egy uj nap sorszamat ami a kezdesi idopont es egy masikat ami a vege idopont es meg kell hatarozni hogy abban az idoben melyik szobak uresek. """
"""bekezdes = int(input("Kerem adja meg az uj foglalas kezdo datumanak sorszamat: "))
vege = int(input("Kerem adja meg az uj foglalas vegenek a sorszamat: "))
bhe = str(bekezdes)+":"+str(vege)
szobak = {}
szam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
for s, d in szalloda.items():
    if d['szoba szam'] not in szobak:
        szobak[d["szoba szam"]] = [str(d['erkezes sorszam'])+":"+str(d['tavozas sorszam'])]
    else:
        szobak[d["szoba szam"]].append(str(d['erkezes sorszam'])+":"+str(d['tavozas sorszam']))

print(szobak)

for e, i in szobak.items():
    if i != bhe:
        print("ures szoba:{}".format(e))
    
"""