import random 
import math 
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy.stats import norm
import statistics as stats
from scipy.stats import chisquare
import numpy as np
import collections
n=100

def menu():
    print("Menu: 0 para salir")
    print("1 - Exponencial") 
    print("2 - Uniforme")
    print("3 - Gamma")
    print("4 - Normal")
    print("5 - Pascal")
    print("6 - Binomial")
    print("7 - Hipergeométrica")
    print("8 - Poisson")
    print("9 - Empírica")
    rta = int(input("Ingrese la opcion elegida: "))
    return rta

#PRUEBAS
def chiCuadrado(numeros):   
    print("\nDatos de la prueba Chi-Cuadrado")
    n=len(numeros)                        
    numerosAux3=numeros
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
    Ei=n/k #totalDatos/totalIntervalos
    chi2calc = (1/Ei) * sum ( [ (Oi-(Ei)) **2 for Oi in freqs ] )
    chi_tabla=chi2.isf(0.01, k - 1)
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
    plt.title('Prueba de Chi-Cuadrado')
    plt.show()

def exponencial(esp):   #ver bien formula
    r = random.random()
    x = (-esp * math.log(r))
    return x

def uniforme(esp, var):
    a = 0
    b = 0
    a= esp-math.sqrt(3*var)
    b=2*esp - a
    r=random.random()
    x= a+((b-a)* r)
    return x  

def gamma(esp, var) :
    k=10 #lo definimos para q sea un numero entero
    alpha= esp/var
    tr=1
    for i in range(0, k):
        r=random.random()
        tr=tr*r
    x = (-(math.log(tr)) /alpha)
    return x

def normal(esp, var): 
    k=30
    suma=0
    for j in range(0, k): 
        r=random.random()
        suma=suma+r
    x=math.sqrt(var) * ((12/k)**(1/2)) * (suma-(k/2)) + esp
    return x

def pascal(esp, var):
    k=round(esp**2/(var-esp))
    p=esp/var
    q=1-p
    tr=1
    for i in range(0,k):
        r=random.random()
        tr=tr*r
    x=math.log10(tr)/math.log10(q)
    return round(x)

def binomial(esp, var):
    x = 0
    p = (esp-var)/esp
    n = round((esp**2) / (esp-var))
    print(n)
    for i in range(0, n):
        r=random.random()
        if ( (r-p)<0 ):
            x = x + 1
    return x

def hipergeometrica():#recordar acá que la esp =np y var= npq(N-n/N-1)
    N=50   
    n=10
    p=0.5  # desp ver cual poner
    s=0
    x=0
    for i in range(0, n):
        r = random.random()
        if ((r-p) < 0):
            s = 1
            x = x+1
        else: s = 0
        p=(N*p-s)/(N-1)
        N=N-1
    return x

def poisson ():
    p = 0.5 #ver desp cual poner
    x=0
    tr=1
    b = math.exp(-p)
    r=random.random()
    tr=tr*r
    while((tr-b) >=0):
        x = x+1
        r=random.random()
        tr=tr*r
    return x

def empirica():
    probabilidades=[0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062,0.151, 0.047, 0.044] # esp = 
    x=0
    r=random.random()
    for i in range(0, len(probabilidades)):
        if(r<=probabilidades[i] and r>probabilidades[i+1]):
            x=i+1 #cat 1, 2, 3,...,10
    return x


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

#esp = 0.7  #para CONTINUAS
#var = 0.05
esp=30 #para DISCRETAS
var=5
rta = menu()
while rta != 0:
    if (rta == 1):        
        numeros=[]
        for i in range(0, n): 
            x = exponencial(esp)
            numeros.append(x)
        print(numeros)
        print(np.mean(numeros))
        chiCuadrado(numeros)
        print(chisquare(numeros))
    elif (rta== 2):
        numeros=[]
        for i in range(0, n): 
            x = uniforme(esp, var)
            numeros.append(x)
        print(numeros)
        print(np.mean(numeros))
        chiCuadrado(numeros)
        prueba_ks(numeros)
    elif (rta==3): 
        numeros=[]
        for i in range(0, n): 
            x = gamma(esp, var)
            numeros.append(x)
        print(numeros)
        print(np.mean(numeros))
    elif (rta==4):
        numeros=[]
        for i in range(0, n): 
            x = normal(esp, var)
            numeros.append(x)
        print(numeros)
        print(np.mean(numeros))
    elif (rta==5): 
        numeros=[]
        for i in range(0, n):
            esp1=3
            var1=4
            x = pascal(esp1, var1)
            numeros.append(x)
        print(numeros)
        print(np.mean(numeros))
    elif (rta==6):
        numeros=[]
        for i in range(0, n): 
            x = binomial(esp, var)
            numeros.append(x)
        print(numeros)
        print(np.mean(numeros))
    elif (rta==7):
        numeros=[]
        for i in range(0, n): 
            x = hipergeometrica()
            numeros.append(x)
        print(numeros)
        print(np.mean(numeros))
    elif (rta==8):
        numeros=[]
        for i in range(0, n): 
            x = poisson
            numeros.append(x)
        print(numeros)
        print(np.mean(numeros))
    elif (rta==9):
        numeros=[]
        for i in range(0, n): 
            x = empirica()
            numeros.append(x)
        print(numeros)
        print(np.mean(numeros))
    rta = menu()

#menu discretas o continuas
#menu pruebas
