import random 
import math 
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy.stats import norm
import statistics as stats
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
def dif_esperanzas(esperanzas, var, esp):
    for i in range(0, len(esperanzas)):
        resta= abs(esperanzas[i] - esp)
        print("esp ", esp)
        print("resta ",resta)
        print("var", var)
        if (resta<=var):
            print("OK")
        else: print("NO")
            
#DISTRIBUCIONES
def exponencial(esp):   
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
    for i in range(0, n):
        r=random.random()
        if ( (r-p)<0 ):
            x = x + 1
    return x

def hipergeometrica():
    N=50   
    n=10
    p=0.5  # desp ver cual poner
    q=1-0.5
    s, x= 0, 0
    esp_hiper=n*p  #esp y var esperadas
    var_hiper=n*p*(1-p)*((N-n)/(N-1))
    for i in range(0, n):
        r = random.random()
        if ((r-p) < 0):
            s = 1
            x = x+1
        else: s = 0
        p=(N*p-s)/(N-1)
        N=N-1
    return x, var_hiper, esp_hiper

def poisson():
    p = 0.5 #es muy grande creo
    x=0
    tr=1
    b = math.exp(-p)
    r=random.random()
    tr=tr*r
    while((tr-b) >=0):
        x = x+1
        r=random.random()
        tr=tr*r
    return x, p

def empirica():
    probabilidades=[0.2, 0.1, 0.3, 0.05, 0.05, 0.2, 0.1]
    probabilidades_acum=[]
    probabilidades_acum.append(probabilidades[0])
    acum=probabilidades[0]
    #esp_emp=sum(probabilidades[i]*(i+1) for i in range(0, len(probabilidades))) #esperanza esperada
    for i in range(1, len(probabilidades)):
        acum=acum+probabilidades[i]
        probabilidades_acum.append(acum)
    #print(probabilidades)
    #print(probabilidades_acum)
    r=random.random()
    #print("random:",r)
    if(r<=probabilidades_acum[0]): x=1 #(0+1)
    else:
        for i in range(1, len(probabilidades)):
            if(r>probabilidades_acum[i-1] and r<=probabilidades_acum[i]):
                x=i+1 #cat 1, 2, 3,...,7       
    #print("categoria: ", x)    
    return x

#esp = 0.7  #para CONTINUAS
#var = 0.05
esp=30 #para DISCRETAS
var=5
desv= math.sqrt(var)
repes=2 #define cuantas esperanzas comparamos
rta = menu()
while rta != 0:
    if (rta == 1):        
        numeros=[]
        esperanzas=[]
        for j in range(0,repes):
            for i in range(0, n):
                x = exponencial(esp)
                numeros.append(x)
            print(numeros)
            esp1=np.mean(numeros)
            print(esp1)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas, var, esp)

    elif (rta== 2):
        numeros=[]
        esperanzas=[]
        for j in range(0, repes):
            for i in range(0, n):
                x = uniforme(esp, var)
                numeros.append(x)
            print(numeros)
            esp1 = np.mean(numeros)
            print(esp1)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas,var, esp)
    elif (rta==3):
        numeros=[]
        esperanzas=[]
        for j in range(0, repes):
            for i in range(0, n):
                x = gamma(esp, var)
                numeros.append(x)
            print(numeros)
            esp1 = np.mean(numeros)
            print(esp1)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas, var, esp)

    elif (rta==4):
        numeros=[]
        for j in range(0, repes):
            for i in range(0, n):
                x = normal(esp, var)
                numeros.append(x)
            print(numeros)
            esp1 = np.mean(numeros)
            print(esp1)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas, var, esp)
    elif (rta==5):
        numeros=[]
        esperanzas=[]
        for j in range(0, repes):
            for i in range(0, n):
                esp1=3
                var1=4
                x = pascal(esp1, var1)
                numeros.append(x)
            print(numeros)
            esp2 = np.mean(numeros)
            print(esp2)
            esperanzas.append(esp2)
        dif_esperanzas(esperanzas, var1, esp1)
    elif (rta==6):
        numeros=[]
        esperanzas = []
        for j in range(0, repes):
            for i in range(0, n):
                x = binomial(esp, var)
                numeros.append(x)
            print(numeros)
            esp1 = np.mean(numeros)
            print(esp1)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas, var, esp)
    elif (rta==7):
        numeros=[]
        esperanzas = []
        for j in range(0, repes):
            for i in range(0, n):
                x , var= hipergeometrica()
                numeros.append(x)
            print(numeros)
            esp1 = np.mean(numeros)
            print(esp1)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas, var,esp)
    elif (rta==8):
        numeros=[]
        esperanzas=[]
        for j in range(0, repes):
            for i in range(0, n): 
                    x = poisson()
                    numeros.append(x)
             print(numeros)
             esp1=np.mean(numeros)
             print(esp1)
             esperanzas.append(esp1)
        dif_esperanzas(esperanzas,lbda)


    elif (rta==9):
        numeros=[]
        for i in range(0, n): 
            x = empirica()
            numeros.append(x)
        print(numeros)
        print(np.mean(numeros))
    rta = menu()
