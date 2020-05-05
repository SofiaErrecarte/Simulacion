def chiCuadrado(numeros):
    n=len(numeros)
    k=10 #hacemos 10 rangos siempre
    #divido todos por la longitud del arreglo
    for i in range(0,n):
        numeros[i]=numeros[i]/n
    print(numeros)
    #Calculamos frecuencias absolutas
    freqs = [0 for i in range(k)]
    
    #Para cada rango
    for i in range(1,k+1):
        max = i/k
        min = max - (1/k)
        for xi in numeros:
            if xi < max and xi >= min:
                #Si el numero esta en el rango, sumamos 1 a la frecuencia de ese rango
                freqs[i-1]+=1
    print('frecuencias: ',freqs)
    
    Ei=n/k #totalDatos/totalIntervalos
    #χ2 = 1/Ei * Σ(Oi - Ei)^2
    chi2 = (1/Ei) * sum ( [ (Oi-(Ei)) **2 for Oi in freqs ] )
    print('chi: ', chi2)
    
    chi_tabla=16.92 #no encuentro en ningun lado como calcularlo sin tabla, cargo directamente porque siempre k=10(9° de libertad) y alfa=0.05
    if (chi2<chi_tabla): print('La hipótesis nula es aceptada. La distribución es uniforme')
    else: print('La hipótesis nula no es aceptada. La distribución no es uniforme')


