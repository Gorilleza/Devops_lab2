import os

DATA_DIR = "/var/data"
RESULT_FILE = "/var/result/data.txt"

# Собираем список всех файлов в папке data
files = [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if os.path.isfile(os.path.join(DATA_DIR, f))]

# Открываем результирующий файл для записи
with open(RESULT_FILE, "w") as result:
    for filepath in files:
        with open(filepath, "r") as f:
            # Читаем первую строку и записываем её в результат
            first_line = f.readline()
            if first_line:
                result.write(first_line.strip() + "\n")

print(f"Программа 1: успешно обработано файлов: {len(files)}")