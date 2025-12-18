#Suma de los n primeros numeros naturales
def suma_naturales(n):
    if n ==0:
        return 0
    else:
        print("suma de naturales:" ,n)
        return n + suma_naturales(n-1)
    
# Solicitar número
numero = int(input("Ingrese un número natural: "))
# Validar si es un número natural
if numero < 0:
    print("Por favor, ingrese un número natural (0 o positivo).")
else:
    resultado = suma_naturales(numero)
    print(f"La suma de los primeros {numero} números naturales es: {resultado}")
# Fin del programa