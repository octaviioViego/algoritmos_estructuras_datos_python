"""
Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.
"""
def invertir_numero(numero):
    
    
    calculo_residuo = numero % 10
    calculo_divisor = numero // 10 
    if calculo_divisor < 1:
        return calculo_residuo
    
    #Nota: Aunque dija el ejercicio que no convierta los número en cadenas esto aplica solamente para 
    # la realización de la operación de separar el número, sin embarlo solo por estetica el resultado lo 
    # ponemos ponemos como cadena. 
    return str(calculo_residuo) + str(invertir_numero(calculo_divisor))
    
# Ingresamos el número
numero = int(input("Ingresa número: "))
numero_invertido = invertir_numero(numero=numero)
print(f"Número invertido: {numero_invertido}")