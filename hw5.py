string = input("Введите неотрицательные целые числа, разделенные пробелом:\n")

string = string.lower()
arr = string.split(' ')
sorted_uniq_numbers = set(map(int, arr))
numbers = list(sorted_uniq_numbers)
first_number = numbers[0] - 1

for number in numbers:
    first_number += 1 
    
    if first_number < number:
        minimum =  first_number
        break
print(minimum)
