def numero_divicible(numero):
    lista_numero_divicibles = [2,3,5,7]

    for i in lista_numero_divicibles:
        if numero % i == 0:
            return numero//i,i 
    
    return 0

def culcular_raiz(numero):
     
    numero , divisor = numero_divicible(numero=numero)

    if numero == 1:
        return divisor

    # Aun no terminado..............
    lista = divisor,culcular_raiz(numero=numero) 

    return lista    
    

print(culcular_raiz(180))
