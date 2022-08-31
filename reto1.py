#Entradas = Variables = Referencias en memoria:

#"None" es para asignar nada a una variable
#"Input" para solicitar valor
#"Elif" condicionales anidadas para cuando hay mas de una opcion 
nivelAgua = int (input("Digite el nivel de agua: "))

#proceso

if (nivelAgua>=0 and nivelAgua<20):
    #salidas
    print (f'El Nivel de agua es: {nivelAgua} y este es bajo')
elif (nivelAgua>=20 and nivelAgua<400):
    #salidas
    print (f'El Nivel de agua es: {nivelAgua} y este es optimo')
elif (nivelAgua>=400):
    #salidas
    print (f'El Nivel de agua es: {nivelAgua} Se van a morir los de caucacia')
else:
    #salidas
    print (f'El Nivel de agua no es valido')
    
#salidas