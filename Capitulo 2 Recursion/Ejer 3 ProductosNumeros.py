"""
Implentar una función para calcular el producto de dos números enteros.
"""
#Multipliación de dos números
def miltipliacion(num1,num2):
	if num2 <= 1:
		return num1
	
	return num1 + miltipliacion(num1,num2-1)
	

#Solicitamos número
num1 = int(input("Ingresa número uno: "))
num2 = int(input("Ingresa número dos: "))	
resultado = 0
if num1 == 0 or num2 == 0:
	print(f"resultado de la multiplicación de el número {num1} con el número {num2} es:{resultado}")
	exit()

resultado = miltipliacion(num1,num2)
print(f"resultado de la multipluación de el número {num1} con el número {num2} es: {resultado}")
