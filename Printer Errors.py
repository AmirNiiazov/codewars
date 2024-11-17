from string import ascii_lowercase


def printer_error(s):
    return f"{s.translate({ord(i): '$' for i in ascii_lowercase[13:]}).count('$')}/{len(s)}"


print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
