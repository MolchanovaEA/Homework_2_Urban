def get_matrix (n, m, value):
    matrix=[]
    for i in range (n):
        row=[]
        for j in range (m):
            row.append (value)
        matrix.append (row)
    return matrix
#result = get_matrix (n, m, value)
result1 = get_matrix (5, 3, 25)
result2 = get_matrix (4, 4, 4)
result3 = get_matrix (7, 10, 7)
print (result1)
print (result2)
print (result3)
for row in result1:
    print (row)
for row in result2:
    print (row)
for row in result3:
    print (row)