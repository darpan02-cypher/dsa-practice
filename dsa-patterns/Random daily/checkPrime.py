def checkPrime(num):
    if num <= 1: # Check if the number is less than or equal to 1, as prime numbers are greater than 1
        return False
    for i in range(2, int(num**0.5) + 1): # Check for factors from 2 to the square root of num , checking square root is enough because if num has a factor larger than its square root, it must also have a factor smaller than its square root. 
        #example: 36 has factors 1,2,3,4,6,9,12,18,36. The square root of 36 is 6. The factors less than or equal to 6 are 1,2,3,4,6. The factors greater than 6 are 9,12,18,36. If we check for factors up to the square root of num, we can find all the factors of num. This reduces the number of iterations and makes the algorithm more efficient.
        if num % i == 0:
            return False
        else:
            return True

# Example usage
number = 29
if checkPrime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")