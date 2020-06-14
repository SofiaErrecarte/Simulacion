import random 
import math 
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np
import collections

qlimit=100000000 #mismo parametro para infinito de los evento 

tarrvl=[]#[0]*100 #TIEMPO DE ARRIBO DE CLIENTES A COLA. SOLO TIENE LOS TIEMPOS DE LOS QUE ESTÁN EN COLA. trabajado como pila en python con append al final para agregar y pop(0) para quitar el first in

tne=[0, 0, 0] #TIEMPO DEL SIGUIENTE EVENTO DE TIPO 1 O 2-AGREGAMOS EVENTO 0 PARA USAR DIRECTAMENTE INDICES 1 Y 2

marrvt, mservt, totcus=1,2,8 #MEDIA LLEGADA ENTREARRIBOS, MEDIA TIEMPO DE SERVICIO, TOTAL DE DEMORAS DE CLIENTES P QUE FINALICE EL SISTEMA

nevnts=2 #NUMERO DE TIPOS DE EVENTOS
busy=1 
idle=0 

def expon(esp):  #procedimiento de tp anterior para calcular num con dist exponencial
    r = random.random()
    x = (-esp * math.log(r))
    return x

def init(): #metodo de inicialización de variables
    global time,niq, tlevnt,numcus,totdel,aniq,autil,server,tne,marrvt
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
    #print("tiempos de los sgtes eventos: ",tne)
    for i in range(1,nevnts+1):
        if (tne[i]<mintne):
            mintne=tne[i]
            next_= i
    if (next_ == 0): #verifico que lista de eventos no esté vacía
        print('Lista vacia en tiempo{0}'.format(time))
        stop=1
    if (stop==0): time = mintne #linea que se ejecuta si la lista de eventos no está vacía. no tiene que irse acumulando (ver h en arrive)
    #print('sgte evento elegido:', next_)
    return stop

def arrive():
    global tne, time, marrvt, server, delay, totdel, numcus, mservt, niq
    h=time + expon(marrvt) #time es el reloj, a ese tiempo le sumo un tiempo exponencial de siguiente evento llegada. por eso el reloj no se acumula, ya se acumula acá en cada arrival o en departure
    tne[1]=h
    print ('tiempo de los siguientes eventos',tne[0],' ',tne[1], ' ', tne[2])
    if (server == busy): #mientras el servidor está ocupado no actualizo el tiempo de departure
        niq=niq+1 #nro clientes en cola
        #if que no va
        a=time
        tarrvl.append(a) #guardo en los tiempos de arribos el tiempo de este cliente. tarrvl[niq-1]= a, otra opcion, niq-1 así guarda desde posicion 0. podría ser con append 
        print('Servidor ocupado. Tiempos de proximos arrivos en cola tamaño {0}: {1}'.format(niq, tarrvl))
    else:
        delay=0 #esta linea y la siguiente están sólo para entender mejor el programa pero no modifican nada
        totdel= totdel + delay
        numcus=numcus+1 #nº de clientes que completaron demora
        server=busy
        c=time + expon(mservt) #igual que h. le defino la demora que tendrá este cliente
        tne[2]=c
    print ('tiempo sgtes eventos 2:', tne[0],' ',tne[1], ' ', tne[2])
        
    
def depart():
    global niq,server,tne,totdel,delay,tarrvl,numcus,mservt
    print("Clientes en cola: ", niq)
    if (niq==0): #no hay clientes en cola
        server =idle
        tne[2]=10**30
        print ('sin clientes en cola. tiempo de los siguientes eventos',tne[0],' ',tne[1], ' ', tne[2])
    else:
        niq=niq-1
        prox_cli_cola=tarrvl.pop(0)
        delay = time - prox_cli_cola #sumo la demora del 1er cliente q entró a la cola cuyo tiempo en tarravl guardamos en 0 (niq-1)
        totdel=totdel + delay
        print('Clientes en cola {0}. demora: {1}, tiempo arrival[0]: {2}'.format(niq, delay, prox_cli_cola))
        numcus=numcus+1
        l=time + expon(mservt)
        tne[2]= l
        '''for i in range (0,niq): #al hacer pop arriba, directamente quito al primer cliente que había entrado a la cola de time of arrival, no hace falta mover las posiciones porque directamente se quita y se mueven solos los sgtes tarrivals en cola. dejo la axplicación igual porlas
            x=tarrvl[i+1] #si sólo había 1 evento no entra en el for porque  arriba hice niq-1. por loq ue se hace la salida de ese evento pero no se quita del arreglo. de todos modos no importa porque cuando vuelva a haber otra departure se guarda en [0] y se pisa. puede hacerse esta variable con pop(0).
            tarrvl[i]= x'''
        print('Tiempos proximos de arrivos en cola: ', tarrvl) 
        print('tiempo sgtes eventos 2:', tne[0],' ',tne[1], ' ', tne[2])

            

def report():
    global avgdel, avgniq,numcus,time,aniq,totdel,autil,util
    avgdel=totdel/numcus
    avgniq=aniq/time 
    util=autil/time 
    print('Cantidad de clientes que completaron demora: ', numcus) #para verificar
    print('Demora promedio del cliente en cola: {0}'.format(avgdel))
    print('Numero promedio del cliente en cola: {0}'.format(avgniq))
    print('Utilizacion del Servidor: {0}'.format(util))
    print('Tiempo que finaliza la simulacion: {0}'.format(time))

def uptavg():
    global tsle, time, tlevnt, niq, aniq, autil, server
    tsle = time - tlevnt #tiempo desde el ultimo evento 
    tlevnt=time
    aniq = aniq+(niq*tsle)
    autil = autil+ (server*tsle)

init()  
print ("Tiempo medio entre arrivos(minutos): ",marrvt,'//Tiempo medio de servicio(minutos): ', mservt,'//Número de demoras de clientes p finalizar: ', totcus)
while(numcus<totcus): #verifico que no pase el límite fijado
    stop= timing()
    if (stop==0): #cola de eventos NO vacía
        uptavg()
        if (next_==1):
            print('ARRIVE')
            arrive()
        elif(next_==2):
            print('DEPART')
            depart()
    elif(stop==1): #cola de eventos vacía
        break
report()
