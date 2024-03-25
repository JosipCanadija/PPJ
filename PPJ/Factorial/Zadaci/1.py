"""
Implementirajte deklarativno, funkcije factorial(n) i factorial_acc(n).
a) "factorial(n)" rekurzivno, bez akumulatora, izračunava faktorijel broja n.
b) "factorial_acc()" rekurzivno, sa akumulatorom izračunava faktorijel broja n.
"""
#a
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n = int(input())))

#b
def factorial_acc(n, acc = 1):
    if n == 0:
        return acc
    else:
        return factorial_acc(n-1, acc*n) 
    
print(factorial_acc(n = int(input())))