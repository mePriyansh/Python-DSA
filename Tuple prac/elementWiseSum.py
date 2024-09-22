'''
Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

Example

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)
'''
#Method1 using for loop

def tuple_elementwise_sum(tuple1, tuple2):
    result=[]
    for i,j in zip(tuple1,tuple2):
        result.append(i+j)
    return(tuple(result))
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple) 

#Time complexity is O(n) where n is the length of the tuple
#Space complexity is O(n) where n is the length of the tuple

#Method2 using list comprehension
def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")
 
    result = tuple(a + b for a, b in zip(t1, t2))
    return result

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple) 

#Using map and sum  
def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")
 
    result = tuple(map(sum, zip(t1, t2)))
    return result
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple) 