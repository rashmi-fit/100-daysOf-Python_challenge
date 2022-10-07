def ArrayChallenge(arr):
    expected=0
    arr=[-1] +arr
    arr.append(-1)
    n=len(arr)
    stack=[0]

    for i in range(n):
        while arr[i]<arr[stack[-1]]:
            h=arr[stack.pop()]
            area=h*(i-stack[-1]-1)
            expected=max(expected,area)
        stack.append(i)
    # code goes here
    return expected

# keep this function call here
print(ArrayChallenge(input()))
