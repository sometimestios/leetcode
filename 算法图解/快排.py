def quick_sort(li,start,end):
    if start>=end:
        return
    left=start
    right=end
    mid=li[left]
    while left<right:
        while left<right and li[right]>=mid:
            right-=1
        li[left]=li[right]
        while left<right and li[left]<=mid:
            left+=1
        li[right]=li[left]
        li[left]=mid
        quick_sort(li,start,left-1)
        quick_sort(li, left+1,end)

def quick_sort2(li,left,right):
    if left<right:
        q=partion(li,left,right)
        quick_sort2(li,left,q-1)
        quick_sort2(li, q+1, right)
def partion(li,left,right):
    x=li[right]
    i=left-1
    for j in (left,right):
        if li[j]<=x:
            i+=1
            li[i],li[j]=li[j],li[i]
    li[i+1],li[right]=li[right],li[i+1]
    return i+1


l=[4,1,5,7,3,2,6]
quick_sort2(l,0,len(l)-1)
print(l)