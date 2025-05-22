num1 = float(input("Введите первое число:"))
num2 = float(input("Введите второе число:"))

if num1 > num2:
    print(num1, "больше чем" , num2)
elif num2 > num1:
    print(num2, "Больше чем" , num1)
else:
    print("Числа равны")