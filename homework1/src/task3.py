# Task 3: Control Structures 

def is_positive(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "0"

def print_primes():
    count = 0
    number = 2
    primes = []

    while count < 10:
        is_prime = True
        
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        
        if is_prime == True:
            primes.append(number)
            count +=1

        number += 1
    
    for prime in primes:
        print(prime)

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