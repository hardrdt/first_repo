time = int(input("Введите время в часах от 0 до 23: "))

if 6 <= time <= 11:
    print("Утро")
elif 12 <= time <= 17:
    print("День")
elif 18 <= time <= 23:
    print("Вечер")
else:
    print("Ночь")