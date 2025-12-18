"""
Dada una secuancia de caracteres, obten dicha secuencia invertida.
"""

#Inversion de cadena resursivamente
def inversion_cadena(cadena,tamano):
	
	if tamano == 0:
		return cadena[tamano] 
	
	return cadena[tamano] +  inversion_cadena(cadena,tamano-1)

#Solicitamos una cadena
cadena = input("Ingresa una frase:")
tamano = len(cadena) - 1
lista_caracteres_invertidos = (inversion_cadena(cadena=cadena,tamano=tamano))
print(lista_caracteres_invertidos)
