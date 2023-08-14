import csv

with open('data2.csv') as f:
    file_reader = csv.reader(f, delimiter=';')
    count = 0
    for row in file_reader:
        if count == 0:
            print(f'{row[0]}  {row[1]}  {row[2]}  {row[3]}')
            print('-' * 35)
        else:
            print(f'{count}   {row[0]}   {row[1]}   {row[2]}   {row[3]}')
        count += 1
