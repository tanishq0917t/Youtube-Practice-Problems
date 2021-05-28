n=int(input())
a=10
b=2
for i in range(n):
    if i%2==0:
        print(a,end=" ")
        a+=10
    else:
        print(b,end=" ")
        b+=2
