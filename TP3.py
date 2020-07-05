import random 
import math 
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np
import collections


util_corridas=[]
avgniq_corridas=[]
avgdel_corridas=[]
w_corridas=[]
l_corridas=[]
pn_corridas=[]
time_corridas=[]
stop2_corridas=[]
deneg_corridas=[]
pn=0
p0=0
repes=10 #define cuantas corridas comparamos
pn_corridas=[] #guarda en cada corrida i cuentas veces hubo cola de longitud n_cli
prob_corridas=[] #guarda la probabilidad en cada corrida i de que haya cola de longitud n_cli



def expon(lambda_):  #procedimiento de tp anterior para calcular num con dist exponencial
    r = random.random()
    esp=1/lambda_
    x = (-esp * math.log(r))
    return x

def init(): #metodo de inicialización de variables
    global time,niq, tlevnt,numcus,totdel,aniq,autil,server,tne,marrvt, qlimit, nevnts, tarrvl, totcus, mservt, busy, idle, avgniq_acum, util_acum, numcus_acum, time_acum, avgdel_acum, server_acum, niq_acum, n_cli, deneg_serv, cont_niq, pn, w_acum, l_acum, pn_corridas

    qlimit=20 #mismo parametro para infinito de los evento 
    
    n_cli= 1 #probabilidad de n cli en cola
    
    tarrvl=[]#[0]*100 #TIEMPO DE ARRIBO DE CLIENTES A COLA. SOLO TIENE LOS TIEMPOS DE LOS QUE ESTÁN EN COLA. trabajado como pila en python con append al final para agregar y pop(0) para quitar el first in

    tne=[0, 0, 0] #TIEMPO DEL SIGUIENTE EVENTO DE TIPO 1 O 2-AGREGAMOS EVENTO 0 PARA USAR DIRECTAMENTE INDICES 1 Y 2

    marrvt, mservt, totcus=8,9,500 #LAMBDA LLEGADA ENTREARRIBOS, MEDIA(mu) TIEMPO DE SERVICIO, TOTAL DE DEMORAS DE CLIENTES P QUE FINALICE EL SISTEMA

    nevnts=2 #NUMERO DE TIPOS DE EVENTOS
    busy=1 
    idle=0 
    time_acum=[]
    util_acum=[]
    avgniq_acum=[]
    numcus_acum=[]
    avgdel_acum=[]
    w_acum=[]
    l_acum=[]
    niq_acum=[]
    server_acum=[]
    
    cont_niq=[0]*qlimit #arreglo que acumula en cada i las veces que tengo i cli en cola
    time=0
    niq=0 #NUMERO DE CLIENTES ACTUALMENTE EN COLA
    tlevnt=0 #TIEMPO DEL ULTIMO EVENTO
    numcus=0 # CLIENTES QUE COMPLETARON DEMORA
    totdel=0 #TOTAL DE DEMORAS COMPLETADAS
    aniq=0 #AREA DEBAJO DE Q(T)
    autil=0 #AREA DEBAJO DE B(T)
    deneg_serv=0
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
    stop2=0
    #print ('tiempo de los siguientes eventos',tne[0],' ',tne[1], ' ', tne[2])
    if (server == busy): #mientras el servidor está ocupado no actualizo el tiempo de departure
        niq=niq+1 #nro clientes en cola
        if(niq >= qlimit):
            print('Error. No se aceptan más clientes en cola. Tiempo: ', time)
            stop2=1
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
    return stop2

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
    global avgdel, avgniq,numcus,time,aniq,totdel,autil,util, w, l, pn, p0, cont_niq, pn_corridas, n_corrida
    avgdel=totdel/numcus
    avgniq=aniq/time 
    util=autil/time
    w = avgdel + (1/mservt)
    l = marrvt * w    
    util_corridas.append(util)
    avgdel_corridas.append(avgdel)
    avgniq_corridas.append(avgniq)
    w_corridas.append(w)
    l_corridas.append(l)
    time_corridas.append(time)
    pn_corridas.append(cont_niq[n_cli])
    prob_corridas.append(cont_niq[n_cli]/(sum(cont_niq)))
    print('Cantidad de clientes que completaron demora: ', numcus) #para verificar
    print('Demora promedio del cliente en cola: {0}'.format(avgdel))
    print('Numero promedio del cliente en cola: {0}'.format(avgniq))
    print('Utilizacion del Servidor: {0}'.format(util))
    print('Demora promedio de clientes en sistema: {0}'.format(w))
    print('Número promedio de clientes en sistema: {0}'.format(l))
    print('Probabilidad de {0} clientes en el sistema: {1}'.format(n_cli, pn))
    print('Tiempo que finaliza la simulacion: {0}'.format(time))
    print('Cantidad de veces que la cola tuvo (i) tamaño: ', cont_niq)
    print('Cantidad de veces que la cola tuvo tamaño {0}: {1}'.format(n_cli, cont_niq[n_cli]))   

