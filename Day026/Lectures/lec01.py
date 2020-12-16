numbers = [1, 2, 3]

numbers_plus_one = [n + 1 for n in numbers]
print(numbers_plus_one)

name = "Angela"
letters = [letter for letter in name]
print(letters)

values = [num * 2 for num in range(1, 5)]
print(values)
print()

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)
