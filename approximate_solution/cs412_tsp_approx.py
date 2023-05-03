"""
    name:  Samuel Snyder & Andrew Bailey
    ChatGPT idea for nearestNeighbor was used for developing this implementation:
    GREEDY ALGORITHM FOR TRAVELING SALESMAN PROBLEM

"""
import random

def nearestNeighbor(tsp, vertex_set, start):
    unvisited = vertex_set.copy()
    tour = []
        
    current_vertex = start
    tour.append(current_vertex)
    unvisited.remove(current_vertex)
    
    while len(unvisited) > 0:
        next_vertex = None
        min_weight = float('inf')
        for v in unvisited:
            if (current_vertex, v) in tsp:
                if tsp[(current_vertex, v)] < min_weight:
                    min_weight = tsp[(current_vertex, v)]
                    next_vertex = v
        tour.append(next_vertex)
        unvisited.remove(next_vertex)
        current_vertex = next_vertex
        
    # complete the cycle
    tour.append(start)
    # add the starting vertex to the end of the tour
    total_weight = sum([tsp[(tour[i], tour[i+1])] for i in range(len(tour) - 1)])
    return tour, total_weight

    
def main():
    # input is a number n and an nXn matrix
    _, e = [int(x) for x in input().split()]
    tsp = dict()
    vertex_set = set()
    for _ in range(e):
        u, v, w = input().split()
        tsp[(u, v)] = float(w)
        tsp[(v, u)] = float(w)
        vertex_set.add(u)
        vertex_set.add(v)
    
    # choose our random start point
    approximation = None
    length = None
    
    # random start point
    for i in range(100):
        start = random.choice(list(vertex_set))
        tour, weight = nearestNeighbor(tsp, vertex_set, start)
        if length == None or weight < length:
            length = weight
            approximation = tour

    print((length))
    print(' '.join(approximation))
    
if __name__ == "__main__":
    main()