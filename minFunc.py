import numpy as np
import matplotlib.pyplot as plt
import random

prob_crossover = 0.6 ## probabilidade de cruzamento
prob_mutation = 0.01 ## probabilidade de mutacao
bases = 10           ## tamanho do binario do cromossomo
ngen = 50            ## numero de geracoes
npop = 50           ## tamanho do populacao

##Funcao a ser minimizada

def y(x): return 500-np.absolute(x * (np.sin(np.sqrt(np.absolute(x)))))

##Populacao inicial
##*0.5 para intervalo de [0,512] com granulacao 0,5
xmin, xmax = 0, 1024
X = np.array(random.sample(range(xmin, xmax), npop), dtype = float)*0.5
X_int = np.array(X*2, dtype = int) ##transforma a populacao para os 1024 valores
chromo= ["{0:010b}".format(i) for i in X_int] ##cromossomos em string binaria

fitness = 1./y(X) #aptidao
popfit = fitness/sum(fitness) ##aptidao relativa da populacao
cprob = np.cumsum(popfit) ##probabilidade acumulada para uso da roleta

##grafico com populacao inicial em vermelho
xgraf = np.linspace(0, 512, 1024)
##plt.subplot(2,1,1)
plt.plot(xgraf, y(xgraf))
plt.plot(X, y(X), 'ro')
plt.title('y(x)')
plt.grid()

##vetores inicialdos para grafico de melhor individo e media da populacao
bv = np.zeros(ngen+1)
bv[0]= min(y(X))
average = np.zeros(ngen+1)
average[0]=np.mean(y(X))

for gen in range(ngen): ##loop para realizar as geracoes

       newpop = []  ##populacao gerada apos sorteio na roleta
       for n in range(npop):
              r = np.random.uniform(0,1)
              for (j, pop) in enumerate(chromo):
                  if r <= cprob[j]:
                      newpop.append(pop)
                      break

       newgen = []  ##nova geracao a ser construida          
       for k in range(0,npop,2):
              P1, P2 = newpop[k], newpop[k+1]          ##pais 1 e 2
              if np.random.random()< prob_crossover:   ##cruzamento
                     cp = np.random.randint(1,bases-1) ##crossover point
                     ch1 = P1[:cp] + P2[cp:]
                     ch2 = P2[:cp] + P1[cp:]             
              else:
                     ch1, ch2 = P1, P2
              if np.random.random()< prob_mutation:   ##mutacao filho 1
                     mp = np.random.randint(0,bases)  ##mutation point
                     mutated = list(ch1)
                     if mutated[mp] == '0':
                            mutated[mp] = '1'
                     else:
                            mutated[mp] = '0'
                     ch1 = ''.join(mutated)
              if np.random.random()< prob_mutation:   ##mutacao filho 2
                     mp = np.random.randint(0,bases)
                     mutated = list(ch2)
                     if mutated[mp] == '0':
                            mutated[mp] = '1'
                     else:
                            mutated[mp] = '0'
                     ch2 = ''.join(mutated)
              newgen.append(ch1)
              newgen.append(ch2)

       population = [] ##populacao no range [0,512]
       for m in range(npop):
              newgenpop = int(newgen[m],2)/2.
              population.append(newgenpop)

       #Novos dados recalculados   
       X = np.array(population)
       X_int = np.array(X*2, dtype = int)
       chromo= ["{0:010b}".format(i) for i in X_int]
       fitness = 1./y(X) 
       popfit = fitness/sum(fitness)
       cprob = np.cumsum(popfit)
       bv[gen+1] = min(y(X))
       average[gen+1]= np.mean(y(X))

#print(np.mean(X))

##pontos em azul da populacao final
plt.plot(population, y(population), 'bo')
##plot dos melhores e da media da populacao
# plt.subplot(2,1,2)
# plt.plot(bv, 'y.-',label='best in generation')
# plt.plot(average,'b*-', label='population average')
# plt.legend(loc='upper center')
plt.show()
