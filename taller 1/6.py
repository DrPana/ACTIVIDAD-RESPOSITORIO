def ultimos2numeros(año):
    año2=año%100
    return año2
def formato(dia,mes,año):
    año=ultimos2numeros(año)
    print(f"{dia}/{mes}/{año}")
dia=int(input("Ingrese el dia\n"))
mes=int(input("Ingrese el mes\n"))
año=int(input("Ingrese el año\n"))
formato(dia,mes,año)