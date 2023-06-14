import random

def generate_random_number():
    return random.randint(1, 100)

def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def calculate_fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    random_number = generate_random_number()
    print("Generated random number:", random_number)

    if is_prime_number(random_number):
        print("The number is prime!")
    else:
        print("The number is not prime.")

    fibonacci_sequence = calculate_fibonacci_sequence(random_number)
    print("Fibonacci sequence of length", random_number, ":", fibonacci_sequence)

if __name__ == "__main__":
    main()