def uptavg():
    global tsle, time, tlevnt, niq, aniq, autil, server, totdel, numcus, avgdel_acum, server_acum, niq_acum, cont_niq
    tsle = time - tlevnt #tiempo desde el ultimo evento 
    tlevnt=time
    avgniq_acum.append(aniq/time) #seria hacer el report en cada vuelta
    util_acum.append(autil/time)#seria hacer el report en cada vuelta
    if(numcus==0): 
        avgdel_acum.append(0)
        w_acum.append(0)
        l_acum.append(0)
    
    if(numcus!=0): 
        avgdel_acum.append(totdel/numcus) #avgdel
        w_acum.append( (totdel/numcus) + (1/mservt)) #w
        l_acum.append(marrvt * ( (totdel/numcus) + (1/mservt))) 

    numcus_acum.append(numcus)
    time_acum.append(time)
    server_acum.append(server)
    niq_acum.append(niq)
    aniq = aniq+(niq*tsle)
    autil = autil+ (server*tsle)
    cont_niq[niq]=cont_niq[niq]+1 




for i in range(0, repes):
    global n_corrida
    n_corrida=i
    init()  
    print ("Tiempo medio entre arrivos(minutos): ",marrvt,'//Tiempo medio de servicio(minutos): ', mservt,'//Número de demoras de clientes p finalizar: ', totcus)
    while(numcus<totcus): #verifico que no pase el límite fijado
        stop= timing()
        if (stop==0): #cola de eventos NO vacía
            uptavg()
            if (next_==1):
                #print('ARRIVE ')
                stop2=arrive()
                if(stop2==1): break
            elif(next_==2):
                #print('DEPART')
                depart()
        elif(stop==1): #cola de eventos vacía
            break
    stop2_corridas.append(stop2)
    report()

    plt.subplot(321)
    plt.plot(numcus_acum, avgdel_acum, alpha=0.5)
    plt.subplot(323)
    plt.plot(time_acum, avgniq_acum, alpha=0.5)
    plt.subplot(325)
    plt.plot(time_acum, util_acum, alpha=0.5)
    plt.subplot(222)
    plt.plot(numcus_acum, w_acum, alpha=0.5)
    plt.subplot(224)
    plt.plot(time_acum, l_acum, alpha=0.5)


#PROMEDIO DE PROMEDIOS

#valores teóricos
ro= marrvt/mservt #u(n) utilización del servidor
p=ro
lq= (ro**2)/(1-ro) #q(n) promedio de clientes en cola (longitud)
wq= lq/marrvt #d(n) demora (tiempo) promedio de clientes en cola
w_esp= wq + (1/mservt)# tiempo promedio de demora en sistema
l_esp= marrvt*w_esp # numero promedio de cli en sistema
p0 = 1 - ro
pn = (ro)**n_cli *p0 #probabilidad de n cli en sistema
if (qlimit <= 100): deneg_serv = 1 - sum((ro)**i * p0 for i in range (0, qlimit)) # probabilidad de denegación de servicio

porc=np.mean(util_corridas)*100
print ("\nPROMEDIO DE PROMEDIOS: \nDemora promedio en cola Wq observada: ",np.mean(avgdel_corridas),
    '\nDemora promedio en cola Wq esperada: ',wq,
    '\nLongitud promedio en cola Lq observada: ', np.mean(avgniq_corridas),
    '\nLongitud promedio en cola Lq esperada: ', lq,
    '\nUtilización del servidor u(n) observada : %.2f ' % (porc), '%', 
    '\nUtilización del servidor u(n) esperada: %.2f ' % (ro*100), '%', 
    '\nDemora promedio en el sistema W observada: ', np.mean(w_corridas), 
    '\nDemora promedio en el sistema W esperada: ', w_esp, 
    '\nNúmero promedio de clientes en el sistema L observada: ', np.mean(l_corridas), 
    '\nNúmero promedio de clientes en el sistema L esperada: ', l_esp, 
    '\nProbabilidad promedio observada de {0} clientes en sistema: {1}'.format(n_cli, sum(prob_corridas)/repes), 
    '\nProbabilidad promedio esperada de {0} clientes en sistema: {1}'.format(n_cli, pn),
    '\nProbabilidad promedio observada de denegación de servicio: ', (sum(stop2_corridas))/repes,
    '\nProbabilidad promedio esperada de denegación de servicio: ', deneg_serv)
    

