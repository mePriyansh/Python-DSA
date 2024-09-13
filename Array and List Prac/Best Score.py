'''
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList)
'''
def first_second(my_list):
    # TODO
    first,second=0,0
    for num in my_list:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num
    return first,second

#Time complexity: O(n)
#Space complexity: O(1)