data = ((10, 10, 10, 12), 
        (30, 45, 56, 45), 
        (81, 80, 39, 32), 
        (1, 2, 3, 4))

rows = len(data)
cols = len(data[0])

averages = []

for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += data[i][j]
    averages.append(round(col_sum / rows, 2))

print(averages)