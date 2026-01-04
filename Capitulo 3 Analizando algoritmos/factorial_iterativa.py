def factorial(num):
 
 # O(n)
 fac = 1
 for i in range(1,num+1):
     fac *= i

 return fac

# Main 
numero = int(input("Ingrese número: "))
print(f"Numero factorial es {factorial(num=numero)}")
