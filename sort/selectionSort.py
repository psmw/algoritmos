import random

def selectionSort(vec):
    for i in range(len(vec)):
        index = i
        for j in range(i+1, len(vec)):
            if vec[index] > vec[j]:
                index = j
        vec[i], vec[index] = vec[index], vec[i]
    print(vec)
    
randVector=[random.randint(1,100) for i in range(7)]

print(randVector)
selectionSort(randVector)