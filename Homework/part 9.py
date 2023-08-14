

# Задача 1

# emp = {
#     'emp1': {'name': 'Jhon', 'salary': '7500'},
#     'emp2': {'name': 'Emma', 'salary': '8000'},
#     'emp3': {'name': 'Brad', 'salary': '6500'}
# }
# print(emp['emp3'])
# emp['emp3']['salary'] = '8500'
#
# for i in emp:
#     print(i, '\nname :', emp[i]['name'], '\nsalary :', emp[i]['salary'])


# Задача 2

# student = {
#     1: {'name': 'Игорь', 'score': 12},
#     2: {'name': 'Валентин', 'score': 7},
#     3: {'name': 'Виктор', 'score': 4},
#     4: {'name': 'Григорий', 'score': 9},
#     5: {'name': 'Дмитрий', 'score': 6}
# }
# score_sum = 0
#
# print('Количество студентов:', len(student))
#
# for i in student:
#     score_sum += student[i]['score']
#     print(i, '-й студент: ', student[i]['name'], '\nБалл: ', student[i]['score'], sep='')
#
# av_score = round(score_sum / len(student))
# print('Средний балл: ', av_score, '. ', 'Студенты с баллом выше среднего: ', sep='')
#
# for i in student:
#     if student[i]['score'] > av_score:
#         print(student[i]['name'])
