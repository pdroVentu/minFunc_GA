# Algoritmo Genético para minimização de função

O trabalho tem como objetivo o desenvolvimento de um algoritmo genético baseado nos requisitos da seção 3 do artigo “A Survey of Genetic Algorithms” de M. Tomassini. Deseja-se encontrar o valor de x que minimize uma função f(x).

## 1. Critérios

+ Avaliar os indivíduos baseado em sua função fitness (de aptidão), qualificando-os;
+ Tratar a função para que os resultados sejam positivos. No caso, deslocando-a verticalmente em 500 pontos;
+ Localizar o valor mínimo da função modificada;
+ Fazer uso de um critério de parada para o algoritmo. No caso, um número máximo de gerações foi dado.

## 2. Desenvolvimento do algoritmo

Para a implementação foi desenvolvido um cromossomo binário de 10 posições capaz de retornar 1024 valores no range de 0 à 512 num passo de 0.5.<br>
Um valor de fitness é dado para cada elemento da população sendo tal população criada com valores aleatórios dentro dos critérios.<br>
O cromossomo binário é transformado em variável do tipo inteiro para realização de cálculos e float para identificação de seu valor real ao longo do desenvolvimento e para fornecimento dos valores finais.

## 3. Parâmetros

O AG tem como parâmetros fornecidos pelo artigo:
+ Probabilidade de crossover: 0.6
+ Probabilidade de mutação: 0.01
+ Tamanho da população inicial: 50
+ Valor máximo de x: 512
+ Valor máximo provido pelo cromossomo: 1024
Ainda foram estipulados para complementação necessária dos parâmetros um numero máximo de 50 gerações, sendo aplicado o método de seleção da roleta, cruzamento e mutação em um único ponto.

## 4. Resultado

![image](https://github.com/pdroVentu/minFunc_GA/assets/63621493/83733d04-3c26-4e63-b561-40c298a7c8b7)<br>
Figura 1. Gráfico com população inicial aleatória (em vermelho) e população ao final das iterações (em azul).

Após 50 gerações é possível localizar um valor de x mínimo em média na posição de 420 tendo, no gráfico, valores entre 416 e 423.
