def binary_search(L,item):
    low=0
    high=len(L)-1
    medium=(low+high)//2
    while low <= high:
        if L[medium]<item:
            low=medium+1
        elif L[medium]>item:
            high=medium-1
        else:
            return medium
        print(medium)
        medium = (low + high) // 2
    return -1

L=[x*2 for x in range(10)]
a=3
print(L)
print(binary_search(L,a))