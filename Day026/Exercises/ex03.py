with open('file1.txt') as file:
    numbers1 = file.readlines()

with open('file2.txt') as file:
    numbers2 = file.readlines()

result = [int(number) for number in numbers1 if number in numbers2]
print(result)
