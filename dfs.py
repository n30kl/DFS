import time
import random
from multiprocessing.dummy import Pool as ThreadPool

def dfs(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path

while True:
    vertices = int(input("Enter graph size for 6 threads: "))
    graph = {}
    arc = int(vertices/10) 

    for x in range(vertices):
        graph[x] = [random.randint(0, vertices-1) for _ in range(arc)]       

    b = [graph, graph]
    c = [vertices-1, 0]

    pool = ThreadPool(10)
    start = time.monotonic()
    pool.starmap(dfs, zip(b, c))
    pool.close()
    pool.join()
    end = time.monotonic()

    #print(graph)
    #print(dfs(graph, 1))

    start = time.monotonic()
    dfs(graph, 1)
    end = time.monotonic()

    print('Elapsed time: ', round((end - start), 3), ' sec')

    print('')
