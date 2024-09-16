my_dict=dict(name='Jack',age=26,address='Downtown')

#Traversing a dictionary
def traverse_dict(dict):
    for key in dict:
        print(key, dict[key])

traverse_dict(my_dict)