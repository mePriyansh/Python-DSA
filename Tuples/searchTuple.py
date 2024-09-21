newTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#in() operator
print(5 in newTuple)
print(11 in newTuple)

#index() method
print("Index method()")
print(newTuple.index(5))

#Using functions
print("Using functions")
def searchTuple(tuple, element):
    for i in tuple:
        if i == element:
            return f"Element {element} found at index {tuple.index(i)}"
    return "Element not found"
print(searchTuple(newTuple, 6))