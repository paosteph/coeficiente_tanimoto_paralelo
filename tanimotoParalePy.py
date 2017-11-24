from __future__ import division
import multiprocessing
import threading
import time
import math


def calcularMat(lim1, lim2, result):
    en=0
    for i in range(lim1, lim2):
        for j in range(i+1, n):
            compAB=identif[i]+'\t'+identif[j]
            result.append(compAB+'\t'+str(coefTanimoto(i,j)))
            en+=1
    print 'Puntos de',threading.current_thread().name,': ',en

def coefTanimoto(a,b):
    elemA = formulaContada[a]
    elemB = formulaContada[b]

    Na = Nb = Nc = aa = ab = ac = 0

    for i in range(0, 16):
        if elemA[i] != 0 or elemB[i] != 0:
            if i == 0:
                if (elemA[i] > 0 and elemB[i] > 0):
                    aa = ab = ac = 1
                elif (elemA[i] > 0):
                    aa = 1
                else:
                    ab = 1
            else:
                #Nc = [lambda : Nc+elemA[i], lambda : Nc+elemB[i]][elemA[i] > elemB[i]]()
                if elemA[i] > elemB[i]:
                    Nc += elemB[i]
                else:
                    Nc += elemA[i]
                Na += elemA[i]
                Nb += elemB[i]
    Na += aa
    Nb += ab
    Nc += ac
    coef = Nc / (Na + Nb - Nc)
    return round(coef,2)

def contar(comp):
    cont = [0] * 16
    caracteres = {'@':0, 'c':1, 'C':2, 'F':3, 'H':4, 'I':5, 'N':6, 'O':7, 'P':8,
                  'S':9, 'B':10, 'l':11, 'n':12, 'o':13, 'r':14, 's':15}
    for c in comp:
        if c in caracteres:
            pos = caracteres.get(c)
            cont[pos] += 1
    return cont

def contarTodo(formT):
    listacontada = []
    for comp in formT:
            listacontada.append(contar(comp))
    return listacontada

def calcularLimites(p):
    lim=[]
    for a in range(p):
        if a == 0:
            lim.append(int(n - math.sqrt((p - a) / p) * n))
            lim.append(int(n - math.sqrt((p - a - 1) / p) * n))
        else:
            lim.append(int(n - math.sqrt((p - a - 1) / p) * n))
    print 'Puntos: ',lim
    return lim

def iniciarHilos(thread_array):
    for t in thread_array:
        t.start()
    for t in thread_array:
        t.join()


#**************Principal**************
start=time.time()

archivo = open('ZINC_chemicals.tsv', 'r')
lineasTotales = archivo.readlines()
identif = []
formula = []
for linea in lineasTotales:
    identif.append( (linea.split('\t'))[1].strip('\n') )
    formula.append( (linea.split('\t'))[3].strip('\n') )
archivo.close()

formulaContada = contarTodo(formula)

end=time.time()
print 'Abrir y contar archivo: ',end-start, ' segundos'

start = time.time()
p=2
n=1000
resultadoHilo=[]
for i in range(p):
   resultadoHilo.append([] * p)

#paralelizacion en calculo de coef_Tanimoto
limites = calcularLimites(p)
hilos=[]

for i in range(p):
    hilos.append(threading.Thread(target=calcularMat, args=(limites[i], limites[i + 1], resultadoHilo[i])))

iniciarHilos(hilos)

end = time.time()
print 'Calcular coef Tanimoto: ',end - start, ' segundos'

start = time.time()
archivoResultado = open('Zinc_coefTanimoto.txt', 'w')
for hilo in resultadoHilo:
    for rcoef in hilo:
        archivoResultado.write(rcoef+'\n')
archivoResultado.close()

end = time.time()
print 'Escribir archivo: ',end - start, ' segundos'

#C=[[0]*n for x in range(n)]
#for i in range(n):
#   m.append([0]*n)
#
# numC = []
# for c in cont:
#    if c > 0:
#        numC.append((chr(i),c))
#    i+=1
#h=0
# for hilo in coeficientes:
#    m = 0
#   j = 1
#   for i in range(len(hilo)):
#        id1 = identif[etiquetas[h][m]]
#       id2 = identif[etiquetas[h][j]]
#        coef = hilo[i]
#        #print id1 + '\t' + id2 + '\t' + str(coef) + '\n'
#        archivoCoef.writelines(id1+'\t'+id2+'\t'+str(coef)+'\n')
#        m+=2
#        j+=2
#    h+=1