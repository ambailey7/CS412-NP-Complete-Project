"""
    name:  Samuel Snyder & Andrew Bailey
    Hein de Haan's solution for TPS using the hill climbing algorithm was used for developing this implementation:
    https://towardsdatascience.com/how-to-implement-the-hill-climbing-algorithm-in-python-1c65c29469de

"""

import random

def randomSolution(tsp):
    cities = []
    for u, _ in tsp:
        if u not in cities and u != 'a':
            cities.append(u)
    solution = ['a'] # always start with 'a'
    numCities = len(cities) # nubmer of cities, not including 'a'
    
    for i in range(numCities):
        city = random.choice(cities)
        solution.append(city)
        cities.remove(city) # no repeat cities
    solution.append('a') # complete the cycle
    
    return solution


def getNeighbors(solution):
    neighbors = []
    for i in range(1, len(solution) - 1):
        for j in range(i + 1, len(solution) - 1):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
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


def hillClimbing(tsp):
    currSolution = randomSolution(tsp) # initial solution
    currLength = calculate(tsp, currSolution)
    neighbors = getNeighbors(currSolution)
    bestNeighbor, bestLength = getBestNeighbor(tsp, neighbors)
    
    while bestLength < currLength:
        currSolution = bestNeighbor
        currLength = bestLength
        neighbors = getNeighbors(currSolution)
        bestNeighbor, bestLength = getBestNeighbor(tsp, neighbors)
    
    return currSolution, currLength


def main():
    # input is a number n and an nXn matrix
    _, e = [int(x) for x in input().split()]
    tsp = dict()
    for _ in range(e):
        u, v, w = input().split()
        w = int(w)
        tsp[(u, v)] = w
        tsp[(v, u)] = w   
    
    print()
    print("Running 100 Iterations:")

    bestSolution = None
    bestLength = None
    # Run n number of iterations
    # the shortest solution is closest to the global minimum
    for _ in range(100):
        solution, length = hillClimbing(tsp)
        if bestLength == None or length < bestLength:
            bestLength = length
            bestSolution = solution
    
    print()
    print("Best solution:")
    print(bestLength)
    print(' '.join(bestSolution))

    pass

if __name__ == "__main__":
    main()
