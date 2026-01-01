"""
Implementar una funcion que permita obtener el valor en la sucesión de Fibonacci 
para un número dado.
"""
#Serie de fibonacci recursivamente
def fibonacci(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

#Solicitar número 
numero = int(input("Ingresa número: "))
if numero<0:
	print(f"El número ingresado {numero} no es válido, ingrese número mayor a cero.")
else:	
	numero=fibonacci(numero)
	print(f"Número de fibonacci es: {numero}")
#Fin del programa
