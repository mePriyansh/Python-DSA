prev_list= [-3, -2, -1, 0, 1, 2, 3, 4, 5]
new_list=[x for x in prev_list if x>0]
print(new_list)

#List comprehension with if else
print("\nList comprehension with if else")
new_list1=[x*x for x in prev_list if x<0]
print(new_list1)

print("\nList comprehension with if else chanaged order")
newlist2 =[i if i%2==0 else i*2 for i in prev_list]
print(newlist2)

#Function to check if a letter is a consonant
sentence = "I love Python"

def isConsonant(letter):
    vowels='aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [x for x in sentence if isConsonant(x)]
print("\nConsonants in the sentence are:")
print(consonants)