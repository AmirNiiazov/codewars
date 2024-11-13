def dig_pow(n, p):
    str_n = str(n)
    sum = 0
    for i in range(len(str_n)):
        sum += int(str_n[i]) ** (p+i)
    return -1 if sum % n != 0 else sum // n

print(dig_pow(46288, 3))