def calculate_area():
    print("Выберите фигуру:")
    print("1. Круг")
    print("2. Прямоугольник")
    print("3. Треугольник")

    choice = input("Введите номер фигуры: ")

    if choice == '1':
        radius = float(input("Введите радиус круга: "))
        area = 3.14159 * radius ** 2
        print(f"Площадь круга: {area}")
    elif choice == '2':
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = length * width
        print(f"Площадь прямоугольника: {area}")
    elif choice == '3':
        base = float(input("Введите основание треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        area = 0.5 * base * height
        print(f"Площадь треугольника: {area}")
    else:
        print("Неверный выбор.")

calculate_area()