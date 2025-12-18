"""
Implementar una función que cañcule la suma de todos los números 
enteros comprendidos entre en cero y un número entero positivo dado.
"""
#Contar número regresivamente
def contar_numero(n):
	if n == 0:
		print(f"Número: {n} ")
		return 
	else:
		print(f"Número: {n}")
		return contar_numero(n-1)

#Solicitar número
numero = int(input("Ingrese número:"))

#Validar su el número es natural
if numero < 0:
	print("Por favor ingrese número natural poisitivo")
else:
	contar_numero(numero)

#Fin de programa
