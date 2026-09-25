# Task 3: Control Structures 

# checks if a number is positive, negative, or 0
def is_positive(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "0"

# determines if a number is prime and prints the first 10 positive prime numbers
def print_primes():
    count = 0
    number = 2
    primes = []

    while count < 10:
        is_prime = True
        
        # determine if number is prime
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        
        # if prime, add to the list of primes
        if is_prime == True:
            primes.append(number)
            count +=1

        number += 1
    
    # print all the prime numbers in the list
    for prime in primes:
        print(prime)

# calculate the sum from 1 to 100 and print it
def print_hundred_sum():
    total = 0
    number = 1

    while number <= 100:
        total += number # add to each number to total sum
        number += 1 # increment current number

    print(total)

def main():
    my_number = 1
    other_number = -1
    zero_number = 0

    print(f"{my_number} is {is_positive(my_number)}")
    print(f"{other_number} is {is_positive(other_number)}")
    print(f"{zero_number} is {is_positive(zero_number)}")

    print ("-------------------")
    print_primes()

    print ("-------------------")
    print_hundred_sum()

if __name__ == "__main__":
    main()