def open_or_senior(data):
    return [['Open', 'Senior'][i[0] >= 55 and i[1] > 7] for i in data]

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))