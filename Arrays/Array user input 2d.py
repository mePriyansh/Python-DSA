row=int(input("Rows:"))
col=int(input("Col:"))
lst=[]
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    lst.append(a)
    
print(lst)