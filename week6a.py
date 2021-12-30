l=[]
m=[]
p=[]
o=[]
data=[]
n=int(input("Enter the range of list :"))
print("Enter elements in list")
for i in range(0,n):
    a=input("Enter name:")
    b=input("Enter roll no :")
    c=input("Enter branch :")
    d=input("Enter age : ")
    l.append(a)
    m.append(b)
    p.append(c)
    o.append(d)
for i in range(0,n):
    data.append(l[i]+" "+m[i]+" "+p[i]+" "+o[i])
data.sort()
print("After sorting by name is :")
for i in range(0,n):
    print(data[i])
