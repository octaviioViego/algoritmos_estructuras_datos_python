# Algoritmo de busqueda binaria

# O(log2 n) 
def busqueda_binaria(lista_num,num,ini,fin):
    
    # O(1) Lineal 
    if ini > fin:
      print("No se entontro el número.")
      return 

    mitad = (ini + fin) // 2

    if num == lista_num[mitad]:
       print(f"Encontramos el número {num} en la posición {mitad+1}")
       return 

    if num > lista_num[mitad]:
      ini = mitad + 1
      print(f"inicio {ini}")
      return busqueda_binaria(lista_num,num,ini,fin)
    
    if num < lista_num[mitad]:
      fin = mitad - 1
      print(f"Fin {fin}")
      return busqueda_binaria(lista_num,num,ini,fin)

    
# Main 
lista = [1,2,3,4,5,6,7,8,9,10]
numero = 1
busqueda_binaria(lista,numero,0,len(lista)-1)

"""
n -> n/2^1 -> n/2^2 .... 1
  -> n/2^k
  -> n/2^k = 1
  -> n = 2^k
  -> log2(n) = k
"""