import csv

with open('/home/user/Загрузки/vacancy.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    reader1 = list(reader)

company = input()

while company != 'None':
    for el in reader1:
        if el[-1]==company:
            print(f'В {company} найдена вакансия: {el[-2]}. З/п составит:{el[-5]}')

    if el[-1]!=company:    
        print('К сожалению, ничего не удалось найти.')
    company = input()