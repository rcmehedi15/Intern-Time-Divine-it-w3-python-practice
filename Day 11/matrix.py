matrix = [
    [1,2,3],
    [4,5,6],
]
#value change

matrix[0][2] = 10
print("Matrix Number : ",matrix[0][2])

# for loop

for row in matrix:
    for col in row:
        print(col)