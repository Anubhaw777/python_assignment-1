'''program takes input from user and calculates the simple interest'''
# Taking user input
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of Interest (per annum): "))
T = float(input("Enter the Time period (in years): "))

# Calculating Simple Interest
SI = (P * R * T) / 100

# Displaying the result
print(f"Simple Interest for Principal {P}, Rate {R}%, and Time {T} years is: {SI:.2f}")
