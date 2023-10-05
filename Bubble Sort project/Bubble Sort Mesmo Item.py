import time
start_time = time.time()

def bubble_sort (vetor):
    tamanho = (len(vetor) - 1)
    for i in range(tamanho,0,-1):
        for z in range(i):
            if vetor[z] > vetor[z+1]:
                valor_temporario = vetor[z]
                vetor[z] = vetor[z+1]
                vetor[z+1] = valor_temporario
    return vetor

vetor_atual = [1,2,3,4,5,6,7,10,14,18]
print(vetor_atual)
print()
print(bubble_sort(vetor_atual))
end_time = time.time()
print()
print(f"The execution time is: {end_time-start_time}")
