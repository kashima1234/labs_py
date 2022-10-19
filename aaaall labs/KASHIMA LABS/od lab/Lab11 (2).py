
#Оюунтуяа Одбаясгалан ИУ7-13Б
#Lab11

from pprint import pprint
import string 

lines = ['odko. 22aaa22.', 'Ich bin  3+4+2+2+2    -2, my prince. Genoa and Lucca are no longer just prerogatives, from',
         ' -3  4 estates, de la famille Buon 9 -     0 aparte. Nein, ich warne Sie davor, wenn Sie mir nicht sagen, dass wir es haben',
         'Krieg, wenn Sie sich noch erlauben, all die Schande, all die Gräueltaten dieses Antichristen (mein Wort,',
         'glaube ich) — ich kenne dich nicht mehr, vo2 +   3you are no longer my friend, you',
         'nêtes plus мой верный раб, 6    + co0 mme vous dites.',
         'Ну, здравствуйте, здравствуйте. Ich sehe, dass ich dir Angst mache 2, садитесь и рассказывайте.']

#lines = ['Ich bin,', 'my prince.', ' абв а а', 'а и у е б б б б б б.']


def fix_lines():
    global width 
    for i in range(len(lines)):
        space_cnt = 0
        j = 0
        lines[i] = lines[i].strip()
        line_len = len(lines[i])
        while j < line_len:
            if lines[i][j] != ' ' and space_cnt > 1:
                lines[i] = lines[i][:j - space_cnt]  + ' ' + lines[i][j:]
                j -= space_cnt - 1
                line_len -= space_cnt - 1
                space_cnt = 0
            elif lines[i][j] != ' ':
                space_cnt = 0
                j += 1            
            elif lines[i][j] == ' ':
                space_cnt += 1
                j += 1
        lines[i] = lines[i][:len(lines[i]) - space_cnt]
    width = len(max(lines, key=lambda x: len(x)))


def align_to_right():
    fix_lines()
    for i in range(len(lines)):
        lines[i] = ' ' * (width - len(lines[i])) + lines[i]


def align_to_left():
    fix_lines()
    for i in range(len(lines)):
        j = 0
        while j < len(lines[i]) and lines[i][j] == ' ':
            j += 1
        lines[i] = lines[i][j:]


