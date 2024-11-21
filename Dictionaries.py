# 1 Basic
# Create a dictionary with three Key-value Pairs
# Representing  a student's information; name,age,grade. 
# Print each Key-value pair on anew line
student_information = {
    "name":"Mariahbless",
    "age": 21,
    "grade":"Grade A"
}
print(student_information)

# Print each Key-value pair on anew line
for name in student_information:
 print(name)
#OR

name = student_information["name"]
print(name)
age = student_information["age"]
print(age)
grade = student_information["grade"]
print(grade)

# Intermediate: 
# Write a function that takes a dictionary of people's names and their ages,
#  {'Alice': 24, 'Bob': 19, 'Charlie': 30}, 
# and returns a list of names of people who are 21 or older.

people_and_their_ages = {
 "Alice":  24,
 "Bob": 19,
 "Charlie": 30
}
print(f" These are the names of people and their age{people_and_their_ages}")

for age in people_and_their_ages:
  print(age)
   


# Advanced:
# Given a dictionary representing items in a store with their prices,
#  {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, 
# write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], 
# and calculates the total cost.







# Challenge: 
# Write a program that counts the occurrences of each word in a given sentence. 
# Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.

def counting_occcurance(sentence):
  words = sentence.split()
  word_counting = {}

  for word in words:
    if word in word_counting:
      word_counting[word] +=1
    else:
      word_counting[word] = 1
      return word_counting
    sentence = "hello world hello"
    print(counting_occcurance(sentence))