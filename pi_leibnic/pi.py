pi = 0
for i in range(1, 20, 2):
    pi += ((-1) ** ((i - 1) / 2)) / float(i)
print(4 * pi)
