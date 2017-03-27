import sys


dictionary = {}
sum = 0
for line in sys.stdin.readlines():
    s = line.strip().split('"')[2].strip().split(' ')
    dictionary[s[0]] = dictionary.get(s[0], 0) + 1
    sum += 1
counter = 0
for key, value in dictionary.items():
    if '300' <= key <= '309':
        counter += value
print(dictionary['200'])
print(counter)
print(sum - counter - dictionary['200'])
print(sum)
