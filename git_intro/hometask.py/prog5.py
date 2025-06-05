n = int(input("Введите число n: "))  

print("Числа от 1 до", n, "не делящиеся на 3:")
for num in range(1, n + 1):
    if num % 3 == 0:  
        continue      
    print(num)        