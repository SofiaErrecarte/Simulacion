import random
import math
import matplotlib.pyplot as plt
import statistics as stats
import collections

tiradas = int(input("Ingrese numero de tiradas: "))
numero = int(input("Ingrese un numero a apostar: "))
corridas= int(input("Ingrese cantidad de veces a ejecutar: "))
numeros_ruleta = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                  26, 27, 28, 29, 30, 31, 32, 33, 35, 35, 36]
frec_esperada = 1/37
prom= stats.mean(numeros_ruleta)
varianza= stats.variance(numeros_ruleta)
desvio= stats.stdev(numeros_ruleta)

for j in range(0,corridas):

    numeros_aleatorios = [0]*tiradas
    frec_relativa = []
    valor_promedio = []
    varianza_lista = []
    varianza_lista.append(0)
    desvio_lista = []
    desvio_lista.append(0)
    cont_relativa = 0
    cont_tiradas = 1
    acum=0
    var=0
    acum_v=0
    for i in range(0,tiradas):
        n = random.randint(0,36)
        numeros_aleatorios[i]=n
        acum = acum + n
        valor_promedio.insert(i,acum/cont_tiradas)
        acum_v= acum_v+(n-prom)**2
        if cont_tiradas!= 1 :
            var = ((acum_v) / (cont_tiradas-1))
            varianza_lista.insert(i, var)
            desvio_lista.insert(i, math.sqrt(var))

        if n == numero:
            cont_relativa+=1
            frec_relativa.insert(i,cont_relativa/cont_tiradas)
        else:
            frec_relativa.insert(i,cont_relativa/cont_tiradas)
        cont_tiradas += 1

    #Graficas
    x=range(0,tiradas)
    plt.subplot(221)
    plt.plot(x,frec_relativa)
    plt.subplot(222)
    plt.plot(x,valor_promedio)
    plt.subplot(223)
    plt.plot(x, varianza_lista)
    plt.subplot(224)
    plt.plot(x, desvio_lista)


plt.subplot(221)
plt.plot(x, [frec_esperada for i in x], label="FR Esperada")
plt.legend(loc="lower right")
plt.title('Frecuencia Relativa')
plt.ylabel('FR para el número ' + str(numero))
plt.xlabel('N(tiradas)')

plt.subplot(222)
plt.plot(x, [prom for i in x], label="Prom. Esperado")
plt.legend(loc="lower right")
plt.title('Valor Promedio')
plt.ylabel('Valor Promedio')
plt.xlabel('N(tiradas)')

plt.subplot(223)
plt.plot(x, [varianza for i in x], label="Var. Esperada")
plt.legend(loc="lower right")
plt.title('Varianza')
plt.ylabel('VAR')
plt.xlabel('N(tiradas)')

plt.subplot(224)
plt.plot(x, [desvio for i in x], label="Desv. Esperada")
plt.legend(loc="lower right")
plt.title('Desviación Estándar')
plt.ylabel('STD')
plt.xlabel('N(tiradas)')

plt.show()
if corridas==1:
    freq_absoulta = collections.Counter(numeros_aleatorios)
    freq_relativa = {k: v / tiradas for k, v in freq_absoulta.items()}
    plt.subplot(211)
    plt.boxplot(numeros_aleatorios, vert=False)
    plt.title("Diagrama de caja")
    plt.xlabel("Numeros de Ruleta")
    plt.ylabel("n(corridas)")
    plt.subplot(223)
    plt.stem(freq_absoulta.keys(), freq_absoulta.values(), use_line_collection=True)
    plt.title("Frecuencia Absoluta")
    plt.ylabel("FAbs")
    plt.xlabel("Numeros de Ruleta")
    plt.subplot(224)
    plt.stem(freq_relativa.keys(), freq_relativa.values(), use_line_collection=True)
    plt.stem(freq_relativa.keys(), freq_relativa.values(), use_line_collection=True)
    plt.title("Frecuencia Relativa")
    plt.ylabel("FR")
    plt.xlabel("Numeros de Ruleta")
    plt.show()
