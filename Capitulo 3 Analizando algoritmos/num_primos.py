# Función para determinar numeros primos 

def num_primo(num):
   list_num = [2]
   bandera = False      
   
   num += 1
   for i in range(num):
    if i >=3:
      for j in list_num:
        if i % j == 0:
          bandera = True

      if not bandera:     
        list_num.append(i)
      bandera = False
  
   print(f"Números primos encontrados: {list_num}")

# Main 
numero = int(input("Ingrese número: "))
num_primo(numero)
