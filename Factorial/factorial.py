import sys

n = sys.stdin.readline()
n = int(n.strip())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
