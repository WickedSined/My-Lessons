user_list=['Мудрик','Апостол','Грубый','Виницкий','','Марик','Бондарь','Синицкий','','Пуня','Паланский','Питкин','']

# Блок удаления пустых значений в списке
for item in user_list:
    if item == '':
        user_list.remove('')
print(user_list)
surname = 'Апостол'


midle_index = len(user_list)//2
print(midle_index)
new_list = []
base = ''

if surname == user_list[midle_index]:
        surname = user_list[midle_index]
        # return surname
elif surname > user_list[midle_index]:
        print(user_list[midle_index:])
elif surname < user_list[midle_index]:
        print(user_list[:midle_index])