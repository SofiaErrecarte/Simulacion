import random 
import math 
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np
import collections


util_corridas=[]
avgniq_corridas=[]
avgdel_corridas=[]
time_corridas=[]

def expon(lambda_):  #procedimiento de tp anterior para calcular num con dist exponencial
    r = random.random()
    esp=1/lambda_
    x = (-esp * math.log(r))
    return x


def init(): #metodo de inicialización de variables
    global time,niq, tlevnt,numcus,totdel,aniq,autil,server,tne,marrvt, qlimit, nevnts, tarrvl, totcus, mservt, busy, idle, avgniq_acum, util_acum, numcus_acum, time_acum, avgdel_acum, server_acum, niq_acum

    qlimit=100000000 #mismo parametro para infinito de los evento 

    tarrvl=[]#[0]*100 #TIEMPO DE ARRIBO DE CLIENTES A COLA. SOLO TIENE LOS TIEMPOS DE LOS QUE ESTÁN EN COLA. trabajado como pila en python con append al final para agregar y pop(0) para quitar el first in

    tne=[0, 0, 0] #TIEMPO DEL SIGUIENTE EVENTO DE TIPO 1 O 2-AGREGAMOS EVENTO 0 PARA USAR DIRECTAMENTE INDICES 1 Y 2

    marrvt, mservt, totcus=1,2,15 #LAMBDA LLEGADA ENTREARRIBOS, MEDIA TIEMPO DE SERVICIO, TOTAL DE DEMORAS DE CLIENTES P QUE FINALICE EL SISTEMA

    nevnts=2 #NUMERO DE TIPOS DE EVENTOS
    busy=1 
    idle=0 
    time_acum=[]
    util_acum=[]
    avgniq_acum=[]
    numcus_acum=[]
    avgdel_acum=[]
    niq_acum=[]
    server_acum=[]
    time=0
    niq=0 #NUMERO DE CLIENTES ACTUALMENTE EN COLA
    tlevnt=0 #TIEMPO DEL ULTIMO EVENTO
    numcus=0 # CLIENTES QUE COMPLETARON DEMORA
    totdel=0 #TOTAL DE DEMORAS COMPLETADAS
    aniq=0 #AREA DEBAJO DE Q(T)
    autil=0 #AREA DEBAJO DE B(T)
    server=idle
    t=time + expon(marrvt)
    tne[1]= t #inicializo los tiempos de cada tipo de evento
    tne[2]=10**30
    print (tne[0],' ',tne[1], ' ', tne[2])

def timing():
    global mintne, next_, tne, time,nevnts
    mintne= 10**29 #MINIMO TIEMPO DEL SIGUIENTE EVENTO
    next_ = 0 #Next almacena 0 si no hay otro evento, o 1 o 2 dependiendo el mintne. si es 0, pasa por el if de lista de eventos vacíos
    stop=0
    for i in range(1,nevnts+1):
        if (tne[i]<mintne):
            mintne=tne[i]
            next_= i
    if (next_ == 0): #verifico que lista de eventos no esté vacía
        print('Lista vacia en tiempo{0}'.format(time))
        stop=1
    if (stop==0): time = mintne #linea que se ejecuta si la lista de eventos no está vacía. no tiene que irse acumulando (ver h en arrive)
    return stop

def arrive():
    global tne, time, marrvt, server, delay, totdel, numcus, mservt, niq
    h=time + expon(marrvt) #time es el reloj, a ese tiempo le sumo un tiempo exponencial de siguiente evento llegada. por eso el reloj no se acumula, ya se acumula acá en cada arrival o en departure
    tne[1]=h
    #print ('tiempo de los siguientes eventos',tne[0],' ',tne[1], ' ', tne[2])
    if (server == busy): #mientras el servidor está ocupado no actualizo el tiempo de departure
        niq=niq+1 #nro clientes en cola
        #if que no va
        a=time
        tarrvl.append(a) #guardo en los tiempos de arribos el tiempo de este cliente. tarrvl[niq-1]= a, otra opcion, niq-1 así guarda desde posicion 0. podría ser con append 
        #print('Servidor ocupado. Tiempos de proximos arrivos en cola tamaño {0}: {1}'.format(niq, tarrvl))
    else:
        delay=0 #esta linea y la siguiente están sólo para entender mejor el programa pero no modifican nada
        totdel= totdel + delay
        numcus=numcus+1 #nº de clientes que completaron demora
        server=busy
        c=time + expon(mservt) #igual que h. le defino la demora que tendrá este cliente
        tne[2]=c
    #print ('tiempo sgtes eventos 2:', tne[0],' ',tne[1], ' ', tne[2]) 
        
    
def depart():
    global niq,server,tne,totdel,delay,tarrvl,numcus,mservt
    #print("Clientes en cola: ", niq)
    if (niq==0): #no hay clientes en cola
        server =idle
        tne[2]=10**30
        #print ('sin clientes en cola. tiempo de los siguientes eventos',tne[0],' ',tne[1], ' ', tne[2])
    else:
        niq=niq-1
        prox_cli_cola=tarrvl.pop(0)
        delay = time - prox_cli_cola #sumo la demora del 1er cliente q entró a la cola cuyo tiempo en tarravl guardamos en 0 (niq-1). tarrvl[1]
        totdel=totdel + delay
        #print('Clientes en cola {0}. demora: {1}, tiempo arrival[0]: {2}'.format(niq, delay, prox_cli_cola))
        numcus=numcus+1
        l=time + expon(mservt)
        tne[2]= l
        #print('Tiempos proximos de arrivos en cola: ', tarrvl) 
        #print('tiempo sgtes eventos 2:', tne[0],' ',tne[1], ' ', tne[2])


