"""
Desarrollar una función que permita convertir un número romano en un 
número decimal.
"""

#Calcula el valor del simbolo dado
def simbolo_decimal(simbolo):
      valor = simbolo
      if valor == 'I':
        representa = 1 
      elif  valor == 'V':
        representa = 5 
      elif valor == 'X':
        representa = 10	
      elif valor == 'L':
        representa = 50 
      elif valor == 'C':
        representa = 100 
      elif valor == 'D':
        representa = 500 
      elif valor == 'M':
        representa = 1000

      return representa


#Calcualar número romano recursivo
def numero_romano(numero,ini):
    tam = len(numero)
    if ini == tam :
      return 0
    
    
    valor = numero[ini]
    #print("Número de vez que entra a la función: ",ini )
    representa = simbolo_decimal(valor)
	
    ini = ini + 1
    siguienteNumero = numero_romano(numero,ini)
    # print("siguiente numero es: ", siguienteNumero)
    # print("El numero presente es: ",representa)
    if representa < siguienteNumero:
      return  siguienteNumero - representa 
    else:
      return representa + siguienteNumero


#Pedimos el número romano al usuario
numero = input("Ingresa el número romano  a covertir: ")

lista_numero_romano = []
for caracteres in numero:
	lista_numero_romano.append(caracteres)

ini = 0
numero_decimal = numero_romano(lista_numero_romano,ini)
print(f"El valor número romano a decimal es de: {numero_decimal}") 

#Fin del código
#Recuerda que python no se lleva bien con los tabuladores, así que usa espacios
