# Funcion que calcula el factorial de un número

def factorial(num):
    if num == 1:
       return 1
    
    # O(n)
    return num * factorial(num-1)

# Main
print("El big O es n O(n)")
numero = int(input("Ingresa número: "))
numero = factorial(numero)
print(f"El valor factorial de número que ingresaste es: {numero}")
