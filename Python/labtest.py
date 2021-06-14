m1=[]
m2=[]
print("enter rowsize and coloumnsize of m1 ")
r1=int(input())
c1=int(input())
print("enter coloumnsize of m2 ")
c2=int(input())
for i in range(r1):         
    a =[]
    for j in range(c1):     
         a.append(int(input()))
    m1.append(a)
for i in range(c1):         
    b =[]
    for j in range(c2):     
         b.append(int(input()))
    m2.append(b)
r=[]
for i in range(r1):         
    c =[]
    for j in range(c2):     
         c.append(0)
    r.append(c)
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            r[i][j] += m1[i][k] * m2[k][j]
print(r)
