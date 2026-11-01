import os

DATA_FILE = "/var/data/data.txt"
RESULT_FILE = "/var/result/result.txt"

with open(DATA_FILE, "r") as f:
    # Читаем все числа из файла
    numbers = [int(x) for x in f.read().split() if x.strip()]

if numbers:
    min_number = min(numbers)
    # Возводим в третью степень
    result = min_number ** 3
    
    with open(RESULT_FILE, "w") as f:
        f.write(str(result))
    
    # Выводим результат на экран (по требованию методички)
    print(f"Программа 2: наименьшее число = {min_number}")
    print(f"Программа 2: его третья степень = {result}")
else:
    print("Числа не найдены!")