import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('data3.db')
cursor = conn.cursor()

# Выполняем запрос к базе данных
cursor.execute('''SELECT * FROM data''')

# Получаем все записи из таблицы
rows = cursor.fetchall()

# Выводим содержимое таблицы
for row in rows:
    print(row)

# Закрываем соединение
conn.close()