def report():
    global avgdel, avgniq,numcus,time,aniq,totdel,autil,util
    avgdel=totdel/numcus
    avgniq=aniq/time 
    util=autil/time
    util_corridas.append(util)
    avgdel_corridas.append(avgdel)
    avgniq_corridas.append(avgniq) 
    time_corridas.append(time)
    print('Cantidad de clientes que completaron demora: ', numcus) #para verificar
    print('Demora promedio del cliente en cola: {0}'.format(avgdel))
    print('Numero promedio del cliente en cola: {0}'.format(avgniq))
    print('Utilizacion del Servidor: {0}'.format(util))
    print('Tiempo que finaliza la simulacion: {0}'.format(time))

def uptavg():
    global tsle, time, tlevnt, niq, aniq, autil, server, totdel, numcus, avgdel_acum, server_acum, niq_acum
    tsle = time - tlevnt #tiempo desde el ultimo evento 
    tlevnt=time
    avgniq_acum.append(aniq/time) #seria hacer el report en cada vuelta
    util_acum.append(autil/time)#seria hacer el report en cada vuelta
    if(numcus==0): avgdel_acum.append(0)
    if(numcus!=0): avgdel_acum.append(totdel/numcus)
    numcus_acum.append(numcus)
    time_acum.append(time)
    server_acum.append(server)
    niq_acum.append(niq)
    aniq = aniq+(niq*tsle)
    autil = autil+ (server*tsle)


repes=1 #define cuantas corridas comparamos
for i in range(0, repes):
    init()  
    print ("Tiempo medio entre arrivos(minutos): ",marrvt,'//Tiempo medio de servicio(minutos): ', mservt,'//Número de demoras de clientes p finalizar: ', totcus)
    while(numcus<totcus): #verifico que no pase el límite fijado
        stop= timing()
        if (stop==0): #cola de eventos NO vacía
            uptavg()
            if (next_==1):
                #print('ARRIVE ')
                arrive()
            elif(next_==2):
                #print('DEPART')
                depart()
        elif(stop==1): #cola de eventos vacía
            break
    report()
    plt.subplot(131)
    plt.plot(numcus_acum, avgdel_acum, label="Corrida {0}".format(i+1), alpha=0.5)
    plt.subplot(132)
    plt.plot(time_acum, avgniq_acum, label="Corrida {0}".format(i+1), alpha=0.5)
    plt.subplot(133)
    plt.plot(time_acum, util_acum, label="Corrida {0}".format(i+1), alpha=0.5)
    

#PROMEDIO DE PROMEDIOS
wq= 0.5 #d(n)
p= 0.5 #u(n)
lq= 0.5 #q(n)
x1=range(0, totcus)  
plt.subplot(131)
plt.plot(x1, [np.mean(avgdel_corridas) for i in x1], label="d(n) Observada")
plt.plot(x1, [wq for i in x1], label="d(n) Esperada")#por calcu
plt.xlabel("Totcus (n)")
plt.ylabel("D(n)")
plt.title("Demora promedio en cola")
plt.legend()

x=range(0, round(max(time_corridas)))
plt.subplot(132)
plt.plot(x, [np.mean(avgniq_corridas) for i in x], label="q(n) Observada")
plt.plot(x, [0.5 for i in x], label="q(n) Esperada")
plt.xlabel("Tiempo (t)")
plt.ylabel("Q(t)")
plt.title("Longitud promedio de la cola")
plt.legend()

plt.subplot(133)
plt.plot(x, [np.mean(util_corridas) for i in x], label="u(n) Observada")
plt.plot(x, [p for i in x], label="u(n) Esperada")
plt.xlabel("Tiempo (t)")
plt.ylabel("B(t)")
plt.title("Utilización del servidor")
plt.legend()
plt.show()



plt.subplot(121)
plt.step(time_acum, server_acum)
plt.fill_between(time_acum,server_acum, step="pre", alpha=0.4)
plt.title("Estado del servidor de corrida {0} con {1} clientes".format(i+1, totcus))
plt.xlabel("Tiempo (t)")
plt.ylabel("B(t)")

plt.subplot(122)
plt.step(time_acum, niq_acum, color="r")
plt.fill_between(time_acum,niq_acum, step="pre", alpha=0.4, color='r')
plt.title("Variación de la longitud de la cola de corrida {0} con {1} clientes".format(i+1, totcus))
plt.xlabel("Tiempo (t)")
plt.ylabel("Q(t)")
plt.show()

porc=np.mean(util_corridas)*100
print ("\nPROMEDIO DE PROMEDIOS:\nDemora promedio en cola d(n): ",np.mean(avgdel_corridas),'\nLongitud promedio en cola q(n): ', np.mean(avgniq_corridas),'\nUtilización del servidor u(n): %.2f ' % (porc), '%')
plt.pie([porc, 100-porc], labels=['Busy', 'Idle'], autopct='%.2f%%', shadow=True, startangle=90, colors=['pink', 'cyan'])
plt.title("Utilización del servidor")
plt.show()
