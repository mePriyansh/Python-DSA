my_list=[10,20,30,40,50,60,70,80,90,100]

# Search for the value using in operator
target=30
if target in my_list:
    print(f'{target} found in the list')
else:
    print(f'{target} not found in the list')
    
#Time complexity : O(n)
#Space complexity : O(1)

# Search for the value using linear search
def linear_search(my_list,n_target):
    for i in range(len(my_list)):
        if my_list[i]==n_target:
            return i
    return -1

n_target=35
index=linear_search(my_list,n_target)
if index==-1:
    print(f'{n_target} not found in the list')
    
#Time complexity : O(n)
#Space complexity : O(1)