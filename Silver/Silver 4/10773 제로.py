t=int(input())
a=[]
count=0
for i in range(t):
    n=int(input())
    if n==0:
        a.pop()
    else:
        a.append(n)
        
for i in range(len(a)):
    count+=a[i]
    
print(count)