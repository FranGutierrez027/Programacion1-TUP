import sys

sys.setrecursionlimit (20000)

#Definicion de funciones

def factorial (x):
    f = 1
    for i in range (1, x =1):
        f*= i
    return f

def factorial_recur (x):
    return 1 if x == 0 else x * factorial_recur(x-1)
#Programa principal

print( factorial(1500))
print(factorial_recur(1500))