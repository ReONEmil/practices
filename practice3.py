"""

Number Pattern Printer: Write a program that prints a number pattern where each row contains
numbers from 1 to that row number. For example:
Copy code
1
1 2
1 2 3
1 2 3 4
Use a while loop with break to limit the number of rows printed.


"""



numberof_row = int(input())

row = 1
while True:
    if row > numberof_row:  
        break
    for num in range(1, row + 1):
        print(num, end =" ")
    print()

    row += 1


row = numberof_row - 1
while True:
    if row == 0:
        break
    for num in range(1, row + 1):
        print(num, end = " ")
    print()
    row -= 1