import random 
import math 
import matplotlib.pyplot as plt
import statistics as stats
import collections

#Valores para probar:
#middle_square: seed=1931 n=10 -> [3728761, 53100369, 1006009, 3600, 1296, 144, 1, 0, 0]
#gcl: seed=5 a=7 c=9 mod=11 -> [0, 9, 6, 7, 3, 8, 10, 2, 1, 5]
#     seed=7 a=1 c=7 mod=13 ->[1, 8, 2, 9, 3, 10, 4, 11, 5, 12, 6, 0, 7] 
#     seed=5 a=7 c=1 mod=97

def menu():
    print("Menu: 0 para salir")
    print("1 - Middle Square") 
    print("2 - Generador Congruencial")
    rta = int(input("Ingrese la opcion elegida: "))
    return rta

def middle_square ():   
    semillas=[]
    numeros=[]
    t=1
    seed= int(input("Ingrese una semillad de 4 numeros: "))
    n= int(input("Ingrese cantidad de repeticiones: "))
    seed_ini=seed
    for i in range(1, n):   
        s=[]
        x = seed * seed
        numeros.append(x)
        dig_x= len(str(numeros[t-1]))
        if dig_x != 8:
            new_seed = str(x).zfill(8) #valor de 8 digitos para generar la nueva semilla
        else: new_seed=str(x)
        x_list=list(new_seed) #convierto a lista para extraer despues las posiciones q necesito
        for i in range(2,6): #0 1 2 3 4 5 6 7 8 - necesito las posiciones 2 3 4 5
            s+=x_list[i]
        seed = int(''.join(s)) #paso lista a numero
        semillas.append(seed) 
    print(numeros,semillas)
    x1 = range(1, n)
    plt.plot(x1, numeros, label="seed={0}, n={1}" .format(seed_ini, n))


def chiCuadrado(numeros):
    n=len(numeros)
    k=10 #hacemos 10 rangos siempre
    #divido todos por la longitud del arreglo
    for i in range(0,n):
        numeros[i]=numeros[i]/n
    print(numeros)
    #Calculamos frecuencias absolutas
    freqs = [0 for i in range(k)]
    
    #Para cada rango
    for i in range(1,k+1):
        max = i/k
        min = max - (1/k)
        for xi in numeros:
            if xi < max and xi >= min:
                #Si el numero esta en el rango, sumamos 1 a la frecuencia de ese rango
                freqs[i-1]+=1
    print('frecuencias: ',freqs)
    
    Ei=n/k #totalDatos/totalIntervalos
    #χ2 = 1/Ei * Σ(Oi - Ei)^2
    chi2 = (1/Ei) * sum ( [ (Oi-(Ei)) **2 for Oi in freqs ] )
    print('chi: ', chi2)
    
    chi_tabla=16.92 #no encuentro en ningun lado como calcularlo sin tabla
    if (chi2<chi_tabla): print('La hipótesis nula es aceptada. La distribución es uniforme')
    else: print('La hipótesis nula no es aceptada. La distribución no es uniforme')


def gcl():  
    x = int(input("Introduce el valor de la semilla: "))
    a = int(input("Introduce el valor del multiplicador a: "))
    c = int(input("Introduce el valor de la constante aditiva c: "))
    mod = int(input("Introduce el valor del modulo m: "))
    periodo = 0
    bandera = 0
    numeros = []
    while(bandera != x): #el codigo se ejecuta hasta que vuelve a generarse la semilla inicialmente ingresada
        if (periodo == 0): #en la primer vuelta asigno que la bandera será x(la semilla ingresada). no puedo asignarlo antes del while porque de ese modo nunca entraria
            bandera = x
        x = (a * x + c) % mod #calculo nueva semilla
        numeros.append(x)
        periodo = periodo + 1 #voy contando las vueltas

    print(numeros)
    x1 = range(0, periodo)
    plt.plot(x1, numeros, label="seed={0}, a={1}, c={2}, mod={3}" .format(bandera, a, c, mod))
    if(periodo == mod): print("El periodo es completo: ", periodo)
    else: print("El periodo es incompleto:", periodo)
    chiCuadrado(numeros)


print('Bienvenido al generador de números pseudoaleatorios')
seguir=int(input("1 ejecutar, 0 salir: "))
while seguir==1:
    rta = menu()
    if rta == 1: middle_square()
    elif rta == 2: gcl()
    seguir = int(input("1 ejecutar, 0 salir: "))
plt.legend(loc="upper right")
plt.xlabel('Período')
plt.ylabel('N° Pseudoaleatorios')
plt.title('Generadores de N° Pseudoaleatorios')
#plt.show()