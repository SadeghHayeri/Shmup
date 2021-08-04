import random

row, column = 100, 48

result = [["B" for i in range(column)] for j in range(row)]

for i in range(row):
    for j in range(column):
        if random.random() > .8:
            result[i][j] = 'G'

with open('map.txt', 'w') as f:
    for row in result:
        f.write(" ".join(row) + "\n")
