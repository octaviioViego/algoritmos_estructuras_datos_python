# ver si es mayor de edad o no
def eres_mayor(edad):
    # O(1)
    if edad > 18:
        # O(1)
        print("Eres mayor de edad.")
    else:
        # O(1)
        print("No eresmayor edad.")
    # El total del Big O es de I -> O(I)

# Main 
edad = int(input("Ingresa edad: "))
eres_mayor(edad=edad)