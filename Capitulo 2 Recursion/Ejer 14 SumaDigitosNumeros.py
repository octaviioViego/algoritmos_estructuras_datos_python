"""
Desarrollar un algoritmo que permita realizar la suma de los digitos de un número
entero, no puede convertir el número a cadena.
"""
#Suma de los digitos de un número recursivo
def SumaDigitos(numero,contador):
 
    if numero == 0:
       return (contador + numero)
    else:
       contador = (numero % 10) + contador

       numero = int(numero/10)
       return SumaDigitos(numero, contador)

#Solicitar un número
numero = int(input("Ingresa un número: "))
suma_numeros = SumaDigitos(numero,0)
print(f"La suma de los digitos del número {numero} es: {suma_numeros} ")
