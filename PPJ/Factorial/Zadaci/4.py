"""
Implementirajte program iz 3. zadatka u "Kick Forward" stilu
"""
def Unos(func):
    binarni_niz = input("binarni niz:")
    func(binarni_niz, ispis)

def pozicije(binarni_niz, func):
    jedinice = [i for i, j in enumerate(binarni_niz) if j == '1']
    func(binarni_niz, jedinice)
    
def ispis(binarni_niz, jedinice):   
    niz = ['_' for _ in binarni_niz]
    for pozicija in jedinice:
        niz[pozicija] = 'X'
    print(''.join(niz))
    
Unos(pozicije)