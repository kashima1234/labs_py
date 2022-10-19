# A function that returns a numeric value if the argument
# can be represented as a number, otherwise - None

def make_float(str_value):
    if str_value is None:
        return None
    if len(str_value) == 0:
        return None
    is_float = True
    num_ended = False
    num_started = False
    e_counter = 0
    e_id = 0
    point_counter = 0
    sign_counter = 0
    for i in range(0, len(str_value)):
        ch = str_value[i]
        if not num_ended:
            if ch.isdigit():
                num_started = True
                if point_counter == 1 and e_counter == 0:
                    is_float = True
                if i == e_id + 1 or i == e_id + 2 and e_counter == 1:
                    is_float = True
            elif i == e_id + 1 and e_counter == 1 and i != len(str_value)-1:
                if ch == '-' or ch == '+':
                    continue
            elif not num_started and (ch == '-' or ch == '+') and \
                    sign_counter == 0 and i != len(str_value)-1:
                sign_counter += 1
            elif ch == '.':
                if not num_started:
                    is_float = False
                if point_counter == 0 and e_counter == 0:
                    point_counter += 1
                else:
                    return None
            elif ch == 'e':
                if e_counter == 0 and num_started and is_float:
                    is_float = False
                    e_id = i
                    e_counter += 1
                else:
                    return None
            elif not ch.isprintable() or ch == ' ':
                if not num_started:
                    if i != len(str_value)-1:
                        continue
                    else:
                        return None
                elif not num_ended:
                    num_ended = True
                else:
                    return None
            else:
                return None
        elif not ch.isprintable() or ch == ' ':
            continue
        else:
            return None

    if is_float:
        if float(str_value) == int(float(str_value)):
            return int(float(str_value))
        return float(str_value)
    return None


# A function that returns an integer value if the argument
# can be represented as an integer, otherwise - None
def make_integer(str_value):
    integer = make_float(str_value)
    if integer is not None and integer % 1 == 0:
        return int(integer)
    else:
        return None
