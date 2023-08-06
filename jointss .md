n=int(input())
ans=[0]*n
k=[]
for i in range(n):
    k=input()
    k=[str(j) for j in k]
    ans[i]=k[0]+''.join(k[1::2])
print('\n'.join(ans))
    
