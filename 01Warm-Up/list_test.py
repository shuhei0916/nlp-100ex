s = 'I have a pen'

print(s)
print(type(s))

splited_list = s.split(' ')
print(splited_list)

print(' '.join(splited_list))

squares = []
for i in range(7):
    squares.append((i + 1) * (i + 1))

for square in squares:
    print(square, end = ' ')