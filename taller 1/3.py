def maxcomdiv1(num1, num2):
    while num2:
        num1,num2=num2,num1%num2
    return num1
def maxcomdiv2(num1, num2, num3, num4):
    max1=maxcomdiv1(num1, num2)
    max2=maxcomdiv1(num3, num4)
    max3=maxcomdiv1(max1, max2)
    return max3
num1=int(input("Ingrese el numero 1\n"))
num2=int(input("Ingrese el numero 2\n"))
num3=int(input("Ingrese el numero 3\n"))
num4=int(input("Ingrese el numero 4\n"))
total=maxcomdiv2(num1, num2, num3, num4)
print(f"El resultado de encontrar el maximo comun divisor de {num1} y {num2}, el maximo comun divisor de {num3} y {num4} y encontrar el maximo comun divisor de sus resultados es: {total}")