while 1:
    cancel = input()
    if cancel == 'cancel':
        break
    else:
        try:
            num = int(cancel)
            if num % 2 == 0:
                print(num/2)
            else:
                print(num*3+1)
        except(ValueError):
            print('Не удалось преобразовать введенный текст в число.')
