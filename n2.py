x = ['apple', 'avocado', 'mango', 'peach', 'apple', 'papaya']
y = [i for i in set(x) if x.count(i) > 1]

if len(y) == 0:
   print("Повторяющихся элементов нет")
else:
   print(y)