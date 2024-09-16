my_dict={'name':'Jack','age':26,'address':'Downtown','degree':'MBA'}
print(my_dict)

# Deleting a key value pair using del
print("Deleting a key value pair using del")
del my_dict['name']
print(my_dict)

# Deleting a key value pair using pop
print("\nNew dictionary")
my_dict1={'name':'Jack','age':26,'address':'Downtown','degree':'MBA'}
print(my_dict1)
print("\nDeleting a key value pair using pop")
my_dict1.pop('age')
print(my_dict1)

# Deleting all key value pairs using popitem
print("\nNew dictionary")
my_dict2={'name':'Jack','age':26,'address':'Downtown','degree':'MBA'}
print(my_dict2)
print("\nDeleting all key value pairs using popitem")
my_dict2.popitem()
print(my_dict2)

#Time Complexity: O(1)
#Space Complexity: O(1)

#Deleting all key value pairs using clear
print("\nNew dictionary")
my_dict3={'name':'Jack','age':26,'address':'Downtown','degree':'MBA'}
print(my_dict3)
print("\nDeleting all key value pairs using clear")
my_dict3.clear()
print(my_dict3)

#Time Complexity: O(n)
#Space Complexity: O(1)