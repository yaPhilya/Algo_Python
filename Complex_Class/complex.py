import sys


class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(real=self.real + other.real,
                             imaginary=self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(real=self.real - other.real,
                             imaginary=self.imaginary - other.imaginary)

    def __mul__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        return ComplexNumber(real=a * c - b * d, imaginary=a * d + b * c)

    def __abs__(self):
        return self.real ** 2 + self.imaginary ** 2

    def conjugate(self):
        return ComplexNumber(real=self.real, imaginary=-self.imaginary)

    def simple_division(self, real):
        return ComplexNumber(real=self.real / real,
                             imaginary=self.imaginary / real)

    def __div__(self, other):
        return (self * other.conjugate()).simple_division(abs(other))

    def __str__(self):
        if self.real != 0:
            if self.imaginary > 0:
                return '%.2f' % self.real + ' + ' + \
                       '%.2f' % self.imaginary + 'i'
            elif self.imaginary < 0:
                return '%.2f' % self.real + ' - ' + \
                       '%.2f' % abs(self.imaginary) + 'i'
            else:
                return '%.2f' % self.real
        elif self.imaginary != 0:
            return '%.2f' % self.imaginary + 'i'
        else:
            return '0.00'


if __name__ == "__main__":
    for line in sys.stdin.readlines():
        print eval(line.strip())
