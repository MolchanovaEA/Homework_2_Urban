n=int(input("Введите число n (количество строк): "))
m=int(input("Введите число m (количество столбцов): "))
value=int(input("Введите значение для заполнения матрицы: "))
def get_matrix (n, m, value):
    matrix=[]
    for i in range (n):
        row=[]
        for j in range (m):
            row.append (value)
        matrix.append (row)
    return matrix
result = get_matrix (n, m, value)
print (result)