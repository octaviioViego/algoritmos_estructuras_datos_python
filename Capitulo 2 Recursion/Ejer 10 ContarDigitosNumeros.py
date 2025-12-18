"""
Desarrollar un algoritmo que cuente la cantidad de digitos en un número 
entero.
"""
#Contar cuantos digitos tiene un números 
def Digitos(numero,contador):
   
    numero = numero / 10
    contador = contador + 1
    if numero < 1 :
       return contador
    
    return  Digitos(numero,contador) 

#Solicitar el número
numero = int(input("Ingresa el número: "))
conteo_digitos = Digitos(numero,0)
print(f"El número de digitos que tiene el numero {numero} es: {conteo_digitos}")
