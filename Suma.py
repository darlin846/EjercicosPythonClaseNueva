# Escribe un programa que solicite al usuario al usuario dos números y los almacene
# en dos variables. En otra variable, almacena el resultadode la suma 
# de esos dos númer5os y luego mostrá ese resultadoen pantalla.
# A continuación, el programa dbe solicitar al usuario que ingrese un
# tercer número, el cual se debe almacenar en una nueva variable.
# Por último, mostrá en pantalla el resultado de la multiplicación
# este nuevo número por el resultado de la suma anterior.

primerNumero = int(input("Escribe el primer numero: "))
segundoNumero = int(input("Escribe el segundo numero: "))

suma = primerNumero + segundoNumero
print(suma)

terceroNumero = int(input("escribe numero: "))
multiplicación = terceroNumero * suma 
print(multiplicación)