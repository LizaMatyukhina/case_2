from random import randint

'''Функция перевода часов в минуты.'''
def time(hours):
    h, m = hours.split(':')
    minutes = int(h) * 60 + int(m)
    return minutes

'''# Функция расчета времени для стоянки на бензоколонке.'''
def time_for_benz(volume):
    volume = int(volume)
    volume = volume // 10
    if volume % 10 > 5:
        volume += 1
    plus_time = randint(-1, 1)
    volume += plus_time
    if volume == 0:
        return 1
    return volume


'''# Счет данных из главного файла + словарь с главными данными.'''
d1 = {}
with open('azs.txt', 'r') as f_in1:
    text1 = f_in1.readlines()
    text1 = [line.strip() for line in text1]
    for i in range(len(text1)):
        a = {}
        line = text1[i]
        line = line.split()
        [a['max']] = line[1]
        k = []
        for j in range(2, len(line)):
            h = line[j]
            k.append(h)
        a.update({'benz': k})
        d1[line[0]] = a

print(d1)


'''
# Счет данных из input.txt + словарь со всеми данными.
# Time_to_stop = время запрвки автомобиля.
# time_to_go = время, когда автомобиль смодет поехать ЕСЛИ НЕТ ОЧЕРЕДИ!!
# V = нужный объем бензинв.
'''
d2 = {}
with open('input.txt', 'r') as f_in2:
    text2 = f_in2.readlines()
    text2 = [line.strip() for line in text2]
    for i in range(len(text2)):
        b = {}
        line = text2[i]
        line = line.split()
        minutes = time(line[0])
        b['V'] = line[1]
        b['benz'] = line[2]
        minutes_to_stop = time_for_benz(line[1])
        b['time_to_stop'] = minutes_to_stop
        b['time_to_go'] = minutes + minutes_to_stop
        d2[minutes] = b
print(d2)

