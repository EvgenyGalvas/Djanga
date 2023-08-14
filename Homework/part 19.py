def quick_sort(a):
    if len(a) > 1:
        x = a[(len(a) - 1) // 2]

        low = [i for i in a if i < x]
        eq = [i for i in a if i == x]
        hi = [i for i in a if i > x]

        a = quick_sort(low) + eq + quick_sort(hi)

    return a


def seq_search(s, item):
    found = False
    pos = 0
    while pos < len(s) and not found:
        if s[pos] == item:
            found = True
        else:
            pos += 1
    return found


lst1 = [5, 9, 6, 7]
lst2 = [3, 11, 8]
lst3 = [2, 4]
lst4 = [10, 1, 12]

lst_total = lst1 + lst2 + lst3 + lst4
lst_total_sort_low_hi = quick_sort(lst_total)
lst_total_sort_hi_low = quick_sort(lst_total)[::-1]


print('1 - сортировка по убыванию')
print('2 - сортировка по возрастанию')
choice = input('-> ')
if choice == '1':
    print(lst_total_sort_hi_low)
elif choice == '2':
    print(lst_total_sort_low_hi)
else:
    print("Некорректные данные")

print()

search_number = int(input('Введите значение для поиска: '))
num = seq_search(lst_total, search_number)
if num:
    print(f'Значение {search_number} найдено' )
else:
    print(f'Значение {search_number} не найдено')
