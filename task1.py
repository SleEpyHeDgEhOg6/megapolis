import csv

def cpSalary(s):
    prox = 100
       

with open('/home/user/Загрузки/vacancy.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    reader1 = list(reader)[1:]
    
        