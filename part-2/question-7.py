'''program that accepts string and calculates the num of digit and letters'''

# ask string input from the user

a=input("Enter any string ")

#initialize counter
letter_count =0
digit_count=0

for char in a:
    if char.isalpha():
        letter_count +=1
    elif char.isdigit():
        digit_count+=1

#prints the result
print("The number of letters are",letter_count)
print("The number of digits are ", digit_count)
