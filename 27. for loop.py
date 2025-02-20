#write a python program to print the multiplication table where the given by user using for loop

number = int(input("Enter a number to print its multiplication table: "))

print(f"Multiplication table for {number}:")

for i in range(1, 11):  
    result = number * i
    print(f"{number} x {i} = {result}")
