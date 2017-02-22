N=int(input())
a=[]

a=list(map(int,input().split()))

sum=0
for i in range(N):
    sum=sum+a[i]
mean=round(sum/N,1)
print(mean)

a.sort()
if(N%2==0):
    median=round((a[int(N/2)]+a[int(N/2-1)])/2,1)
else:
    median=round(a[int(N/2)])
print(median)

count_a={}
max_crr=0
for i in range(N):
    max=(a.count(a[i]))
    if(max>max_crr):
        mode=a[i]
        max_crr=max
print(mode)
