#Creating empty dictionary using dict() function
dict1 = dict()
print(dict1)

#Creating empty dictionary using {}
dict2 = {}
print(dict2)
#Time complexity: O(1)
#Space complexity: O(1)

#Creating dictionary with key-value pairs
dict3 = {1: 'apple', 2: 'ball'}
print(dict3)

#Creating dictionary elements and dict()
dict4 = dict(f1='apple', f2='ball')
print(dict4)

#Creating dictionary with list of tuples
my_tuple=[(1, 'apple'), (2, 'ball')]
dict5 = dict(my_tuple)
print(dict5)
#Time complexity: O(n)
#Space complexity: O(n)