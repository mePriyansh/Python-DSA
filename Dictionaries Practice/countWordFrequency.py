'''
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output:

 {'apple': 3, 'orange': 2, 'banana': 1}
'''
def count_word_frequency(words):
    word_count={}
    for word in words:
        word_count[word]=word_count.get(word,0)+1
    return word_count

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))

#Other way to solve the problem
def count_word_frequency(words):
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))

#Time complexity: O(n)
#Space complexity: O(n)