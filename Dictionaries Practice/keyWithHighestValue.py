'''
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output:
b
'''

def max_value_key(my_dict):
    # TODO
    max=float("-inf")
    max_key=None
    for key in my_dict:
        if my_dict[key]>max:
            max=my_dict[key]
            max_key=key
    return(max_key)
my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key((my_dict)))

#Time complexity: O(n)
#Space complexity: O(1)

#Other way to solve this problem is by using max function
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)
my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key((my_dict)))