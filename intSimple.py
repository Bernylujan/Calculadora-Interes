# Calculadora de interes simple y compuesto (con tabulador).


def calcIntSimple():
    intSimple = (presente * numPeriodos * tasaInteres)
    print("Su Interes Simple es: " + str(intSimple))

def calcFuturo(): 
    intSimple = (presente * numPeriodos * tasaInteres)
    cantFinal = (intSimple + presente)
    print("Su Cantidad Final a pagar es: " + str(cantFinal))

def eachPeriodo(): 
    i = 0 
    n = 1 
    print("|| Periodo || Interes || Cant ")
    while i < (numPeriodos + 1): 
        interes = (presente * n * tasaInteres)
        
        print(f"|| {i}       ||  {interes}   || {presente} ")


        i += 1

presente = int(input("Ingrese su valor Presente: "))
numPeriodos = int(input("Ingrese su Numero de Periodos: "))
tasaInteres = float(input("Ingrese su Tasa de Interes: "))
print("==============================")
calcIntSimple()
print("==============================")
calcFuturo()
print("==============================")
eachPeriodo()