import numchecker


def get_float(text, repeat=True, non_zero=False, positive=False):
    while repeat:
        num = numchecker.make_float(input(text))
        if num is None:
            print('Input value must be a number')
        elif non_zero and num == 0:
            print('Input value cannot be zero')
        elif positive and num <= 0:
            print('Input value must be positive')
        else:
            return num


def get_int(text, repeat=True, non_zero=False, positive=False, min_n=float('-inf'), max_n=float('inf')):
    while repeat:
        num = numchecker.make_integer(input(text))
        if num is None:
            print('Input value must be an integer')
        elif non_zero and num == 0:
            print('Input value cannot be zero')
        elif positive and num <= 0:
            print('Input value must be positive')
        else:
            return num


def get_string(text, repeat=True, non_zero=True):
    string = ''
    while repeat:
        string = input(text)
        if len(string) == 0 and non_zero:
            continue
        break
    return string.strip()
