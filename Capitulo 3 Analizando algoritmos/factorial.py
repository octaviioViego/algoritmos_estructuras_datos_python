# Funcion que calcula el factorial de un número

def factorial(num):
    if num == 1:
       return 1

    return num * factorial(num-1)

# Main
numero = int(input("Ingresa número: "))
numero = factorial(numero)
print(f"El valor factorial de número que ingresaste es: {numero}")
