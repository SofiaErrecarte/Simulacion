import random 
import math 
import matplotlib.pyplot as plt
from scipy.stats import chi2
import statistics as stats
import numpy as np
import collections

#Valores para probar:
#middle_square: seed=1931 n=10 -> [3728761, 53100369, 1006009, 3600, 1296, 144, 1, 0, 0]
#gcl: seed=5 a=7 c=9 mod=11 -> [0, 9, 6, 7, 3, 8, 10, 2, 1, 5]
#     seed=7 a=1 c=7 mod=13 ->[1, 8, 2, 9, 3, 10, 4, 11, 5, 12, 6, 0, 7] 

def menu():
    print("Menu: 0 para salir")
    print("1 - Middle Square") 
    print("2 - Generador Congruencial")
    print("3 - Generador de Python")
    rta = int(input("Ingrese la opcion elegida: "))
    return rta

def menu2():
    print("Pruebas de aleatoriedad:")
    print("1- Kolmogorov Smirnov")
    print("2- Chi-cuadrado")
    print("3- Pruebas de Series")
    print("4- Prueba de Huecos")
    rta2=int(input("Ingrese opcion deseada: "))
    return rta2

def middle_square ():   
    semillas=[]
    numeros=[]
    t=1
    seed= int(input("Ingrese una semilla de 4 numeros: "))
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
    
    
    numeros2=[]
    print(n)
    maximo=max(numeros)
    for i in range(0, n-1):
        numeros2.append(numeros[i]/maximo)
    #print(numeros2)
    x1 = range(0, n-1)
    #plt.plot(x1, numeros2, label="MS - seed={0}, n={1}" .format(seed_ini, n))
    plt.scatter(numeros2, numeros2, label="MS - seed={0}, n={1}" .format(seed_ini, n))
    plt.legend(loc="lower right")
    #plt.xlabel('Período')
    plt.xlabel('N° Pseudoaleatorios')
    plt.ylabel('N° Pseudoaleatorios')
    plt.title('Generadores de N° Pseudoaleatorios - Middle Square')
    #plt.show()  

    return numeros2

def prueba_series(numeros):
    print("\nDatos de la prueba de Series ")
    long = len(numeros)
    numerosAux2=numeros
    #print(numerosAux2)
    k = 10   #va a haber 10 rangos
    print('Cantidad de rangos: ', k)

    # Crear el array bidimensional de las celdas con sus frecuencias
    freqs =  [[0 for i in range(k)] for i in range(k)]
    frec_intervalos=[]
    # Para cada par de rangos (i,j)
    for i in range(1, k + 1):
        maxI = i / k
        minI = maxI - (1 / k)
        for j in range(1, k + 1):
            maxJ = j / k
            minJ = maxJ - (1 / k)
            for n in range(0,(long-1)):
                if numerosAux2[n] < maxI and numerosAux2[n] >= minI and numerosAux2[(n+1)] < maxJ and numerosAux2[(n+1)] >= minJ:
                    # Si el primer elemento esta en el rango i, y el segundo en el j,
                    # sumamos 1 a la frecuencia de esos rangos
                    freqs[i - 1][j - 1] += 1

    
    frec_esperada= (long-1)/k
    #print('Frecuencia esperada', frec_esperada)
    for i in range(0,k):
        cont = 0
        for j in range(0,k):
            cont = cont +  freqs[i][j]
        frec_intervalos.append(cont)
    #print("Frecuencia observada en cada intervalo: ",frec_intervalos)

    # χ2 = k/n * Σ(fj - n/k)^2
    acum=0
    for i in frec_intervalos:
        acum+= (i - frec_esperada) ** 2
    
    chi2calc= acum * (1/ frec_esperada)
    chi_tabla=chi2.isf(0.05, k - 1)
    print('{0} < {1}'.format(chi2calc, chi_tabla))
    if (chi2calc < chi_tabla):
        print('Los numeros son independientes según la prueba de Series.\n')
    else:
        print('Los números no son independientes según la prueba de Series.\n')
    #print(numerosAux2)
    
    x1 = range(0, k)
    plt.plot(x1, [frec_esperada for i in x1], label="FR Esperada")
    plt.scatter(x1, frec_intervalos, color='red', label="FR Observada")
    plt.legend(loc="upper right")
    plt.xlabel('Período')
    plt.ylabel('Frecuencia Absoluta')
    plt.title('GCL seed=5, a=2, c=3, m=997 - Prueba de Series')
    plt.show()

