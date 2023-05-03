"""
    name:  Samuel Snyder & Andrew Bailey
    Hein de Haan's solution for TPS using the hill climbing algorithm was used for developing this implementation:
    https://towardsdatascience.com/how-to-implement-the-hill-climbing-algorithm-in-python-1c65c29469de

"""

import random

def randomSolution(vertices, s):
    solution = [s]
    num = len(vertices) - 1 # minus s
    v = vertices.copy()
    v.remove(s)
    v = list(v)
    for _ in range(num):
        choice = random.choice(v)
        solution.append(choice)
        v.remove(choice)
    solution.append(s)

    return solution


def getNeighbors(solution):
    neighbors = []
    for i in range(1, len(solution) - 1):
        neighbor = solution.copy()
        neighbor[i], neighbor[i+1] = neighbor[i+1], neighbor[i]
        neighbors.append(neighbor)
    return neighbors


def calculate(tsp, solution):
    length = 0
    for i in range(1, len(solution)):
        length += tsp[(solution[i - 1], solution[i])]
    return length


def getBestNeighbor(tsp, neighbors):
    bestLength = calculate(tsp, neighbors[0])
    bestNeighbor = neighbors[0]
    for neighbor in neighbors:
        length = calculate(tsp, neighbor)
        if length < bestLength:
            bestLength = length
            bestNeighbor = neighbor
    return bestNeighbor, bestLength


def hillClimbing(tsp, vertices, s):
    currSolution = randomSolution(vertices, s) # initial solution
    currLength = calculate(tsp, currSolution)
    print("here-1")
    neighbors = getNeighbors(currSolution)
    print("here")
    bestNeighbor, bestLength = getBestNeighbor(tsp, neighbors)
    print("here2")
    i = 0
    while bestLength < currLength:
        currSolution = bestNeighbor
        currLength = bestLength
        neighbors = getNeighbors(currSolution)
        bestNeighbor, bestLength = getBestNeighbor(tsp, neighbors)
        i += 1
        print(i)
        print("bestLength: ", bestLength)
    
    return currSolution, currLength


def main():
    # input is a number n and an nXn matrix
    _, e = [int(x) for x in input().split()]
    tsp = dict()
    vertex_set = set()
    for _ in range(e):
        u, v, w = input().split()
        w = float(w)
        tsp[(u, v)] = w
        tsp[(v, u)] = w
        vertex_set.add(u)
        vertex_set.add(v)
    
    # choose our random start point
    start = list(vertex_set)[0]
    print(start)
    bestSolution = None
    bestLength = None
    # Run n number of iterations
    # the shortest solution is closest to the global minimum
    for _ in range(1):
        solution, length = hillClimbing(tsp, vertex_set, start)
        if bestLength == None or length < bestLength:
            bestLength = length
            bestSolution = solution

    print(bestLength)
    print(' '.join(bestSolution))

    pass

if __name__ == "__main__":
    main()
