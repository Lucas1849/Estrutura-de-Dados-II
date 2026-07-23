from random import randint
import time

def gerarListaValoresAleatorios(quantidade):
    lista = []
    for i in range(quantidade):
        lista.append(randint(0,1000))

    return lista

aleatorio = gerarListaValoresAleatorios(2000)
aleatorio2 = gerarListaValoresAleatorios(2000)

def Troca(lista, posfix, posvar):
    lista[posfix], lista[posvar] = lista[posvar], lista[posfix]

#Considerações bubble-sort: É a pior forma de ordenação.
#Para resolvermos casos em que a varredura é inútil, pois a lista já está ordenada utilizamos da variável change.
#A função troca é utilizada exclusivamente para atribuição dupla.
def bubblesort(lista):
    for i in range(len(lista)- 1 , 0, -1):
        change = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                Troca(lista, j, j+1)
                change = True
        if change == False:
            break
    return lista

inc = time.time()
bubblesort(aleatorio)
fin = time.time()
temp = fin-inc
print(f'{temp:.5f}')

#Sort para sequências prévias ordenadas
def selectionSort(lista):
    tamanho = len(lista)
    for i in range(tamanho -1):
        menor = i
        for j in range(i+1,tamanho):
            if lista[j] < lista[menor]:
                menor = j

        if (i != menor):
            Troca(lista, i, menor)

def medirTempoBubble(num):
    lista  = gerarListaValoresAleatorios(num)
    inicio = time.time()
    bubblesort(lista)
    final = time.time()
    tempo = final - inicio
    return tempo

def medirTempoSelection(num):
    lista = gerarListaValoresAleatorios(num)
    inicio = time.time()
    selectionSort(lista)
    final = time.time()
    tempo = final - inicio
    return tempo

inicio = time.time()
selectionSort(aleatorio2)
final = time.time()
tempo = final- inicio
print(f'{tempo:.5f}')

print(f'{"Tempo de execução":=^150}')
#Colunas
print(f'{"1000":=^50}',end=''), print(f'{"10000":=^50}',end=''), print(f'{"100000":=^50}')
#Linhas
print(f'{"==Bubble sort"}',end=''), print(f'{medirTempoBubble(1000): ^40}',end='') 
print(f'{medirTempoBubble(10000): ^40}'), "print(f'{medirTempoBubble(100000): ^40}')"

print(f'{"==Selection sort"}',end =''), print(f'{medirTempoSelection(1000): ^40}',end='') 
print(f'{medirTempoSelection(10000): ^40}'), "print(f'{medirTempoSelection(100000): ^40}')"
print(f'{"="*150}')