#print('Corridas en las cuales se denegó (1) o no (0) el servicio: ', stop2_corridas)
#print('Cantidad de veces que la cola tuvo (i) tamaño: ', cont_niq)
#print('Cantidad de veces que la cola tuvo {0} tamaño en i corrida: {1}'.format(n_cli, pn_corridas))
#print('Probabilidad observada de cola de longitud {0} en cada corrida i: {1}'.format(n_cli, prob_corridas))

#GRÁFICAS
#1
x1=range(0, totcus)  
plt.subplot(321)
plt.plot(x1, [np.mean(avgdel_corridas) for i in x1], label="d(n) Observada")
plt.plot(x1, [wq for i in x1], label="d(n) Esperada")#por calcu
plt.xlabel("Clientes")
plt.ylabel("D(n)")
plt.title("Demora promedio en cola")
plt.legend()

x=range(0, round(max(time_corridas))+1)
plt.subplot(323)
plt.plot(x, [np.mean(avgniq_corridas) for i in x], label="q(t) Observada")
plt.plot(x, [lq for i in x], label="q(t) Esperada")
plt.xlabel("Tiempo (t)")
plt.ylabel("Q(t)")
plt.title("Longitud promedio de la cola")
plt.legend()

plt.subplot(325)
plt.plot(x, [np.mean(util_corridas) for i in x], label="u(t) Observada")
plt.plot(x, [p for i in x], label="u(t) Esperada")
plt.xlabel("Tiempo (t)")
plt.ylabel("B(t)")
plt.title("Utilización del servidor")
plt.legend()

x1=range(0, totcus)  
plt.subplot(222)
plt.plot(x1, [np.mean(w_corridas) for i in x1], label="w(n) Observada")
plt.plot(x1, [w_esp for i in x1], label="w(n) Esperada")#por calcu
plt.xlabel("Clientes")
plt.ylabel("W(n)")
plt.title("Demora promedio en el sistema")
plt.legend()

plt.subplot(224)
plt.plot(x, [np.mean(l_corridas) for i in x], label="L(t) Observada")
plt.plot(x, [l_esp for i in x], label="L(t) Esperada")
plt.xlabel("Tiempo (t)")
plt.ylabel("L(t)")
plt.title("Número promedio de clientes en el sistema")
plt.legend()
plt.show()

#2
plt.subplot(211)
plt.step(time_acum, server_acum)
plt.fill_between(time_acum,server_acum, step="pre", alpha=0.4)
plt.title("Estado del servidor de corrida {0} con {1} clientes".format(i+1, totcus))
plt.xlabel("Tiempo (t)")
plt.ylabel("B(t)")

plt.subplot(212)
plt.step(time_acum, niq_acum, color="r")
plt.fill_between(time_acum,niq_acum, step="pre", alpha=0.4, color='r')
plt.title("Variación de la longitud de la cola de corrida {0} con {1} clientes".format(i+1, totcus))
plt.xlabel("Tiempo (t)")
plt.ylabel("Q(t)")
plt.show()

#3
plt.pie([porc, 100-porc], labels=['Busy', 'Idle'], autopct='%.2f%%', shadow=True, startangle=90, colors=['magenta', 'pink'])
plt.title("Utilización del servidor")
plt.show()

#4
X = np.arange(repes)
plt.bar(X + 0.00, pn, color = "magenta", width = 0.25, label='Pn Esperada')
plt.bar(X + 0.25, prob_corridas, color = "pink", width = 0.25, label='Pn Observada')
plt.xticks(X+0.12, ["1","2","3","4", "5", "6", "7", "8", "9", "10"])
plt.title('Probabilidad de {0} clientes en cola'.format(n_cli))
plt.ylabel('Pn')
plt.xlabel('Corridas')
plt.legend()
plt.show()
