"""
    name:  Sam Snyder & Andrew Bailey
    
"""

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