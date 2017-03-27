import sys

counter = 0
for line in sys.stdin.readlines():
    s = line.strip().split('"')
    if s[-2] == 'Go-http-client/1.1':
        counter += 1
print(counter)