def chiCuadrado(numeros):   
    print("\nDatos de la prueba Chi-Cuadrado")
    n=len(numeros)                        
    numerosAux3=numeros
    #print(numerosAux3)
    k=10 #hacemos 10 rangos siempre 
    print('Cantidad de rangos: ', k)
    #Calculamos frecuencias absolutas
    
    freqs = [0 for i in range(k)]
    #Para cada rango
    for i in range(1,k+1):
        max = i/k
        min = max - (1/k)
        for xi in numerosAux3:
            if xi < max and xi >= min:
                #Si el numero esta en el rango, sumamos 1 a la frecuencia de ese rango
                freqs[i-1]+=1
    #print('frecuencias: ',freqs)
    
    Ei=n/k #totalDatos/totalIntervalos
    print('F esperada:', Ei)
    #χ2 = 1/Ei * Σ(Oi - Ei)^2
    chi2calc = (1/Ei) * sum ( [ (Oi-(Ei)) **2 for Oi in freqs ] )
    #print('chi: ', chi2calc)
    
    #alfa=0.05 95% grados de libertad=k-1
    chi_tabla=chi2.isf(0.05, k - 1)
    print('{0} < {1}'.format(chi2calc, chi_tabla))
    if (chi2calc<chi_tabla): print('La hipótesis nula es aceptada. La distribución es uniforme según prueba de Chi-Cuadrado\n')
    else: print('La hipótesis nula no es aceptada. La distribución no es uniforme según prueba de Chi-Cuadrado\n')
    #print(numerosAux3)
    x1 = range(0, k)
    plt.plot(x1, [Ei for i in x1], label="FR Esperada")
    plt.scatter(x1, freqs, color='red', label="FR Observada")
    plt.legend(loc="upper right")
    plt.xlabel('Período')
    plt.ylabel('Frecuencia Absoluta')
    plt.title('GCL seed=5, a=2, c=3, m=997 - Prueba de Chi-Cuadrado')
    plt.show()

def espera(numeros):     
    print("\nDatos de la prueba de Huecos ")
    numerosAux4=numeros
    #print(numerosAux4)
    _i = 0 # extremo inferior subintervalo, >= 0
    _s = 0.5 # extremo superior subintervalo, <= 1
    _psi = _s - _i # calculo probabilidad del subintervalo
    
    # cálculo de posiciones donde hay números perteneciente al subintervalo seleccionado
    _pos = []
    for i in numerosAux4:
        if (i >= _i and i < _s):
            _pos.append(1)
        else:
            _pos.append(0)
    #print(_pos)

    # cálculo de la longitud de cada hueco
    _tesp = []
    _c = 0
    for i in _pos:
        if i==1:
            _tesp.append(_c) #cada vez que vuelve a haber un 1 agrega el contador que fue contando los 0
            _c = 0 #siempre se vuelve a reiniciar en 0
        else: #i==0
            _c += 1
    #print(_tesp)

    _ch = max(_tesp) #+ 1 # cantidad de huecos
    if (_ch > 15): #definimos un tama;o de hueco max, en este caso 10, siempre que haya uno > a 10 se considera que es tama;o 10
        _ch = 15
    #print(_ch)

    # cálculo de la frecuencia observada
    _fO = []
    for i in range(_ch):
        if (i == 15): #9
            _fO.append(sum(n >= 15 for n in _tesp))
        else:
            _fO.append(_tesp.count(i))
    #print(_fO)

    # cálculo de la frecuencia esperada
    _fE = []
    for i in range(_ch):
        _fE.append((1 - _psi)**i * _psi * sum(_fO))

    # cálculo del estadístico
    chi2calc = 0
    for i in range(_ch):
        chi2calc += (_fO[i] - _fE[i])**2 / _fE[i]
    print(chi2calc)

    chi_tabla=chi2.isf(0.05, _ch - 1)
    if (chi2calc<chi_tabla): 
        print('{0} < {1}'.format(chi2calc,chi_tabla))
        print('La hipótesis nula es aceptada. Los números son independientes según prueba de Huecos\n')
    else: print('La hipótesis nula no es aceptada. Los números no son independientes según prueba de Huecos\n')
    #print(numerosAux4)
    x1 = range(0, _ch)
    plt.plot(x1, _fE, label="FR Esperada")
    plt.scatter(x1, _fO, color='red', label="FR Observada")
    plt.legend(loc="upper right")
    plt.xlabel('Período')
    plt.ylabel('Frecuencia Absoluta')
    plt.title('GCL seed=5, a=2, c=3, m=997- Prueba de Huecos')
    plt.show()

