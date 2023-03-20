import random

group1 = ['Иванов', "Петров", "Сидоров", "Смирнов", "Попов", "Кузнецова", "Соколов", "Михайлова", "Василькова", "Новикова"]
group2 = ["Байол", "Бондарева", "Овчинникова", "Мазилова", "Цыганков", "Кащенко", "Гордеев", "Чугунова", "Дмитриева", "Головина"]
sport = (random.sample(group1, 5) + random.sample(group2, 5))
#Функция sample() модуля random возвращает список длины k случайных элементов, выбранных из последовательности

print(group1)
print(group2)
print(sport)
print('длина спортивной группы', len(sport))

spisok = list(sport)
spisok.sort()
sport = tuple(spisok) #Создадим кортеж из полученного списка
print(sport)

if 'Иванов' in sport:
    print(sport.count('Иванов'))
else:
    print('Иванов не входит в спортивную команду')