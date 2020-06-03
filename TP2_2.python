import random 
import math 
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy.stats import norm
import statistics as stats
import numpy as np
import collections
n=1000

def menu():
    print("Menu: 0 para salir")
    print("1 - Exponencial") 
    print("2 - Uniforme")
    print("3 - Gamma")
    print("4 - Normal")
    rta = int(input("Ingrese la opcion elegida: "))
    return rta


def exponencial(numeros, esp):
    num_exp=[]
    for i in range(0,n):
        x = (-esp * math.log(numeros[i]))
        #print("x", x)
        num_exp.append(x)
    #print ("numeros generados dep de transf", num_exp)
    #x1 = range(0,n)
    plt.plot(num_exp)
    plt.show()

def uniforme(numeros, esp, var):
    a = 0
    b = 0
    num_unif=[]
    a= esp-math.sqrt(3*var)
    b=2*esp - a
    for i in range(0,n):
        x= a+((b-a)* numeros[i])
        num_unif.append(x)
    plt.plot(num_unif)
    plt.show()   

def gamma(numeros, esp, var) :
    #k=esp**2/var
    k=10
    alpha= esp/var
    num_gamma=[]
    for j in range(0, n):
        tr=1
        for i in range(1, k):
            tr=tr*numeros[j]
        x = (-(math.log(tr)) /alpha)
        num_gamma.append(x)
    plt.plot(num_gamma)
    plt.show()  

def normal(numeros, esp, var): 
    num_normal=[]
    num_normalfunc=[]
    k=30
    
    for i in range(0, n):
        sum=0
        for j in range(0, k): #me parece que tiene que ir generando una secuencia de longitud k de r numeros para cada x por lo que dice en la pag 112, quizás en la gamma sea lo mismo. de todos modos no entiendo por qué recibe esp y var aunque bueno, como siempre es el generador de python la distribuion de lo random siempre va a ser uniforme con =esp y var me parece, igual ni entiendo el graf q tira
            r=random.random()
            sum=sum+r
        y=norm.ppf(numeros[i], loc=esp, scale=var) # la puse para probar pero no estan bien los parametros, no entiendo q poronga hace eso q suma en la formula del libro
        x=math.sqrt(var) * ((12/k)**(1/2)) * (sum-k/2) + esp
        num_normal.append(x)
        num_normalfunc.append(y)
    plt.plot(num_normal)
    plt.show()
    plt.plot(num_normalfunc)
    plt.show()


numeros = []
for i in range (0,n):
    numeros.append(random.random())
#print("numeros random",numeros)

var=np.var(numeros)

esp=0
#frec = []
#for i in range(0,n+1):
    #esp = esp + (numeros[i] * numeros.count(numeros[i])/n)
esp=np.mean(numeros)
print("Esperanza", esp)

rta = menu()
while rta != 0:
    if (rta == 1): exponencial(numeros,esp) 
    elif (rta== 2): uniforme(numeros,esp,var)
    elif (rta==3): gamma(numeros, esp, var)
    elif (rta==4): normal(numeros, esp, var)
    rta = menu()
