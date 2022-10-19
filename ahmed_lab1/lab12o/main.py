#ИУ7-13Б Оюунтуяа Одбаясгалан
#Lab 12
import ioformat
import numchecker
import traceback


bad_symbols = '/\\:*?"<>|+'
current_path = None
epsilon = 1e-10
print_width = 12


def calculate_max_length(data_base):
    global print_width
    print_width = 12
    for line in data_base:
        values = list(line)
        print_width = max(print_width, len(values[0]), len(values[2]))


def get_extension(file_path):
    extension = ''
    for i in range(len(file_path)-1, -1, -1):
        char = file_path[i]
        if char != '.':
            extension = char + extension
            continue
        break
    return extension


def pretty_print(*values):
    safe_open(current_path, 'r', calculate_max_length)
    if values is tuple():
        str_value = '{0:^{3:}} {1:^{3:}} {2:^{3:}}'.format('Name', 'Value', 'Type', print_width)
        print(str_value)
    elif len(*values) == 3:
        tmp_num = numchecker.make_float(values[0][1])
        str_value = '{0:^{3:}} {1:^{3:}.4g} {2:^{3:}}'.format(values[0][0], tmp_num, values[0][2], print_width)
        print(str_value)


def add_record(data_base):
    values = [None] * 3
    values[0] = ioformat.get_string('Enter the value of the first field (name): ')
    values[1] = str(ioformat.get_float('Enter the value of the second field (price): '))
    values[2] = ioformat.get_string('Enter the value of the third field (type): ')
    for element in values:
        if element is None or len(element) == 0:
            print('Input error: not all fields are filled')
            return
    str_v = ' '.join(values)
    data_base.write(str_v + '\n')


def create_file(file_path):
    if safe_open(file_path, 'r'):
        ans = ''
        while ans not in ['Д', 'Н']:
            ans = input('The file already exists. Overwrite? Д/Н: ').upper()
            if ans == 'Н':
                print('Operation aborted by user')
                return
    safe_open(file_path, 'w', print('File created'))


def field_search(data_base, num_of_fields):
    def matches(value, key):
        if type(key) == str:
            if value == key:
                return True
        else:
            if abs(float(value) - key) < epsilon:
                return True
        return False

    def get_field(column):
        res = ''
        if column == 1:
            res = input('Enter the value of the first field (name): ').strip()
        elif column == 2:
            res = ioformat.get_float('Enter the value of the second field (value): ')
        elif column == 3:
            res = input('Enter the value of the third field (type): ').strip()
        print()
        return res

    num = num_of_fields[0]
    if num == 1:
        column = ioformat.get_int('Enter attribute column number: ')
        if 1 <= column <= 3:
            key = get_field(column)
        else:
            print('Column not found')
            return
        if key is None or ((type(key) == str) and len(key) == 0):
            print('Empty filter introduced')
            return

        counter = 0
        print()
        print('Searching results:')
        for line in data_base:
            values = list(line.split())
            if (len(values) == 3) and (type(values[0]) == type(values[2]) == str) and (numchecker.make_float(values[1]) is not None):
                if matches(values[column - 1], key):
                    if counter == 0:
                        pretty_print()
                    pretty_print(values)
                    counter += 1
        if counter == 0:
            print('No matches found')

    elif num == 2:
        column_1 = ioformat.get_int('Enter the number of the first attribute column: ')
        if 1 <= column_1 <= 3:
            key_1 = get_field(column_1)
        else:
            print('Column not found')
            return
        if key_1 is None or ((type(key_1) == str) and len(key_1) == 0):
            print('Empty filter introduced')
        while True:
            column_2 = ioformat.get_int('Enter the number of the second attribute column: ')
            if column_2 == column_1:
                print('The second column must be different from the first')
                continue
            if 1 <= column_2 <= 3:
                key_2 = get_field(column_2)
            else:
                print('Column not found')
                return
            if key_2 is None or ((type(key_2) == str) and len(key_2) == 0):
                print('Empty filter introduced')
            break

        counter = 0
        print()
        print('Searching results:')
        for line in data_base:
            values = list(line.split())
            if (len(values) == 3) and (type(values[0]) == type(values[2]) == str) and (numchecker.make_float(values[1]) is not None):
                if matches(values[column_1 - 1], key_1) and matches(values[column_2 - 1], key_2):
                    if counter == 0:
                        pretty_print()
                    pretty_print(values)
                    counter += 1
        if counter == 0:
            print('No matches found')


def print_data_base(data_base):
    print()
    counter = 0
    for line in data_base:
        values = list(line.split())
        if len(values) == 3:
            if(type(values[0]) == type(values[2]) == str) and (numchecker.make_float(values[1]) is not None):
                if counter == 0:
                    pretty_print()
                pretty_print(values)
                counter += 1
    if counter == 0:
        print('Database is empty')


def safe_open(file_path, mode, func=None, *args):
    try:
        with open(file_path, mode) as data_base:
            if func is not None:
                if len(args) > 0:
                    func(data_base, args)
                else:
                    func(data_base)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return False
    except OSError as err:
        print(f"Operating system error while working with file {file_path}")
        print(traceback.format_exc())
        return False
    except Exception as err:
        print(f"Unexpected error while working with file {file_path}", repr(err))
        print(traceback.format_exc())
        return False
    return True


def menu():
    global current_path
    print()
    print('1. Select file to work')
    print('2. Initialize database')
    print('3. List the contents of the database')
    print('4. Add an entry to the database')
    print('5. Single field search')
    print('6. Search by two fields')
    print('7. Exiting the program')
    num = ioformat.get_int('Enter option number: ')
    if 0 > num or num > 7:
        print('Option not found!!')

    if num == 1:
        file_path = input("Enter file name: ").strip()
        if len(file_path) == 0 or any(char in bad_symbols for char in file_path) or file_path[-1] in '. ':
            print('Invalid file name')
        else:
            ext = get_extension(file_path)
            if ext != 'txt':
                print('Unsupported file type:', ext)
            else:
                current_path = file_path
                print('File selected')
    else:
        if current_path is not None:
            if num == 2:
                create_file(current_path)

            if num == 3:
                safe_open(current_path, 'r', print_data_base)

            if num == 4:
                safe_open(current_path, 'a', add_record)

            if num == 5:
                safe_open(current_path, 'r', field_search, 1)

            if num == 6:
                safe_open(current_path, 'r', field_search, 2)
        else:
            print('You must enter the path to the file')

    if num == 7:
        return 0


def main():
    while menu() is None:
        pass


if __name__ == '__main__':
    main()
