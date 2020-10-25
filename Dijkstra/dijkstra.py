grafo={'a':{'b':1,'c':3,'d':5},'b':{'c':1,'d':1,'e':5,'f':8},'c':{'d':1,'e':3},'d':{'e':1,'f':7},
'e':{'b':6,'f':1},'f':{}}

def dijkstra(vec,inicio,fim):
    dist_menor = {}
    aux = {}
    graph = vec
    inf = float('inf')
    caminho_menor = []
    for i in graph:
        dist_menor[i] = inf
    dist_menor[inicio] = 0
    print('vec menor distancia no inicio do loop: ' + str(dist_menor))

    while graph:
        caminho = None
        for i in graph:
            if caminho is None:
                caminho = i
            elif dist_menor[i]<dist_menor[caminho]:
                caminho = i
        for j,k in vec[caminho].items():
            if k + dist_menor[caminho]<dist_menor[j]:
                dist_menor[j] = k + dist_menor[caminho]
                aux[j] = caminho
        graph.pop(caminho)

    aux2 = fim
    while aux2 != inicio:
        try:
            caminho_menor.insert(0,aux2)
            aux2 = aux[aux2]
        except KeyError:
            print('erro')
            break

    caminho_menor.insert(0,inicio)

    if dist_menor[fim] != inf:
        print('menor distancia ' + str(dist_menor[fim]))
        print('caminho tomado ' + str(caminho_menor))

dijkstra(grafo,'a','f')
