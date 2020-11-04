import random

def selectionSort(vec):
    for i in range(len(vec)):
        aux1 = i
        for j in range(i+1, len(vec)):
            if vec[aux1] > vec[j]:
                aux1 = j
        vec[i], vec[aux1] = vec[aux1], vec[i]
    print(vec)
    
randVector=[random.randint(1,100000) for i in range(50)]

print(randVector)
selectionSort(randVector)