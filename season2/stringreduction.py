def StringChallenge(strParam):
    n=len(strParam)
    cnt1, cnt2, cnt3=0 ,0 ,0
    for i in range(0,n):
        if(strParam[i]=='a'):
            cnt1+=1
        elif(strParam[i]=='b'):
            cnt2+=1
        else:
            cnt3+=1

    if(cnt1 ==n or cnt2==n or cnt3==n):
        return n
    elif(cnt1%2==0 and cnt2%2==0 and cnt3%2==0):
        return 2
    elif(cnt1%2!=0 and cnt2%2!=0 and cnt3%2!=0):
        return 2
    else:
        return 1

print(StringChallenge("cccc"))