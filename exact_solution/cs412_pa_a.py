"""
    name:  Samuel Snyder & Andrew Bailey
    
    GeeksforGeeks was used in developing the strucutre for this project:
    https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/ 

"""

from itertools import permutations
import random


# matrix W, start at s
def exactTSP(edges, s):
    vertices = []
    for u, _ in edges:
        if u not in vertices:
            vertices.append(u)
    
    min = float('inf')
    # create permutations that represent paths in our graph
    perms = permutations(vertices)
    path = []
    for next in perms:
        if next[0] == s: # only start with s
            cycle = list(next)
            cycle.append(s) # append starting vertex to create a cycle
            weight = 0
            path = [s] 
            # construct the path/weight for the permutation
            for i in range(len(cycle) - 1):
                u, v = (cycle[i], cycle[i + 1])
                if (u, v) in edges:
                    weight += edges[(u, v)]
                    path.append(v)
            if weight < min:
                min = weight
                shortest_path = path
    # print output
    print(min)
    print(' '.join(shortest_path))


# utility function to create a new problem in the desired format
def problemGenerator(n):
    edges = dict()
    m = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                # ASCII a=97; z=122
                m += 1
                edges[(i, j)] = round(random.uniform(1.000, 1000.000), 3)
    # print in desired input format
    print(str(n) + " " + str(m))
    for u, v in edges:
        print(str(u) + " "+ str(v) + " " + str(edges[(u, v)]))


def main():
    # input is a number n and an nXn matrix
    _, e = [int(x) for x in input().split()]
    edges = dict()
    vertex_set = set()
    for _ in range(e):
        u, v, w = input().split()
        w = float(w)
        edges[(u, v)] = w
        edges[(v, u)] = w   
        vertex_set.add(u)
        vertex_set.add(v)
    
    start = list(vertex_set)[0]

    exactTSP(edges, start)
    # call this to create a test case
    # problemGenerator(8)

    pass

if __name__ == "__main__":
    main()


