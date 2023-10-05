def bubble_sort (vetor):
    tamanho = (len(vetor) - 1)
    for i in range(tamanho,0,-1):
        for z in range(i):
            if vetor[z] > vetor[z+1]:
                valor_temporario = vetor[z]
                vetor[z] = vetor[z+1]
                vetor[z+1] = valor_temporario
    return vetor

vetor_atual = list(map(int,input().split()))
print(bubble_sort(vetor_atual))
