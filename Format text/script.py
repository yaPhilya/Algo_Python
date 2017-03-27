import argparse
import sys
import re


class MyException(Exception):
    pass


def format(source='stdin', path='stdout', width=78, margin=1):
    if source == 'stdin':
        text = sys.stdin.read().strip()
    else:
        with open(source) as f:
            text = f.read().strip()
    if path == 'stdout':
        out = sys.stdout
    else:
        out = open(path, 'w')
    for paragraph in text.split('\n\n'):
        paragraph = paragraph.strip()
        if paragraph == '':
            continue
        current = margin - 1
        for i in range(margin - 1):
            out.write(' ')
        for line in paragraph.split('\n'):
            line = line.strip()
            parts = re.split("(\W)", line)
            token = ''
            flag = False
            for part in parts:
                if part.isalnum():
                    if flag is False:
                        token += part
                        flag = True
                    elif current + len(token) + 1 <= width:
                        if current != 0:
                            out.write(' ')
                        out.write(token)
                        current += len(token) + 1
                        token = part
                    elif len(token) <= width:
                        out.write('\n')
                        out.write(token)
                        current = len(token)
                        token = part
                    else:
                        raise MyException('Word is too long '
                                          'for that line length')
                elif part == ',' or part == '.' or part == '?' or part == "'" \
                        or part == '!' or part == '-' or part == ':':
                    token += part
                    flag = True
                else:
                    pass
            if token != '':
                if current + len(token) + 1 <= width:
                    out.write(' ')
                    out.write(token)
                elif len(token) <= width:
                    out.write('\n')
                    out.write(token)
                else:
                    raise MyException('Word is too long for that line length')
            out.write('\n')
            current = 0
    if path != 'stdout':
        out.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default='stdin',
                        type=str, help='source of text')
    parser.add_argument('-o', '--output', default='stdout',
                        type=str, help='destination of formating')
    parser.add_argument('-l', '--line-length',
                        type=int, help='max length of string', required=True)
    parser.add_argument('-p', '--paragraph-spaces',
                        type=int, help='first line margin', required=True)
    args = parser.parse_args()
    if args.line_length <= args.paragraph_spaces:
        raise MyException('Line length less than paragraph spaces')
    format(args.input, args.output, args.line_length, args.paragraph_spaces)


if __name__ == '__main__':
    main()
