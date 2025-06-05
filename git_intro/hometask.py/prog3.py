number = int(input("Введите число: "))  

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
    if result % 5 == 0:  
        print("Фу, 5 опять...")