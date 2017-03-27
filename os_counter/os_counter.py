import sys

dic = {'2Macintosh': 0, '0Windows': 0, '1Ubuntu': 0, '2OS X': 0, '4Unknown': 0}
for line in sys.stdin.readlines():
    s1 = line.strip().split('"')[-2].strip().split('(')[1]
    s = s1.strip().split(';')[0].strip().split(' ')[0]
    if s != 'Windows' and s != 'Ubuntu' and s != 'Macintosh':
        dic['4Unknown'] += 1
    elif s == 'Windows':
        dic['0Windows'] += 1
    elif s == 'Ubuntu':
        dic['1Ubuntu'] += 1
    elif s == 'Macintosh':
        dic['2Macintosh'] += 1
dic['2OS X'] = dic['2Macintosh']
del(dic['2Macintosh'])
for key, value in sorted(dic.items(), key=lambda x: (x[1], x[0])):
    print(key[1:] + ': ' + str(value))
