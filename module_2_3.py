# Вариант № 1 (более короткий и красивый)
print("Вариант № 1")
my_list=[42,69,322,13,0,99,-5,9,8,7,-6,5]
index = 0
while index < len(my_list):
    if my_list[index]<0:
        break
    if my_list[index]>0:
        print(my_list[index])
    index += 1

# Вариант № 2 (более длинный)
print("Вариант № 2")
my_list=[42,69,322,13,0,99,-5,9,8,7,-6,5]
index = 0
while index < len(my_list):
    if my_list[index] > 0:
        print(my_list[index])
        index += 1
    if my_list[index] == 0:
        index += 1
    if my_list[index] < 0:
        break