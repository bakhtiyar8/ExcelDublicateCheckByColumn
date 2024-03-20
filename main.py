import openpyxl
import sqlite3

# Открываем файл Excel
wb = openpyxl.load_workbook('SDRdata.xlsx')
sheet = wb.active
# Создаем базу данных SQLite
conn = sqlite3.connect('data4SDR.db')
cursor = conn.cursor()

# Создаем таблицу в базе данных
cursor.execute('''CREATE TABLE data (SiteName text, Frequency integer)''')

# Итерируемся по строкам в Excel и записываем данные в базу данных
for row in sheet.iter_rows(values_only=True):
    site_name = row[0]
    
    for i in range(1, len(row)):
        frequency = row[i]
        
        cursor.execute('''INSERT INTO data (SiteName, Frequency) VALUES (?, ?)''', (site_name, frequency))

conn.commit()
print("Process finished")
# Закрываем соединение
conn.close()