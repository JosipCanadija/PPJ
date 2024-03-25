"""
Implementirajte kontrolnu abstrakciju "iterate(s,isDone,transform)" (control abstraction u 2. poglavlju skripte), te 
pomoću nje implementirajte funkciju "rangeList(a,b,step)" koja vraća listu brojeva od a do b. Neka program bude što deklarativniji.
"""

def iterate(s, isDone, transform):
    if isDone(s):
        return s
    else:
        s1 = transform(s)
        return iterate(s1, isDone, transform)
    
def rangelist(a, b, step):
    result = []

    def isDone(x):
        return x > b
    
    def transform(x):
        result.append(x)
        return x + step
        
    iterate(a, isDone, transform)    
    
    return result

print(*rangelist(1, 20, 4))