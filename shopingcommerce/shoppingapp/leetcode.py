n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=a[n-1]-a[0]-1
a.remove(a[n-1])
a.remove(a[0])
print(ans-len(a))
