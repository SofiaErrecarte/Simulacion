import random
import math
import matplotlib.pyplot as plt
import statistics as stats
import collections

numeros_ruleta = list(range(0,37))
lim_tiradas = 2500 #limite de tiradas p capital infinito, para por docena en cap finito y para funcion capital inicial
monto_ini = 0
lim_capital = monto_ini *10
t_max = []


# MENU
def menu():
    print("Menu: 0 para salir")
    print("1 - Martingala") #Martingala par/impar
    print("2 - Jugar al mismo número")
    print("3 - Jugar por docena")
    rta = int(input("Ingrese la opcion elegida: "))
    return rta

# MARTINGALA
def martingala(capital):
    dinero = []
    rta = int(input("Ingrese 1 si quiere apostar a impar o 2 si quiere apostar a par: "))
    monto = int(input("Ingrese apuesta inicial: "))
    monto_ini= monto
    t = 0
    numerosSalidos = []

    #CAPITAL FINITO
    if capital != 0:

        #IMPAR
        if rta == 1:
            dinero.append(capital)
            while capital>=monto:
                t = t + 1
                n = random.randint(0, 36)
                if n % 2 == 0 or n==0: #num pares o cero
                    x = len(dinero)
                    capital = capital-monto
                    dinero.append(capital) #muestra fluctuacion de caja hasta q se queda sin poder apostar mas 
                    numerosSalidos.append(n)
                    monto = monto * 2 #apuesta el doble de la anterior
                    if monto>lim_capital: monto = monto_ini
                else:
                    x = len(dinero)
                    capital = capital + monto*1 #le pagan monto*1
                    dinero.append(capital)
                    numerosSalidos.append(n)
            x = len(dinero)
            print("Termino su capital en la tirada: ", t)
            t_max.append(t) #va guardando t que es la cantidad de tiradas
            x1 = range(0, x)
            plt.plot(x1, dinero , label="Martingala con capital: {0} - monto: {1}" .format(dinero[0], monto_ini))

        #PAR
        else:
            dinero.append(capital)
            while capital >= monto:
                t = t + 1
                n = random.randint(0, 36)
                if n % 2 != 0 or n==0: #num impares o cero
                    x = len(dinero)
                    capital = capital - monto
                    dinero.append(capital) #muestra fluctuacion de caja hasta q se queda sin poder apostar mas 
                    numerosSalidos.append(n)
                    monto = monto * 2  # apuesta el doble de la anterior
                    if monto>lim_capital: monto = monto_ini
                else:
                    x = len(dinero)
                    capital = capital + monto * 1  # le pagan monto *1
                    dinero.append(capital)
                    numerosSalidos.append(n)
            x = len(dinero)
            print("Termino su capital en la tirada: ", t)
            t_max.append(t) #va guardando t que es la cantidad de tiradas
            x1 = range(0, x)
            plt.plot(x1, dinero , label="Martingala con capital: {0} - monto: {1}" .format(dinero[0], monto_ini))


    #CAPITAL INFINITO
    else:

        #IMPAR
        if rta == 1:
            dinero.append(capital)
            t = 0
            for i in range (0, lim_tiradas) :
                t = t + 1
                n = random.randint(0, 36)
                if n % 2 == 0 or n==0: #num pares o cero
                    x = len(dinero)
                    capital = capital-monto
                    dinero.append(capital) #muestra fluctuacion de caja
                    numerosSalidos.append(n)
                    monto = monto * 2 #apuesta el doble de la anterior
                    if monto>lim_capital: monto = monto_ini #en caso de q ese doble supere el limite, apuesta el monto inicial
                else:
                    x = len(dinero)
                    capital = capital + monto*1 #le pagan monto*1
                    dinero.append(capital)
                    numerosSalidos.append(n)
            x = len(dinero)
            x1 = range(0, x)
            print("Termino su capital en la tirada: ", t)
            t_max.append(t) #va guardando t que es la cantidad de tiradas
            plt.plot(x1, dinero , label="Martingala con monto: {0}" .format(monto_ini))
        
        #PAR
        else:
            dinero.append(capital)
            for i in range (0, lim_tiradas):
                t = t + 1
                n = random.randint(0, 36)
                if n % 2 != 0 or n==0: #num impares o cero
                    x = len(dinero)
                    capital = capital - monto
                    dinero.append(capital) #muestra fluctuacion de caja hasta q se queda sin poder apostar mas 
                    numerosSalidos.append(n)
                    monto = monto * 2  # apuesta el doble de la anterior
                    if monto>lim_capital: monto = monto_ini #en caso de q ese doble supere el limite, apuesta el monto inicial
                else:
                    x = len(dinero)
                    capital = capital + monto * 1  # le pagan el monto*1
                    dinero.append(capital)
                    numerosSalidos.append(n)
            x = len(dinero)
            x1 = range(0, x)
            print("Termino su capital en la tirada: ", t)
            t_max.append(t) #va guardando t que es la cantidad de tiradas
            plt.plot(x1, dinero , label="Martingala con monto: {0}" .format(monto_ini))

