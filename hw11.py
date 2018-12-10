def letters_range(start, stop, step=1):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    idx_start = alphabet.index(start)
    idx_finish = alphabet.index(stop)
    stack = []
    for idx in range(idx_start, idx_finish, step):
        stack.append(alphabet[idx])

    return stack

print(letters_range('b', 'w', 2 ) == ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v'])
print(letters_range('a', 'g') == ['a', 'b', 'c', 'd', 'e', 'f'])
print(letters_range('g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'])
print(letters_range('p', 'g', -2) == ['p', 'n', 'l', 'j', 'h'])
print(letters_range('a','a') == [])

