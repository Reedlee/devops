string = input("Введите текст, содержащий любые слова, слоги, числа или их комбинации, разделенные пробелом:\n")

array = string.split(' ')
clear_dict = {}
clear_string = ''
for word in array:
    if not clear_dict.get(word): 
        clear_dict[word]=word

clear_string = ' '.join(clear_dict.keys())

print(clear_string)
