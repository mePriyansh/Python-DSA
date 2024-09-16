my_dict={'name':'Jack','age':26,'address':'Downtown','city':'New York'}

def search_dict(dict,search_for):
    for key in dict:
        if dict[key]==search_for:
            return key, dict[key]
    return "Not found"

print(search_dict(my_dict,26))
print(search_dict(my_dict,27))

#Time complexity: O(n)
#Space complexity: O(1)