file_out = open('out.txt', 'w')
file_in = open('in.txt', 'r')
shortest = longest = file_in.readline()
while True:
    line = file_in.readline().strip()
    if len(line) == 0:
        break
    if len(line) > len(longest):
        longest = line
    if len(line) < len(shortest):
        shortest = line
print(shortest)
print(longest)
file_out.write(shortest + '\n')
file_out.write(longest + '\n')
file_in.close()
file_in = open('in.txt', 'r')
while True:
    line = file_in.readline().strip()
    if len(line) == 0:
        break
    if line == shortest or line == longest:
        continue
    file_out.write('{} ({})\n'.format(line,len(line.split())))
file_out.close()
file_in.close()
print(file_out)
