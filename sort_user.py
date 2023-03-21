user_list=[5,2,9,-10,200,5,0,-2,7,6,4,5]


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
    
# def sort_list(spisok):
#     # pivot = spisok.pop()
#     max_value, min_value = [], []
#     equals_value = []
    
#     if len(spisok) > 1 :
#         pivot = spisok.pop()

#     else:
#         return spisok    

#     for item in spisok[:1]:
#         if item > pivot:
#             max_value.append(item)
#         elif item == pivot:
#             equals_value.append(item)
#         elif item < pivot: 
#             min_value.append(item)
#     return sort_list(max_value)+[equals_value]+sort_list(min_value)

print(sort_list(user_list))







