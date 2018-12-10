def convert_t(temp, scale_type = 'c'):
    if scale_type == 'c':
        converted_t = (temp*9/5)+32,2
    elif scale_type == 'f':
        converted_t = (temp-32)*5/9
    else:
        raise ValueError.new('Unknown temperature type. Should be "c" or "f"')
    return f'{round(converted_t,2)}{scale_type}'


print(convert_t(243,'f'))
