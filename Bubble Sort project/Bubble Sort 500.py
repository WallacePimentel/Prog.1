import time
import random as rd
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

vetor500 = []
for i in range(500):
    vetor500.append(rd.randint(0,500))

print(vetor500)
print()
print(bubble_sort(vetor500))
end_time = time.time()
print()
print(f"The execution time is: {end_time-start_time}")
