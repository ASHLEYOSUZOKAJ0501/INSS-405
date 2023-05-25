import random

def generate_random_numbers():
    random_numbers = []
    for _ in range(100):
        random_numbers.append(random.randint(1, 100))
    return random_numbers

def sort_number(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers

random_numbers = generate_random_numbers()
sorted_numbers = sort_number(random_numbers)

print("Random Numbers:", random_numbers)
print("Sorted Numbers:", sorted_numbers)
print("\nSorted Numbers:")
for number in sorted_numbers:
    print(number)

