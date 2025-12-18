"""
Desarrollar un algoritmo que permita convertir un número entero en sistema decimal
a sistema binario.
"""
#Programa de decimal a binario recursivo
def convertidor(numero_decimal, iteracion):
    numero = (2**iteracion)
   
    if numero == numero_decimal or numero_decimal < (numero + numero):
       #print(f"Ultimo numero es: {numero}")
       print("1",end = " ")
       return numero
    else:
       ultimo_numero = convertidor(numero_decimal, iteracion + 1)
       if (ultimo_numero + numero) > numero_decimal:
          print("0", end = " ")
          return ultimo_numero 
      
       if(ultimo_numero + numero) == numero_decimal or (ultimo_numero + numero) < numero_decimal:
          print("1" , end = " ")
          return (ultimo_numero  + numero_decimal)
       
#Solicitar número 
numero = int(input("Ingresa un número: "))
print(f"En número {numero} a binario es:")
numero = convertidor(numero,0)
print()




