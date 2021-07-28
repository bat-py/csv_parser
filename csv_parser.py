import time 
import csv 

file = input("Файл: ").replace("'", "").replace('"', '').strip()
while True:
    try:
        multi_column = int(input("Порядковый номер столбца который нужно разделить: "))-1
    except:
        print("Введите целое число!\n")
    else:
        break


dates = [] 
parsed_dates = []

#reads csv file and write all dates to variable 'date'
with open(file, 'r', encoding='latin1') as red:
    d = csv.reader(red, delimiter=';')
    
    for i in d:
        dates.append(i)


for date in dates:
    multi_column_items = date[multi_column].split(',')
    for i in multi_column_items:
        date[multi_column] = i
        parsed_dates.append(date)
        

#write pardes dates to file 'parsed_dates.csv'
with open('parsed_dates.csv', 'w', encoding='latin1', newline='') as parsed_d:
    n = csv.writer(parsed_d, delimiter=';')
    n.writerows(parsed_dates)


print('\nВсё готово :)')
time.sleep(2)

