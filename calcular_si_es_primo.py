n = int(input("Ingrese un número: "))

def es_primo(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True 

if es_primo(n):
    print(f"{n} es un número primo")
else:
    print(f"{n} no es un número primo")