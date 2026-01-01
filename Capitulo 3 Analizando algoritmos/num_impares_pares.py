# Funcion en python que determina números pares e impares

# El total de nuestra funcion es de orden  O(n). 
# las otras dos instrucciones restantes del algoritmo
# (la primera y la última) son operaciones elementales de O(1) y se desprecian respecto al orden del ciclo for.

def num_par_impar(num):
    cont_impares = 0
    # O(n) es de orden n 
    for i in range(num):
      # O(Total de la desición) es de O(3)
      # O(1) Esto por la comparación
      if i % 2 == 0:
        print(f"El número {i} es par.")
      #O(2) Esto por la suma y la asignación
      else:
        cont_impares += 1
        print(f"El número {i} es impar.");
    return cont_impares

# Main
numero = int(input("Ingrese número: "))
cont = num_par_impar(numero) 
print(f"El número de impares fue: {cont}")
