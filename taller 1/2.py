def fact(num):
    total=1
    for i in range(num):
        total= total*(i+1)
    return total
num1=int(input("Ingrese un numero\n"))
if num1 >= 100 and num1 <= 1000000:
    print(fact(num1))
else:
    print("El numero ingresado no es valido")