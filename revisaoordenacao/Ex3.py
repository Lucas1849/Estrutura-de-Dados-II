def particiona(vetor, inicial, final):
    esquerda = inicial
    direita = final
    md = int((esquerda + direita)/2)

    vetor[inicial], vetor[md] = vetor[md], vetor[inicial]
    pivo = vetor[inicial]

    while (esquerda < direita):
        while (vetor[esquerda] < pivo and esquerda <= final ):
            esquerda += 1

        while (vetor[direita] > pivo and direita >= 0):
            direita -= 1

        if (esquerda < direita):
            temp = vetor [direita]
            vetor[direita] = vetor[esquerda]
            vetor[esquerda] = temp
    
    vetor[inicial] = vetor[direita]
    vetor[direita] = pivo
    return direita

def quickSort(vetor, inicio, fim):
    if (fim > inicio):
        pivo = particiona(vetor, inicio, fim)
        quickSort(vetor, inicio, pivo - 1 )
        quickSort(vetor, pivo + 1, fim)
    