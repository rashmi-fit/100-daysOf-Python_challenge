'''binary search
l lower bound, u upper bound 
If the search value is smaller than list[mid] then change upper bound and (mid - 1) becomes new upper bound value.

If the search value is bigger than list[mid] then change lower bound and (mid + 1) becomes new lower bound value.
'''
position=0
def search(list,num):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==num:
            print("found")
            return mid
        else:
            if list[mid]<num:
                l=mid+1
            else:
                u=mid-1 
                # because you have to skip the value
    return False

list=[1,3,4,5,6,7,90,23,10000,56,4]
list.sort()
num=23
pos = search(list,num)
if pos:
    print("found at",pos)
else:
    print("not found")