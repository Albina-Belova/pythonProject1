" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример: - 6 -> да - 7 -> да - 1 -> нет  "

q = int(input('Введите день: '))
if q == 1:
    print('Понедельник- нет')
elif q == 2:
    print('Вторник-нет')
elif q == 3:
    print('Среда-нет')
elif q == 4:
    print('Четверг-нет')
elif q == 5:
    print('Пятница-нет')
elif q == 6:
    print('Суббота-да')
else:
    print('Воскресенье-да')