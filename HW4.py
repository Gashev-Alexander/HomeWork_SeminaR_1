print("Введите координаты точки")
x = float(input("X = "))
y = float(input("Y = "))
if x > 0 and y > 0:
    print("Четверть 1")
elif x < 0 and y > 0:
    print("Четверть 2")
elif x < 0 and y < 0:
    print("Четверть 3")
elif x > 0 and y < 0:
    print("Четверть 4")
elif x == 0 and y != 0 :
    print("На оси X")
elif y == 0 and x != 0:
    print("На оси Y")
elif x == 0 and y == 0:
    print("Центр")