hora=int(input("Ingrese la cantidad de horas trabajadas\n"))
precioh=int(input("Ingrese el precio por hora trabajada\n"))
def mas40(hora, precioh):
    hora2=hora-40
    total1=hora2*(precioh*1.5)+(precioh*40)
    return total1
def menos40(hora, precioh):
    total=hora*precioh
    return total
if hora>40:
    print(mas40(hora, precioh))

else:
    print(menos40(hora, precioh))