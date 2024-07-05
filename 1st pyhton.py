def solve(s1,l):
    count=0
    for x in range(l):
        for y in range(l):
            if s1[x][0]==s1[y][1]:
                count=count+1
    print(count)
            
i=int(input(""))
s1= [[0 for _ in range(2)] for _ in range(i)] #col frist after write for row
# print(s1)
for j in range(i):
    a,b=input("").split()
    s1[j][0],s1[j][1]=a,b
solve(s1)