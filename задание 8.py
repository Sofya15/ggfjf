a = int(input("Введите наименьшее число: "))
b = int(input("Введите наибольшее число: "))
for i in range(a,b):
    if i % a == 0:
        print(i)
