# Lists
# Basic:
#  Create a list of 5 fruits and print each fruit on a new line using a for loop.
fruits = ["Apple", "Pineapple", "Watermelon","Banana", "Passionfruit"]
for fruit in fruits:
    print(f"The five fruits are {fruits}")


# Intermediate: 
# Write a function that takes a list of numbers and returns a new list with each number squared. 
# Example: [1, 2, 3] should become [1, 4, 9].

def square_numbas(numbas):
 return[n**2 for n in numbas]
numbas = [1,2,3]
squared_numbas = (numbas)



# Advanced: 
# Write a Python program that takes two lists, 
# list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, 
# combined = [1, 4, 2, 5, 3, 6].

List1 = [1,2,3]
List2 = [4,5,6]
combined_list = List1 + List2
print(combined_list)


# Challenge: 
# Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], 
# write a program to find and print the two largest numbers in the list without using the max() function.

def largest_two_numbers(numbs):
   largest = float('-inf')
   second_largest = float('-inf')
   for num in numbs:
      if num > largest:
         second_largest = largest
         largest = num
      elif num > second_largest and num != largest:
         second_largest = num
         return largest,second_largest
numbs = [3,1,4,1,5,9,2]
print("Largest:")
print("Second largest:")