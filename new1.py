import math
# Function to check if a number is prime or not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to find the smallest prime p
def find_smallest_prime(input_numbers):
    n = len(input_numbers) - 1
    q = min(input_numbers)
    p = q

    while True:
        divisible = True
        for x in input_numbers:
            if x != q and (p % x) != q:
                divisible = False
                break

        if divisible and is_prime(p):
            return p

        p += 1
input_str = input("Enter n+1 distinct natural numbers separated by spaces: ")
input_numbers = list(map(int, input_str.split()))

resultp = find_smallest_prime(input_numbers)

if resultp is not None:
    print("The smallest prime 'p' is:", result)
else:
    print("none")
