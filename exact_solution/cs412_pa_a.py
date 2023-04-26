"""
    name:  Samuel Snyder & Andrew Bailey
    
    GeeksforGeeks was used in developing the strucutre for this project:
    https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/ 

"""

from itertools import permutations


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


def main():
    # input is a number n and an nXn matrix
    n, e = [int(x) for x in input().split()]
    edges = dict()
    for _ in range(e):
        u, v, w = input().split()
        w = int(w)
        edges[(u, v)] = w
        edges[(v, u)] = w   
    print(edges)

    print()
    exactTSP(edges, "a") 
    pass

if __name__ == "__main__":
    main()


