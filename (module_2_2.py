first = int(input("Введите число: "))
second = int(input("Введите число: "))
third = int(input("Введите число: "))
if first != second and first != third and second != third:
    print('0')
elif first == second and first !=third :
    print("2")
elif first != second and first == third:
    print("2")
elif first != second and first != third:
    print("2")
elif first == second and first == third and second == third:
    print('3')