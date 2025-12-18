"""
Implementar una función para calcular la potencia dado dos números enteros, el 
primero representa la base y segundo el exponente
"""
#Potencia de dos números recursivamente
def potencia(base,exponente):
	if exponente <= 1:
		return base
	
	return base * potencia(base, exponente-1)

#Solicitamos la base y el exponente
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

if exponente == 0:
	print("El resultado es: 1")
else:
	resultado = potencia(base,exponente)
	print(f"El resultado es: {resultado}")

