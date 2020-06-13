import random 
import math 
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np
import collections

qlimit=10**30 #mismo parametro para infinito de los evento 
#busy, idle, nevnts, next_, niq, numcus, server, totcus
#aniq, autil, marrvt, mservt, time, tlevnt, totdel
tarrvl=[] #ver
tne=[]
marrvt, mservt, totcus=1,0.5,10
nevnts=2 
busy=1
idle=0

def expon(esp):   
    r = random.random()
    x = (-esp * math.log(r))
    return x

def init():
    global time,niq, tlevnt,numcus,totdel,aniq,autil,server,tne,marrvt
    time=0
    niq=0
    tlevnt=0
    numcus=0
    totdel=0
    aniq=0
    autil=0
    server=idle
    tne.insert(0,0)
    tne.insert(1,time + expon(marrvt))
    tne.insert(2, 10**30)
    tarrvl.insert(0,0)
    print (tne[0],' ',tne[1], ' ', tne[2])

    #return time,niq,tlevnt,numcus,totdel,aniq,autil,server

def timing():
    global mintne, next_, tne, time,nevnts
    mintne= 10**29
    next_ = 0
    stop=0
    for i in range(1,nevnts+1):
        if (tne[i]<mintne):
            mintne=tne[i]
            #print('Timing',mintne)
            next_= i
    if (next_ == 0):
        print('Lista vacia en tiempo{0}'.format(time))
        stop=1
    print('tiempo1',mintne)
    time = mintne
    return stop

def arrive():
    global tne, time, marrvt, server,delay,totdel,numcus,mservt,niq
    tne.insert(1, time + expon(marrvt))
    if (server == busy):
        niq=niq+1 #nro clientes en cola
        #if que no va
        tarrvl.insert(niq,time)
    else:
        delay=0 #sacar tiempo porm de clientes en cola
        totdel= totdel + delay
        numcus=numcus+1 #nº de clientes que completaron demora
        server=busy
        tne.insert(2, time + expon(mservt)) 
    
def depart():
    global niq,server,tne,totdel,delay,tarrvl,numcus,mservt
    if (niq==0):
        server =idle
        tne.insert(2, 10**30) #ver en variable
    else:
        niq=niq-1
        delay = time - tarrvl[1]
        #print('delay',delay)
        totdel=totdel + delay
        numcus=numcus+1
        tne.insert(2,time + expon(mservt))
        for i in range (1,niq+1): #range(0)???
            tarrvl.insert(i,tarrvl[i+1])

def report():
    global avgdel, avgniq,numcus,time,aniq,totdel,autil,util
    avgdel=totdel/numcus
    avgniq=aniq/time 
    util=autil/time 
    print('Demora promedio del cliente en cola: {0}'.format(avgdel))
    print('Numero promedio del cliente en cola: {0}'.format(avgniq))
    print('Utilizacion del Servidor: {0}'.format(util))
    print('Tiempo que finaliza la simulacion: {0}'.format(time))

def uptavg():
    global tsle, time, tlevnt, niq, aniq, autil, server
    tsle=time - tlevnt
    tlevnt=time
    aniq=aniq+(niq*tsle)
    autil = autil+ (server*tsle)


init()  
print(time,niq,tlevnt,numcus,totdel,aniq,autil)
print (marrvt,' ', mservt,' ', totcus)
while(numcus<totcus):
    stop= timing()
    if (stop==0):
        print('tiempo2' ,time)
        #print(next_)
        uptavg()
        if (next_==1):
            arrive()
        elif(next_==2):
            depart()
            #print(totdel)
    elif(stop==1):
        break
print(tarrvl)
report()

