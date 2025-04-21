def binary_search(length,target,low=None,high=None):
    if low is None:
        low=0
    if high is None:
        high=len(length)-1

    midpoint=(low+high)//2

    if length[midpoint] == target:
        return midpoint

    elif target < length[midpoint]:

        return binary_search(length,target,low,midpoint-1)
    else:
        return  binary_search(length,target,midpoint+1,low)

length=[1,2,3,4,5,6,7,8,9,10,11,12]
target=10
print("Bineary seaarch index number is :",binary_search(length,target))