n=int(input())
check=99
if n<100:
    print(n)
else:
    for i in range(100,n+1):
        a=i//100; b=(i%100-i%10)//10; c=i%10
        if (b-a)==(c-b):
            check+=1
    print(check)