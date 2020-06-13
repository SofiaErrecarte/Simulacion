import random 
import math 
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np
import collections

qlimit=100000000 #mismo parametro para infinito de los evento 
#busy, idle, nevnts, next_, niq, numcus, server, totcus
#aniq, autil, marrvt, mservt, time, tlevnt, totdel
tarrvl=[0]*100 #ver
tne=[]
marrvt, mservt, totcus=0.7,0.9,100
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
    t=time + expon(marrvt)
    tne.insert(1,t)
    tne.insert(2, 10**30)
    tarrvl.insert(niq,t)
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
    #print('tiempo1',mintne)
    time = mintne
    return stop

def arrive():
    global tne, time, marrvt, server, delay, totdel, numcus, mservt, niq
    h=time + expon(marrvt)
    tne[1]=h
    #tne.insert(1, time + expon(marrvt))
    if (server == busy):
        niq=niq+1 #nro clientes en cola
        #if que no va
        a=time
        #print (niq)
        tarrvl[niq]=a
        #tarrvl.insert(niq,time)
        #print(niq)
    else:
        delay=0 #sacar tiempo porm de clientes en cola
        totdel= totdel + delay
        numcus=numcus+1 #nº de clientes que completaron demora
        server=busy
        c=time + expon(mservt)
        tne[2]=c
        
    
def depart():
    global niq,server,tne,totdel,delay,tarrvl,numcus,mservt
    if (niq==0):
        server =idle
        x=10000000
        tne[2]=x
        #tne.insert(2, 10**30) #ver en variable
    else:
        niq=niq-1
        delay = time - tarrvl[0]
        #print('delay',delay)
        totdel=totdel + delay
        numcus=numcus+1
        l=time + expon(mservt)
        tarrvl[2]= l
        #tne.insert(2,time + expon(mservt))
        for i in range (0,niq): #range(0)???
           x=tarrvl[i+1]
           tarrvl[i]= x
           #tarrvl.insert(i,tarrvl[i+1])

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
    tsle = time - tlevnt
    tlevnt=time
    aniq = aniq+(niq*tsle)
    autil = autil+ (server*tsle)
    #print (tsle)

init()  
print(time,niq,tlevnt,numcus,totdel,aniq,autil)
print (marrvt,' ', mservt,' ', totcus)
while(numcus<totcus):
    stop= timing()
    if (stop==0):
        #print('tiempo2' ,time)
        #print(next_)
        uptavg()
        #print(aniq)
        if (next_==1):
            arrive()
        elif(next_==2):
            depart()
            #print(totdel)
    elif(stop==1):
        break
    print('niq',niq)
print(tarrvl)
report()

