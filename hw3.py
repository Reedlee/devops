string = input("Введите текст, содержащий любые слова, слоги, числа или их комбинации, разделенные пробелом:\n")

array = string.lower().split(' ')
counter = {}
clear_string = ''
words = []
for word in array:
    if counter.get(word): 
        counter[word] += 1
        if len(words) == 0 or counter[words[-1]] == counter[word]:
            words.append(word)
        elif counter[words[-1]] > counter[word]:
            words = [word]
    else:
        counter[word] = 1

for word in words:
    print("{count} - {word}".format(count=counter[word], word=word))
