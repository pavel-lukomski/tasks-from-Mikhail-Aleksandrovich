last_l, new_l = int(input()), int(input())
if last_l == -1:
    print('Определено расстояние до нового объекта, и оно равно', new_l)
elif new_l > last_l:
    print('Объект отдалился')
elif new_l < last_l:
    print('Объект приблизился')
elif new_l == last_l:
    print('Расстояние не изменилось')
