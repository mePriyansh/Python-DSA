n=int(input("Enter the number of elements: "))
new_dict={}
for i in range(n):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    new_dict[key]=value
print(new_dict)