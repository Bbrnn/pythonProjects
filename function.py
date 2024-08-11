def shorten_number(number):
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return str(number // 1000) + 'K'
    elif number < 1000000000:
        return str(number // 1000000) + 'M'
    else:
        return str(number // 1000000000) + 'B'

print(shorten_number(1000000))
print(shorten_number(900))
print(shorten_number(50000000000))
