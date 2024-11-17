
def disemvowel(string_):
    return string_.translate({ord(i): None for i in 'euioaEIOUA'})