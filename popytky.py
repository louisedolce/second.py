file = open("sobaka.txt", "r")
line = file.read()
print('Последовательность:', line)
leni = list(set(line)) #делаем из списка множество, а затем опять список, чтобы удалить повторяющиеся элементы
for j in range(0, len(leni)): #некая переменная, позволяющая сделать цикл n-1 раз
    for i in range(1, len(leni)): #переменная пробегающая все числа в последовательности
        if leni[i-1] > leni[i]:
            leni[i-1], leni[i] = leni[i], leni[i-1]
leni.remove(',')
leni.remove(' ')
print('Последовательность в порядке убывания:', leni)