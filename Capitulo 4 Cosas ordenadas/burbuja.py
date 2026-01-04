# Algoritmo burbuja

def burbuja(lista):
    tamano_lista = len(lista)

    for i in range(0, tamano_lista):
        for j in range(0,tamano_lista - 1 - i):
            if lista[j] > lista[j+1]:
                lista[j] , lista[j+1] = lista[j+1], lista[j]
    return lista



def burbuja_mejorado(lista):
    # Bandera que nos indica que se recorrio todo la lista sin modificaciones
    bandera = True
    cont = 0
    tamano_lista = len(lista) - 1

    while(cont < tamano_lista and bandera):
        bandera = False
        for i in range(tamano_lista):
            if lista[i] > lista[i+1]:
                lista[i] , lista[i+1] = lista[i+1] , lista[i]
                print("Se metio a la comparación.")
                bandera = True
        cont += 1
    return lista


lista_numero = [1,2,4,3,5,6]

print(burbuja_mejorado(lista=lista_numero))