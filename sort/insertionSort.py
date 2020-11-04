import random

def insertionSort(vec):
    for i in range(1, len(vec)):
        comparisonValue = vec[i]
        j = i-1
        while j >= 0 and comparisonValue < vec[j]:
            vec[j+1] = vec[j]
            j -= 1
        vec[j+1] = comparisonValue
    print(vec)
        
    
randVector=[random.randint(1,100) for i in range(7)]

print(randVector)
insertionSort(randVector)