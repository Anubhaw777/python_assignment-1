'''This program finds the number which are divisible by 7 and multiple of 5 between 15000 and 2000'''

#it finds the number divisible by 7 and multiple of 5 between 1500 and 2000

final=[num for num in range(1500,2001 )
       if num%7==0 and num%5==0]

#prints the result

print("the number divisible by 7 and multiple of 5 between 1500 and 2000 is ", final)

