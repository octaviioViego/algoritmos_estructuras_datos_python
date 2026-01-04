# Ver si es primo
def es_primo(num):
    #O(1)
    if num <= 1:
        return False
    #O(1)
    con = 0
    
    #O(n)
    for i in range(2, num+1):
        if num % i == 0:
            con += 1
    #O(1)    
    if con == 1:
        #O(1)
        return True
    else:
        return False
        

# Main. La Big O es 'n'.
numero = int(input("Ingrese número: "))

if es_primo(num=numero):
    print("Es primo.")
else:
    print("no es primo.")
