import sqlite3
import openpyxl

# Подключаемся к базе данных
conn = sqlite3.connect('data4SDR.db')
cursor = conn.cursor()

# Выполняем запрос к базе данных для поиска дубликатов
cursor.execute('''SELECT SiteName, Frequency, COUNT(*) as count FROM data GROUP BY SiteName, Frequency HAVING count > 1''')

# Получаем все записи с дубликатами
duplicates = cursor.fetchall()

# Создаем новый Excel файл
wb = openpyxl.Workbook()
ws = wb.active

# Записываем результаты в Excel
ws.append(['SiteName', 'Frequency', 'Duplicate Count'])
for row in duplicates:
    ws.append(row)

# Сохраняем Excel файл
wb.save('SDR_GeranMeasFDDLTE_duplicates_report.xlsx')

# Закрываем соединение
conn.close()