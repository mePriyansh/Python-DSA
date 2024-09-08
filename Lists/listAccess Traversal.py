#Create a list

shoppingList = ['Milk','Cheese','Butter']
print(shoppingList)

#Access the list elements
print(shoppingList[1])
print(shoppingList[-1])

#Check if milk is in the list
print('\nUsing in operator:')
print('Milk' in shoppingList)

#Traversal of list
print('\nTraversing the list:')
for i in shoppingList:
    print(i)
    
#Empty list
emptyList = []
print('\nEmpty list:',emptyList)