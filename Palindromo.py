p=input("Escriba una palabra: ").lower()
P1=list(p)
P2=list(P1)
P2.reverse()
if P1==P2:
    print("ES UN POLINDROMO")
else:
    print("NO ES UN POLINDROMO")