import collections

#graph to be searched through
graph = {
    'a':['b','c'],
    'b':['d','e'],
    'c':['f','g'],
    'd':[],
    'e':['h'],
    'f':[],
    'g':[],
    'h':[],
}

#bsf search algorithm. Takes in the graph and the starting node
def bsf(g, root):
    queue = collections.deque([root])
    visited = []
    #while there is stuff in the queue, take the first item in the queue and add it to list of visited nodes if it isnt in their already.
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print(node)
        for item in g[node]:
            if item not in visited:
                queue.append(item)
        

bsf(graph, 'a')