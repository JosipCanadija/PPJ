"""
Implementirajte u "CookBook" stilu program koji ima sljedeće:
a) Unos korisnika: niz nula i jedinica (npr. "01100010")
b) Izračun pozicija (indeksa) na kojima su jedinice ("01100010" --> [1,2,6])
c) Ispis niza koji sadrži "_" za nule i "X" za jedinice, koristeći listu indeksa

Primjer kako bi output trebao izgledati:
Input binarnog niza: 01100010
_XX___X_
"""
global binarni_niz
global jedinice

def unos():
    global binarni_niz
    binarni_niz = input()
    
def pozicije():
    global binarni_niz
    global jedinice
    
    jedinice = [i for i, j in enumerate(binarni_niz) if j == '1']
    
def ispis():
    global binarni_niz
    global jedinice
    
    niz = ['_' for _ in binarni_niz]
    for pozicija in jedinice:
        niz[pozicija] = 'X'
    print(''.join(niz))
    
unos()
pozicije()
ispis()