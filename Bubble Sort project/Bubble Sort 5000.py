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

vetor5000 = []
for i in range(5000):
    vetor5000.append(rd.randint(0,5000))

print(vetor5000)
print()
print(bubble_sort(vetor5000))
end_time = time.time()
print()
print(f"The execution time is: {end_time-start_time}")
