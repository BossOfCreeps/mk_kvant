# pip3 install matplotlib

import sqlite3
import matplotlib.pyplot as plt

# Создаём (или открываем) файл базы
conn = sqlite3.connect("temperatura.db")
cur = conn.cursor()

# Таблица: день и температура
cur.execute("CREATE TABLE IF NOT EXISTS pogoda (den INTEGER, temp REAL)")

###

# Удаляем старые данные
cur.execute("DELETE FROM pogoda")

# Записываем данные
dani = [
    (1, -5.2),
    (2, -3.1),
    (3, 0.4),
    (4, 2.8),
    (5, 1.5),
]
cur.executemany("INSERT INTO pogoda VALUES (?, ?)", dani)

conn.commit()  # сохранить
print("Записано!")

###

# Читаем данные
cur.execute("SELECT den, temp FROM pogoda")
rows = cur.fetchall()

conn.close()

for den, temp in rows:
    print(f"День {den}: {temp}°C")

###

# Разбираем данные на два списка
dni = [s[0] for s in rows]
tempy = [s[1] for s in rows]

plt.plot(dni, tempy)
plt.title("Температура по дням")
plt.grid(True)
plt.show()

"""
| График                 | Функция        | Когда использовать                  |
|------------------------|----------------|-------------------------------------|
| Линейный               | `plot`         | изменение во времени                |
| Столбчатый             | `bar`          | сравнение категорий                 |
| Горизонтальные столбцы | `barh`         | сравнение категорий (горизонтально) |
| С заливкой             | `fill_between` | область под кривой                  |
| Точечный               | `scatter`      | связь двух величин                  |
"""
