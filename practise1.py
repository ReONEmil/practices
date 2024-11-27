"""



Prime Number Finder: Develop a program that prompts the user to enter a number and checks
if it is a prime number. If the number is not prime, display its factors. Use a while loop with
break to exit the loop when the factors are 



"""

number = int(input())

if number < 2:
    print(f"{number} is not a prime number")
else:
    i = 2
    is_prime = True
    factors = []


    while i <= number // 2:
        if number % i == 0:
            is_prime = False
            factors.append(i)
            break
        i += 1
    

    if is_prime:
        print(f"{number} is a prime number")

    else:
        factors = [i for i in range(1, number + 1) if number % i == 0]

        print(f"{number} is not a prime number")
        print(f"Factors are:", factors)