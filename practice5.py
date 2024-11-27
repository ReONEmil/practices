"""

Even Number Generator: Develop a program that generates even numbers starting from 2 up
to a user-specied limit. Use a while loop to continuously generate even numbers until the limit
is reached, using continue to skip odd numbers.

"""

limit = int(input("Enter the limit: "))

number = 2

print("Even numbers until the ", limit, "are:")

while number <= limit:
    if number % 2 != 0:
        number += 1
        continue
    
    print(number, end=" ")
    
    number += 1
