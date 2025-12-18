#Factorial recursivo

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        print("Factorial de:", n)
        return n * factorial(n - 1)
    

#Solicitar número
numero = int(input("Ingrese un número natuaral:"))

#Validar si es un número natural
if numero < 0:
    print("Por favor, ingrese un número natural (0 o positivo).")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
# Fin del programa
