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

vetor_atual = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
print(vetor_atual)
print()
print(bubble_sort(vetor_atual))
end_time = time.time()
print()
print(f"The execution time is: {end_time-start_time}")
