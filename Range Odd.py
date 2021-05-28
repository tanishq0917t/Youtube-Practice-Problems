a,b=list(map(int,input().split()))
if a%2==0: a+=1
while a<=b:
    print(a,end=" ")
    a+=2
