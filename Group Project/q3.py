import random

def generate_random_integers():
    random_integers = []
    for _ in range(100):
        random_integers.append(random.randint(1, 100))
    return random_integers

def print_odd_values(numbers):
    numbers.sort()
    odd_values = [num for num in numbers if num % 2 != 0]
    print("Odd Values:", odd_values)

random_integers = generate_random_integers()
print("\nSorted Numbers:")
print_odd_values(random_integers)
