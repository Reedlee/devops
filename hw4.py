import re
string = input("Введите неотрицательные цифры, разделенные не цифровым литералом:\n")

string = string.lower()
string = re.sub(r'\-\-', '-', string)
string = re.sub(r'\-', ' -', string)
string = re.sub(r'[^\-\d]', ' ', string)
arr = string.split(' ')

counter = 0
for digit in arr:
    if len(digit) > 0: 
        counter += int(digit)

print(counter)