# MISMO NUMERO
def mismoNumero(capital):
    dinero = []
    num = int(input("Ingrese el número: "))
    monto = int(input("Ingrese apuesta inicial: "))
    t = 0
    numerosSalidos = []
    monto_ini=monto
    # CAPITAL FINITO
    if capital != 0:
        dinero.append(capital)  # capital inicial
        while capital>=monto:
            t = t + 1
            n = random.randint(0, 36)
            if n != num:
                x = len(dinero)
                capital = capital-monto
                dinero.append(capital) #muestra lo q apuesta y gana hasta q se queda sin plata
                numerosSalidos.append(n)
            else:
                x = len(dinero)
                capital = capital + monto*36
                dinero.append(capital)
                numerosSalidos.append(n)
        x = len(dinero)
        print("Termino su capital en la tirada: ", t)
        t_max.append(t) #va guardando t que es la cantidad de tiradas
        x1 = range(0, x)
        plt.plot(x1, dinero , label="Mismo número con capital: {0} - monto: {1}" .format(dinero[0], monto_ini))

    #CAPITAL INFINITO
    else:
        dinero.append(capital)  # capital inicial
        t = 0
        while t<=lim_tiradas :
            t = t + 1
            n = random.randint(0, 36)
            if n != num:
                x = len(dinero)
                capital = capital-monto
                dinero.append(capital) # muestra lo q apuesta y gana hasta q se queda sin plata
                numerosSalidos.append(n)
                if monto>lim_capital: monto = monto_ini
            else:
                x = len(dinero)
                capital = capital + monto*36
                dinero.append(capital)
                numerosSalidos.append(n)
        x = len(dinero)
        x1 = range(0, x)
        print("Termino su capital en la tirada: ", t)
        t_max.append(t) #va guardando t que es la cantidad de tiradas
        plt.plot(x1, dinero , label="Mismo número con monto: {0}" .format(monto_ini))

#POR DOCENA
def docena(capital):
    rta = int(input("Ingrese a que docena desea apostar: \n1) 1-12 \n2) 13-24 \n3) 25-36\n"))
    dinero = []
    monto = int(input("Ingrese apuesta inicial: "))
    t = 0
    numerosSalidos = []
    monto_ini= monto
    docenax = []
    if rta == 1: 
        docenax=list(range(1,13))
    elif rta == 2: 
        docenax=list(range(13,25))
    elif rta==3: 
        docenax=list(range(25,37))
    

    #CAPITAL FINITO
    if capital!=0:
        porcentaje_calculado = monto_ini*100/capital #se calcula el porcentaje en base al monto y capital
        dinero.append(capital)  # capital inicial
        while capital>=monto : # and t<=lim_tiradas para q no entre en loop
            t = t + 1
            n = random.randint(0, 36)
            if n in docenax:
                x = len(dinero)
                capital = capital + monto*2
                dinero.append(capital)
                numerosSalidos.append(n)
                monto = monto +(monto*porcentaje_calculado) 
                if monto>lim_capital: monto = monto_ini
            else:
                x = len(dinero)
                capital = capital-monto
                dinero.append(capital) #muestra lo q apuesta y gana hasta q se queda sin plata
                numerosSalidos.append(n)
                if monto>lim_capital: monto = monto_ini
        x = len(dinero)
        print("Termino su capital en la tirada: ", t)
        t_max.append(t) #va guardando t que es la cantidad de tiradas
        x1 = range(0, x)
        plt.plot(x1, dinero , label="Por docena con capital: {0} - monto: {1}" .format(dinero[0], monto_ini))
        #plt.plot(x1, [dinero[0] for i in x1]) #capital- poner esto tiene sentido si hacemos grafica con distintos capitales
        
    #CAPITAL INFINITO
    else:
        porcentaje_calculado = 0.1 #forzamos el porcentaje ya q el capital es 0 (infinito)
        dinero.append(capital)  #iniciaria con 0, si no aca ponemos un numero grande
        for i in range(0,lim_tiradas):
            t = t + 1
            n = random.randint(0, 36)
            if n in docenax:
                x = len(dinero)
                capital = capital + monto*2
                dinero.append(capital)
                numerosSalidos.append(n)
                monto = monto +(monto*porcentaje_calculado)
                if monto>lim_capital: monto = monto_ini
            else:
                x = len(dinero)
                capital = capital-monto
                dinero.append(capital) #muestrawd lo q apuesta y gana hasta q se queda sin plata
                numerosSalidos.append(n)
                if monto>lim_capital: monto = monto_ini
        x = len(dinero)
        x1 = range(0, x)
        print("Termino su capital en la tirada: ", t)
        t_max.append(t) #va guardando t que es la cantidad de tiradas
        plt.plot(x1, dinero , label="Por docena con monto: {0}" .format(monto_ini))
        

print("Bienvenidos a la Ruleta")
titulo= input('Titulo: ')
seguir=int(input("1 jugar, 0 salir: "))
while seguir ==1:
    capElegido =  int(input("Ingrese 1 si quiere jugar con capital finito o 2 si quiere jugar con capital infinito: "))
    if capElegido == 1:
        capital = int(input("Cual es su capital : "))
    else:
        capital = 0
    rta = menu()
    if rta == 1: martingala(capital)
    elif rta == 2: mismoNumero(capital)
    elif rta == 3: docena(capital)
    seguir = int(input("1 jugar, 0 salir: "))

capitalIni=capital
t_max.sort()
tirada_max = t_max.pop()
x1 = range(0, tirada_max)
plt.plot(x1, [capitalIni for i in x1]) # capital- poner esto tiene sentido para graficar con mismo capital en todas las jugadas
plt.legend(loc="upper right")
plt.xlabel('N(Tiradas)')
plt.ylabel('$(Dinero)')
plt.title(titulo)
plt.show()
