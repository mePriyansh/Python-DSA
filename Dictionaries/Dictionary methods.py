my_dict={'name':'Jack','age':26,'address':'Downtown','degree':'Masters'}
print(my_dict)

#copy() method creates a shallow copy of the dictionary
print("Copy method")
new_dict=my_dict.copy()
print(new_dict)

#fromkeys() method creates a new dictionary with keys from the given sequence
print("\nFromkeys method")
dict1=dict.fromkeys(['name','age','address','degree'])
print(dict1)

#get() method returns the value of the specified key
print("\nGet method")
print(my_dict.get('name'))


#items() method returns a view object that displays a list of a dictionary's key-value tuple pairs
print("\nItems method")
print(my_dict.items())

#keys() method returns a view object that displays a list of all the keys in the dictionary
print("\nKeys method")
print(my_dict.keys())

#values() method returns a view object that displays a list of all the values in the dictionary
print("\nValues method")
print(my_dict.values())

#setdefault() method returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print("\nSetdefault method")
print(my_dict.setdefault('name','John'))

#update() method updates the dictionary with the specified key-value pairs
print("\nUpdate method")
dict1={'name':'John'}
my_dict.update(dict1)
print(my_dict)