def prueba_ks(numeros):
    print("\nDatos de la prueba Kolmogorov-Smirnov")
    n=len(numeros)
    numerosAux1=[]
    numerosAux1=numeros
    numerosAux1.sort()
    #print(numerosAux1)
    if n<50: 
        d_ks= float(input("Ingrese el valor de la tabla:")) #tengo que ingresar el valor de la tabla
    else:  
        d_ks=1.36/math.sqrt(n) #grado de confianza de 95%-- valor sacado de la tabla
    
    d_mas = []
    #D +
    for i in range(1,n):  #aca por q no hace de 0 a n?
        valor=(i/n)-numerosAux1[i-1]
        d_mas.append(valor)
    #D -
    d_menos=[]
    for i in range (1,n):
        valor=numerosAux1[i-1]-(((i-1)-1)/n)
        d_menos.append(valor)

    d1= max([num for num in d_mas]) #busco los numeros mayores de cada lista d 
    print("D+:",d1)
    d2= max([num for num in d_menos])
    print("D-:",d2)

    if d1>d2: d=d1 
    else: d=d2
    print("D = {}".format(d))
    print('{0} < {1}'.format(d, d_ks))
    if d>d_ks: print("No sigue una distribucion uniforme según la prueba Kolmogorov Smirnov\n")
    else : print("Sigue una distribucion uniforme según la prueba Kolmogorov Smirnov\n")
    #print(numerosAux1)

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
    
        #directamente divido acá asi ya paso el arreglo entre 0 y 1
    n=len(numeros)
    maximo=max(numeros)
    for i in range(0,n):
        numeros[i] = (numeros[i]/maximo)
    #print(numeros)
    if(periodo == mod): print("El periodo es completo: ", periodo)
    else: print("El periodo es incompleto:", periodo)

    
    chiCuadrado(numeros)
    prueba_series(numeros)
    espera(numeros)
    prueba_ks(numeros)
    #grafico general
    x1 = range(0, periodo)
    plt.ylabel('N° Pseudoaleatorios')
    plt.title('Generadores de N° Pseudoaleatorios - GCL')
    #plt.plot(x1, numeros, label="GCL - seed={0}, a={1}, c={2}, m={3}" .format(bandera, a, c, mod))
    plt.scatter(numeros, numeros, label="GCL - seed={0}, a={1}, c={2}, m={3}" .format(bandera, a, c, mod))
    #plt.legend(loc="upper right")
    plt.legend(loc="lower right")
    #plt.xlabel('Período')
    plt.xlabel('N° Pseudoaleatorios')
    plt.show()
    covar=np.cov(numeros)
    print(covar)
    
    return numeros
    
def random_python(numeros):
    n=len(numeros)
    sem=int(input('Ingrese la semilla: '))
    random.seed(sem)
    for i in range(0, n):
        numeros[i]= (random.random())
    #print(numeros)
    
    x1 = range(0, n)
    plt.plot(x1, numeros, label="PY - seed={0}, n={1}" .format(sem,n+1))
    plt.legend(loc="upper right")
    plt.xlabel('Período')
    plt.ylabel('N° Pseudoaleatorios')
    plt.title('Generadores de N° Pseudoaleatorios - Generador Python')

    return numeros

print('Bienvenido al generador de números pseudoaleatorios')
seguir=int(input("1 ejecutar, 0 salir: "))
numeros=[]
while seguir==1:
    rta = menu()
    if rta == 1: numeros=middle_square()
    elif rta == 2: numeros=gcl()
    elif rta == 3: numeros=random_python(numeros)
    
    #pruebas p todos los generadores
    continuar=1
    while continuar==1:
        rta2= menu2()
        if(rta2==1): prueba_ks(numeros)
        elif (rta2==2): chiCuadrado(numeros)
        elif (rta2==3): prueba_series(numeros)
        elif (rta2==4): espera(numeros)
        continuar=int(input('Realizar otra prueba: 1 SI // 0 NO : '))
    
    seguir = int(input("1 ejecutar, 0 salir: "))
#plt.title('Generadores de N° Pseudoaleatorios - GCL vs Middle Square')
plt.show()
