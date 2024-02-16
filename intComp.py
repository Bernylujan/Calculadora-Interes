presente = int(input("Ingrese su valor Presente: "))
numPeriodos = int(input("Ingrese su Numero de Periodos: "))
tasaInteres = float(input("Ingrese su Tasa de Interes: "))

intCompuesto =  presente * ((1 + tasaInteres) **  numPeriodos)

def calcIntCompuesto():
    print("Su Interes es de: " + str(round((intCompuesto - presente), 2)))

def calcFuturo(): 
    cantFinal = intCompuesto
    print("Su Cantidad Final a pagar es: " + str(round(cantFinal, 2)))

def eachPeriodo(): 
    
    print( "|| Periodo || Interes       || Cant ")
    print(f"||    0    ||       0       || {presente} ")
    
    i =  1
    cant = presente 
    while i < numPeriodos + 1: 
     resultado = cant * tasaInteres
     iCompuesto = round(resultado, 2)
     cant = round((cant + iCompuesto), 2)
     print(f"||    {i}    ||      {iCompuesto}    ||   {cant} ")
     i += 1

print("==============================")
calcIntCompuesto()
print("==============================")
calcFuturo()
print("==============================")
eachPeriodo()