def align_to_width():
    fix_lines()
    print_text()
    def idx_to_next_space(line_idx, curr_idx):
        if lines[line_idx][curr_idx] == ' ':
            while curr_idx < len(lines[line_idx]) and lines[line_idx][curr_idx] == ' ':
                curr_idx += 1
        while curr_idx < len(lines[line_idx]) and lines[line_idx][curr_idx] != ' ':
            curr_idx += 1
        
        return curr_idx

    for i in range(len(lines)):
        spaces_amount = lines[i].count(' ')
        amount_to_insert= width - len(lines[i])

        if spaces_amount == 0:
            lines[i] = ' ' * (amount_to_insert // 2) + lines[i] + ' ' * (amount_to_insert // 2)
            if amount_to_insert % 2:
                lines[i] += ' '
            continue

        insert_count = amount_to_insert // spaces_amount
        curr_space = idx_to_next_space(i, 0)
        for j in range(spaces_amount):
            lines[i] = lines[i][:curr_space] + ' ' * insert_count + lines[i][curr_space:]
            amount_to_insert -= insert_count
            curr_space = idx_to_next_space(i, curr_space)
        
        if amount_to_insert != 0:
            idx = idx_to_next_space(i, 0)
            lines[i] = lines[i][:idx] + ' ' * amount_to_insert + lines[i][idx:]


def word_indexes(word):
    ln = len(word)

    for i in range(len(lines)):
        idx = lines[i].find(word)
        while idx != -1:
            curr_word = word
            if idx - 1 < 0: curr_word = ' ' + curr_word
            else: curr_word = lines[i][idx - 1] + curr_word
            if idx + ln >= len(lines[i]): curr_word = curr_word + ' '
            else: curr_word = curr_word + lines[i][idx + ln]
            if ((curr_word[0] == ' ' or curr_word[0] in string.punctuation)
                and (curr_word[-1] == ' ' or curr_word[-1] in string.punctuation)):
                yield i, idx
            idx = lines[i].find(word, idx + len(word))


def del_word():
    global lines
    word = input('Enter a word: ')
    for i, j in word_indexes(word):
        lines[i] = lines[i][:j] + lines[i][j + len(word):]

    fix_lines()
    lines = [lines[i] for i in range(len(lines)) if len(lines[i]) != 0]
    

def replace_word():
    old_w, new_w = input('Enter the old word: '), input('Enter a new word: ')
    for i, j in word_indexes(old_w):
        lines[i] = lines[i][:j] + new_w + lines[i][j + len(old_w):]
    fix_lines()


def calculate():
    global lines
    print('cacl')
    sign_digits = set('1234567890+-')
    digits = set('1234567890')
    def next_symb(line_idx, curr_idx):
        curr_idx += 1
        while curr_idx < len(lines[line_idx]):
            if lines[line_idx][curr_idx]!= ' ': return (line_idx, curr_idx)
            curr_idx += 1
        if line_idx < len(lines) - 1:
            return next_symb(line_idx + 1, -1)
        else:
            return None
    
    line_idx = 0
    idx = -1
    char_idx = next_symb(line_idx, idx)
    nums = []
    while char_idx != None:
        line_idx, idx = char_idx[0], char_idx[1]
        if lines[line_idx][idx] in sign_digits:
            end_line_idx, end_idx = line_idx, idx
            next_char_idx = next_symb(end_line_idx, end_idx)
            while next_char_idx != None and lines[next_char_idx[0]][next_char_idx[1]] in sign_digits:
                end_line_idx, end_idx = next_char_idx[0], next_char_idx[1]
                if next_char_idx[1] == len(lines[next_char_idx[0]]) - 1 and lines[next_char_idx[0]][next_char_idx[1]] in digits:
                    break
                next_char_idx = next_symb(end_line_idx, end_idx)
            nums.append(((line_idx, idx), (end_line_idx, end_idx)))
            line_idx, idx = end_line_idx, end_idx
        char_idx = next_symb(line_idx, idx)
    print(nums)
    for start_idx, end_idx in nums:
        num = ''
        line_start, idx_start = start_idx[0], start_idx[1]
        line_end, idx_end = end_idx[0], end_idx[1]
        if line_start != line_end:
            num += lines[line_start][idx_start:]
            for curr_line_idx in range(line_start + 1, line_end):
                num += lines[curr_line_idx]
            num += lines[line_end][:idx_end + 1]
        else:
            num = lines[line_start][idx_start : idx_end + 1]
        if '+' not in num and '-' not in num:
            continue
        if num[1:-1].count('-') == num[1:-1].count('+') == 0:
            continue
        sign = 1
        result = 0
        curr_num = ''
        for i in range(len(num)):
            if num[i] in digits:
                curr_num += num[i]
            elif num[i] != ' ':
                if len(curr_num) != 0:
                    result += int(curr_num) * sign
                    curr_num = ''
                sign = 1 if num[i] == '+' else -1
        if len(curr_num) != 0:
            result += int(curr_num) * sign
        if line_start == line_end:
            lines[line_start] = lines[line_start][:idx_start] + str(result) + lines[line_start][idx_end + 1:]
        else:
            lines[line_start] = lines[line_start][:idx_start] + str(result)
            lines = [lines[i] for i in range(len(lines)) if i <= line_start or i >= line_end - 1]
            if next_symb(line_end, idx_end) == None or next_symb(line_end, idx_end)[0] != line_end:
                lines.pop(line_end)
            else:
                lines[line_end] = lines[line_end][idx_end + 1:]
        
        width = len(max(lines, key=lambda x: len(x)))
 

def frequent_char():
    chars = dict()
    seq = 1
    for i in range(len(lines)):
        for char in lines[i]:
            if char == ' ': continue
            if char == '.':
                if not seq % 2:
                    freq_char = max(chars.items(), key=lambda x: x[1])[0]
                    print(f'Sentence {seq}:', repr(freq_char))
                seq += 1
                chars.clear()
            chars.setdefault(char, 0)
            chars[char] += 1
        


def print_text():
    print('-' * width)
    for line in lines:
        print(line)
    print('-' * width)
    print(end='\n\n')

def print_menu():
    print('''1. Align text left
2. Align text right
3. Justify text
4. Remove all occurrences of a given word
5. Replacing one word with another throughout the text
6. Calculation of arithmetic expressions inside the text (operations of addition and subtraction)
7. In each even sentence, determine the most common
symbol.''')

def loop():
    fix_lines()
    functions = [align_to_left, align_to_right, align_to_width, \
                del_word, replace_word, calculate, frequent_char]
    last_align_functoin = 0
    print_menu()
    print('ENTER OPTION TO EXIT quit')
    while True:
        cmd = input('Enter option number from 1 to 7: ')
        if cmd == 'quit': break
        if not cmd.isdigit() or int(cmd) < 1 or int(cmd) > 7:
            print('You entered an invalid number, please try again!')
            continue
        cmd = int(cmd) - 1
        
        functions[cmd]()
        if cmd < 3:
            last_align_functoin = cmd
        elif cmd < 6:
            functions[last_align_functoin]()
        print_menu()
        print_text()


def test():
    replace_word()
    print_text()


def main():
    loop()

if __name__ == '__main__':
    main()
