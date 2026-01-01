# Función para calcular el finonacci de un número

def fibonacci(num):
   # O(1)
   if num == 0 or num == 1:
      return num
   # 
   return fibonacci(num -1) + fibonacci(num -2)


# Main
numero = int(input("Ingresa número: "))
numero = fibonacci(numero)
print(f"El valor de fibonacci es: {numero}")

