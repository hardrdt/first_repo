total = 0  

while True:  
    num = int(input("Введите число (0 для выхода): "))
    if num == 0:  
        break     
    total += num  

print(f"Сумма всех введённых чисел: {total}")