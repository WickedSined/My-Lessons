user_list=['Мудрик','Апостол','Грубый','Виницкий','','Марик','Бондарь','Синицкий','','Пуня','Паланский','Питкин','']
sorted_list=[]
# Блок удаления пустых значений в списке
for item in user_list:
    if item == '':
        user_list.remove('')
 
    
print(user_list)

# Блок сортировки списка
def sort_list(spisok):
    less = []
    gr = []
    eq = []

    if len(spisok)<2:
        return spisok
    else:
        pivot=spisok[0]
    
    for item in spisok[1:]:
        if item < pivot:
            less.append(item)
        elif item == pivot:
            eq.append(item)
        elif item > pivot:
            gr.append(item)
    return sort_list(less) + eq + [pivot] + sort_list(gr)

def find_surname(work_list, surname):

    if not work_list:
        return None
    # определяем индекс для деления списка пополам (без остатка деление на 2)
    middle_index = len(work_list) // 2
    
    if surname == work_list[middle_index]:
        return surname
    elif surname < work_list[middle_index]:
        new_list = work_list[:middle_index]
        return find_surname(new_list, surname)
    elif surname > work_list[middle_index]:
        new_list = work_list[middle_index+1:]
        return find_surname(new_list, surname)
    
    # else:
    #     new_list = work_list[:middle_index]
    #     return find_surname(new_list, surname)


name_sur = 'Пуня'
sorted_list = sort_list(user_list)
print(find_surname(sorted_list,name_sur))
