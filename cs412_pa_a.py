"""
    name:  Samuel Snyder & Andrew Bailey
    
"""

from itertools import permutations


# 4
# 0 5 10 15
# 5 0 20 25
# 10 20 0 25
# 15 25 25 0


# matrix W, start at s
def exactTSP(W, s):
    perms = []
    nums = [n for n in range(len(W))]
    p = permutations(nums)
    for i in p:
        print(i)




def main():
    # input is a number n and an nXn matrix
    n = int(input())
    wMatrix = [[int(x) for x in input().split()] for _ in range(n)]
    print()
    print(exactTSP(wMatrix, 0)) 
    pass

if __name__ == "__main__":
    main()


