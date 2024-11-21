# Loops
# Basic: 
# Write a Python program that prints all even numbers between 1 and 20 using a for loop.
def even():
 numbers = (1,21)
for num in range (1,21):
    if num % 2 == 0:
        print(num)
even()

# Intermediate: 
# Use a while loop to ask the user to input a number until they provide a number greater than 10.
numb = 0
numb <= 10
numb = int(input(f" Enter the number greater than 10"))
if numb <= 10:
    print("The number should be greater than 10, try again") 
else:
    print("Invalid entered value,enter the valid number")

# Advanced: 
# Write a program that prints the multiplication table (from 1 to 10) 
# for numbers from 1 to 5 using nested for loops.2

for row in range (1,6):
    print(f"{row:3} |", end='')
for col in range (1,11):
    print(f"{row*col:4}",end='')





# Challenge: 
# Given a list of integers, [4, 7, 2, 9, 12, 15], 
# write a program using a for loop to find the sum of all odd numbers and print the result.

numbers = [4,7,2,9,12,15]
sum_of_odd_numbers = 0

for num in numbers:
    if num % 2 != 0:
        sum_of_odd_numbers += num
        print(f" The sum of all odd numbers is ", sum_of_odd_numbers)