n = int(input("Введите число n: "))  
even_numbers = []  

for num in range(1, n + 1):
    if num % 2 == 0:  
        even_numbers.append(num)  
        print(num)  

print(f"Всего чётных чисел: {len(even_numbers)}")  