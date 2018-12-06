def calc_number(number):
    if number % 2 == 0:
        number = number/2
    else:
        number = number*3+1
    print(number)
    return number

string = input()
print(f"Для числа {string}:\n")
number = int(string)
counter = 0
while number != 1:
   number = calc_number(number)
   counter += 1

print(f"Всего получаем {counter} шагов.")
