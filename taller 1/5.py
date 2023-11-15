def operacion(x,n):
    total=x
    for i in range(n-1):
        total=total*x
    return total
x=float(input("Ingrese el numero X\n"))
n=int(input("Ingrese el numero N\n"))
resultado=operacion(x,n)
print (resultado)