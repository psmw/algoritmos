import random

def bubbleSort(vec):
    control = True
    index = len(vec) - 1
    while index > 0 and control:
        control = False
        for i in range(index):
            if vec[i]>vec[i+1]:
                control = True
                aux = vec[i]
                vec[i] = vec[i+1]
                vec[i+1] = aux
        index = index - 1
    print(vec)
    
    
    
randVector=[random.randint(1,100000) for i in range(50)]

print(randVector)
bubbleSort(randVector)