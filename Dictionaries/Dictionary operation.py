#in/not in functions
my_dict = {2: 'apple', 
           4: 'ball',
           1: 'cat',
           3: 'dog'
           }
print(my_dict)
print("\n Check if Key 1 is present in my_dict: ")
print(1 in my_dict)
print("\n Check if Apple present in my_dict value: ")
print('apple' in my_dict.values())   

print("\nCheck if Key 5 is not present in my_dict: ")
print(5 not in my_dict)
print("\nCheck if Elephant is not present in my_dict value: ")
print('elephant' not in my_dict.values())

#len() function can be used to find the length of the dictionary
print("\nLength of my_dict: ", len(my_dict))

#sorted() function can be used to sort the dictionary
print("\nSorted my_dict: ", sorted(my_dict))

#all() function can be used to check if all the keys are True and returns True if all the keys are True else False
print("\nall() function")
print("Given dictionary")  
print(my_dict)
print("\nCheck if all keys are True in my_dict: ", all(my_dict))

print("\nnew dictionary")
my_dict1 = {1: 'apple', False: 'False', 3: 'cat', 4: 'dog'}
print(my_dict1)
print("\nCheck if all keys are True in my_dict: ", all(my_dict1))

print("\nnew dictionary")
my_dict2 = {0: 'abc'}
print(my_dict2)
print("\nCheck if all keys are True in my_dict: ", all(my_dict2))

#any() function can be used to check if any of the keys are True and returns True if any of the keys are True else False
print("\nany() function")
print("given dictionary")
print(my_dict)
print("\nCheck if any keys are True in my_dict: ", any(my_dict))