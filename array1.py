n=int(input())
m=int(input())
r=[]
for i in range(n):
    k=int(input())
    r.append(k)
for j in range((len(r)-1)):
    if r[1+j]-r[j]>m:
       print("1")
    if len(r)%2!=0:
        if r[0]-r[len(r)-1]>m:
            print("1")
        else:
            print("0")
    else:
       print("0")
    
    
