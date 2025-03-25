''' ask two number and display 1st divided by second with 2 decimal places'''

#taking user input
a=int(input("Enter first number "))
b=int(input("Enter second number "))

#applying condition
if b==0:
    print(" Error: 0 is not allowed ")
else:
    result=a/b
    print( f"result is: {result:.2f}" )
