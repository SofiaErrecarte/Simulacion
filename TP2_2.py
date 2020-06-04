import random 
import math 
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy.stats import norm
import statistics as stats
import numpy as np
import collections
n=10

def menu():
    print("Menu: 0 para salir")
    print("1 - Exponencial") 
    print("2 - Uniforme")
    print("3 - Gamma")
    print("4 - Normal")
    rta = int(input("Ingrese la opcion elegida: "))
    return rta


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
    k=30
    p=esp/var
    q=1-p
    tr=1
    for i in range(0,k):
        r=random.random()
        tr=tr*r
    x=math.log10(tr)/math.log10(q)  ##ver bien si es log o ln
    return x

def binomial(esp, var):
    x = 0
    n=30
    p = (esp-var)/esp
    n = (esp**2) / (esp-var)
    for i in range(0, n):
        r=random.random()
        if ( (r-p)<0 ):
            x = x + 1
    return x

def hipergeometrica():
    N=50   
    n=10
    p=0.5  #desp ver cual poner
    x=0
    for i in range(0, n):
        r = random.random()
        if ((r-p) < 0):
            s = 1
            x = x+1
        else s=0
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
    probabilidades=[0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062,0.151, 0.047, 0.044]
    r=random.random()
    for i in range(0, len(probabilidades)):
        if(r<=probabilidades[i]):
            x=i+1 #cat 1, 2, 3,...,10
    return x


esp = 30 #cambiar q ingrese user
var = 5
rta = menu()
while rta != 0:
    if (rta == 1): x = exponencial(esp) 
    elif (rta== 2): x = uniforme(esp,var)
    elif (rta==3): x = gamma(esp, var)
    elif (rta==4): x = normal(esp, var)
    elif (rta==5): x = pascal(esp, var)
    elif (rta==6): x = binomial(esp, var)
    elif (rta==7): x = hipergeometrica()
    rta = menu()

#menu discretas o continuas
#menu pruebas
