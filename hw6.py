number = input("Введите целое число:\n")
is_palindrome_base_10  = (number == number[::-1])
binary = bin(int(number))
binary = binary[2:] 
is_pandrome_base_2 =  (binary == binary[-1::-1])

is_palindrome = is_palindrome_base_10 & is_pandrome_base_2

print(f"Это полный палидром? {is_palindrome}")
