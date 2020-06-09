import random 
import math 
import matplotlib.pyplot as plt
from scipy.stats import chi2, norm, binom, poisson, expon, uniform
import statistics as stats
import numpy as np
import collections
n=2500

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
    print("Esperanza esperada: ", esp)
    print("Varianza esperada: ", var)
    for i in range(0, len(esperanzas)):
        resta= abs(esperanzas[i] - esp)
        print("Diferencia entre E.Esperada y E.calculada: ",resta)
        if (resta<=var):
            print("El conjunto generador pasa la prueba de Diferencia de Esperanzas.")
        else: print("NO")

def grafico_normal(et, st, esperanzas, desvios):
    plt.subplot(211)
    x = np.linspace(norm.ppf(0.01, et, st), norm.ppf(0.99, et, st), 100)
    for i in range(0, len(esperanzas)):
        plt.plot(x, norm.pdf(x, esperanzas[i], desvios[i]), label = 'Observada {0}'.format(i+1), alpha=0.5)
    plt.plot(x, norm.pdf(x, et, st), 'r', label = 'Esperada')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Distribución Normal')
    plt.legend()
    plt.show()
    
def grafico_binomial(param_n, param_p, n, p):
    plt.subplot(211)
    x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
    fmp = binom.pmf(x, n, p) # Función de Masa de Probabilidad Esperada
    for i in range(0, len(param_n)):
        x_1 = np.arange(binom.ppf(0.01, param_n[i], param_p[i]), binom.ppf(0.99, param_n[i], param_p[i]))
        fmp_1 = binom.pmf(x_1, param_n[i], param_p[i]) # Función de Masa de Probabilidad Observada
        plt.plot(x_1, fmp_1, label="Observada {0}".format(i+1), alpha=0.5)
        plt.vlines(x_1, 0, fmp_1, lw=5, alpha=0.5)
    plt.plot(x, fmp, label="Esperada", color='r')
    plt.vlines(x, 0, fmp, lw=5, alpha=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Distribución Binomial')
    plt.legend()

def grafico_poisson(esperanzas, lbda):
    plt.subplot(223)
    p1 = poisson(lbda) # Distribución lambda esperado
    x = np.arange(p1.ppf(0.01), p1.ppf(0.99))
    fmp = p1.pmf(x) # Función de Masa de Probabilidad
    plt.plot(x, fmp, '--', color='r', label="Esperada")
    plt.vlines(x, 0, fmp, lw=5, alpha=0.5)
    for i in range(0, len(esperanzas)):
        p2 = poisson(lbda) # Distribución lambda observado
        x = np.arange(p2.ppf(0.01), p2.ppf(0.99))
        fmp = p2.pmf(x) # Función de Masa de Probabilidad
        plt.plot(x, fmp, '--', label="Observada {0}".format(i+1), alpha=0.5)
        plt.vlines(x, 0, fmp, lw=5, alpha=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Distribución de Poisson')
    plt.legend(loc="upper right")

def grafico_exp(esperanzas, esp):
    plt.subplot(223)
    loc=0
    xvalues = np.linspace(expon.ppf(0.01, loc, esp), expon.ppf(0.99, loc, esp), 100)
    cdf = expon.cdf(xvalues, loc, esp)
    plt.plot(xvalues, cdf, color='r', label="Esperada")
    for i in range(0, len(esperanzas)):
        xvalues = np.linspace(expon.ppf(0.01, loc, esperanzas[i]), expon.ppf(0.99, loc, esperanzas[i]), 100)
        cdf = expon.cdf(xvalues, loc, esperanzas[i])
        plt.plot(xvalues, cdf, label="Observada {0}".format(i+1), alpha=0.5)
    plt.title("Distribución Exponencial")
    plt.ylabel('f(x)')
    plt.xlabel('X')
    plt.legend()
    

def grafico_uniforme(a, b, param_a, param_b):
    plt.subplot(224)
    uniforme = uniform(a, b)
    x = np.linspace(uniforme.ppf(0.01), uniforme.ppf(0.99), 100)
    fp = uniforme.pdf(x) # Función de Probabilidad
    plt.plot(x, fp, label="Esperada", color="r")
    plt.vlines(x, 0, fp, lw=5, color='r')
    for i in range(0, len(param_a)):
        uniforme = uniform(param_a[i], param_b[i])
        x = np.linspace(uniforme.ppf(0.01), uniforme.ppf(0.99), 100)
        fp = uniforme.pdf(x) # Función de Probabilidad
        plt.plot(x, fp, label="Observada {0}".format(i+1), alpha=0.5)
        plt.vlines(x, 0, fp, lw=5, alpha=0.5, color='')
    plt.ylim(0, 1.2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Distribución Uniforme')
    plt.legend()
    

def grafico_empirica(numeros, probabilidades):
    plt.subplot(224)
    cat=list(range(1,len(probabilidades)+1))
    freq_absoluta=[]
    freq_relativa=[]
    freq_absoulta = collections.Counter(numeros)
    freq_relativa = {k: v / len(numeros) for k, v in freq_absoulta.items()}
    plt.bar(cat, probabilidades, color="r", label="Esperada")
    plt.bar(freq_relativa.keys(), freq_relativa.values(), alpha=0.5, label="Observada")
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Distribución Empírica')
    plt.legend()
    plt.show()

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
    return x, a, b  

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
    return x, n, p

def hipergeometrica():
    N=50   
    n=10
    p=0.5  
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

def poissonD():
    p = 6 
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
    probabilidades_acum, acum=[], probabilidades[0]
    probabilidades_acum.append(probabilidades[0])
    esp_emp=sum(probabilidades[i]*(i+1) for i in range(0, len(probabilidades))) #esperanza esperada
    var_emp=sum( ( ( (i+1) - esp_emp)**2 )*probabilidades[i] for i in range(0, len(probabilidades)))
    for i in range(1, len(probabilidades)):
        acum=acum+probabilidades[i]
        probabilidades_acum.append(acum)
    r=random.random()
    if(r<=probabilidades_acum[0]): x=1 #(0+1)
    else:
        for i in range(1, len(probabilidades)):
            if(r>probabilidades_acum[i-1] and r<=probabilidades_acum[i]): x=i+1 #cat 1, 2, 3,...,7    
    return x, esp_emp, var_emp, probabilidades

espC = 0.7  #para CONTINUAS
varC = 0.05
desvC=math.sqrt(varC)
espD=30 #para DISCRETAS
varD=5
desvD= math.sqrt(varD)

repes=5 #define cuantas corridas comparamos
rta = menu()
while rta != 0:
    
    if (rta == 1):        
        numeros=[]
        esperanzas=[]
        for j in range(0,repes):
            numeros=[]
            for i in range(0, n):
                x = exponencial(espC)
                numeros.append(x)
            esp1=np.mean(numeros)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas, varC, espC)
        grafico_exp(esperanzas, espC)
        

    elif (rta== 2):
        numeros=[]
        esperanzas=[]
        param_a=[]
        param_b=[]
        for j in range(0, repes):
            numeros=[]
            for i in range(0, n):
                x, a, b = uniforme(espC, varC)
                numeros.append(x)
            esp1 = np.mean(numeros)
            var1 = np.var(numeros)
            a1= esp1-math.sqrt(3*var1)
            b1=2*esp1 - a1
            param_a.append(a1)
            param_b.append(b1)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas,varC, espC)
        grafico_uniforme(a, b, param_a, param_b)

    elif (rta==3):
        numeros=[]
        esperanzas=[]
        for j in range(0, repes):
            numeros=[]
            for i in range(0, n):
                x = gamma(espC, varC)
                numeros.append(x)
            esp1 = np.mean(numeros)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas, varC, espC)

    elif (rta==4):
        esperanzas=[]
        desvios=[]
        numeros=[]
        for j in range(0, repes):
            numeros=[]
            for i in range(0, n):
                x = normal(espC, varC)
                numeros.append(x)
            esp1 = np.mean(numeros)
            desv1=np.std(numeros)
            esperanzas.append(esp1)
            desvios.append(desv1)
        dif_esperanzas(esperanzas, varC, espC)
        grafico_normal(espC, desvC, esperanzas, desvios)

    elif (rta==5):
        numeros=[]
        esperanzas=[]
        for j in range(0, repes):
            numeros=[]
            for i in range(0, n):
                esp1=3
                var1=4
                x = pascal(esp1, var1)
                numeros.append(x)
            esp2 = np.mean(numeros)
            esperanzas.append(esp2)
        dif_esperanzas(esperanzas, var1, esp1)

    elif (rta==6):
        numeros=[]
        esperanzas = []
        param_n=[]
        param_p=[]
        for j in range(0, repes):
            numeros=[]
            for i in range(0, n):
                x, n, p = binomial(espD, varD)
                numeros.append(x)
            esp1 = np.mean(numeros)
            var1= np.var(numeros)
            p1 = (esp1-var1)/esp1
            n1 = round((esp1**2) / (esp1-var1))
            param_n.append(n1)
            param_p.append(p1)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas, varD, espD)
        grafico_binomial(param_n, param_p, n, p)

    elif (rta==7):
        numeros=[]
        esperanzas = []
        for j in range(0, repes):
            numeros=[]
            for i in range(0, n):
                x, var, esp= hipergeometrica()
                numeros.append(x)
            esp1 = np.mean(numeros)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas, var, esp)

    elif (rta==8):
        numeros=[]
        esperanzas=[]
        for j in range(0, repes):
            numeros=[]
            for i in range(0, n): 
                    x, lbda = poissonD()
                    numeros.append(x)
            esp1=np.mean(numeros)
            esperanzas.append(esp1)
        dif_esperanzas(esperanzas, lbda, lbda)
        grafico_poisson(esperanzas, lbda)


    elif (rta==9):
        numeros=[]
        esperanzas=[]
        for i in range(0, n): 
            x, esp, var, prob = empirica()
            numeros.append(x)
        esp1=np.mean(numeros)
        esperanzas.append(esp1)
        dif_esperanzas(esperanzas, var, esp) 
        grafico_empirica(numeros, prob)
        

    rta = menu()
