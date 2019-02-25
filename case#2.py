from random import randint


def time(hours):
    h, m = hours.split(':')
    minutes = int(h) * 60 + int(m)
    return minutes


# Специально для Айгерим
def back_time(minutes):
    h = minutes // 60
    m = minutes - h * 60
    phrase = str(h) + ':' + str(m)
    return phrase


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


d1 = {}
with open('azs.txt', 'r') as f_in1:
    text1 = f_in1.readlines()
    text1 = [line.strip() for line in text1]
    value = len(text1)
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
# Prices!
d3 = {}
d3['АИ-80'] = 38
d3['АИ-92'] = 41
d3['АИ-95'] = 44
d3['АИ-98'] = 49


colichestvo_kolonok = value
d4 = {}
d6 = {}
for n in range(1, colichestvo_kolonok+1):
    d4[n] = 0
    d6[n] = []

print(d6)


# Для подсчета объема бензина.
d5 = {}
d5['АИ-80'] = 0
d5['АИ-92'] = 0
d5['АИ-95'] = 0
d5['АИ-98'] = 0


its_time_to_go = {}
queue = 0

# Ставлю в очередь.
for i in range(1440):
    condition = 0 # По этому условию я дальше проверяю сможет ли человек встать в очередь, если сможет, то я меняю на 1, если нет, то ******* (ищи звездочки дальше)
    if i in d2.keys(): # если время совпадает с временем приезда клиента
        patrol = d2[i]['benz']  # запоминаю какой бензин нужен
        mini = 1000
        for j in range(1, colichestvo_kolonok + 1):
            if patrol in d1[str(j)]['benz']: # Если этот бензин имеется в наличии (в первом словаре), то
                if d4[j] < int(d1[str(j)]['max']): # Проверяю в 4 словаре с очередью все ли в порядке, меньше ли она, чем максимум из 1 словаря
                    if d4[j] < mini:
                        hil = j
                        mini = d4[j]
                        d4[j] += 1
                        print(' В', back_time(i), 'новый клиент: ', back_time(i), d2[i]['benz'], d2[i]['V'],
                              d2[i]['time_to_stop'],
                              'встал в очередь к автомату №', j)
                        d6[j].append(i)
                        condition = 1 # ВОТ ТУТ МЕНЯЮ ********
                        d5[d2[i]['benz']] += int(d2[i]['V']) # Это для дальнейших вычислений, не нужно менять
                        d2[i].update({'station': j}) # Добавляю еще одно значение с бензоколонкой для проверки в след условии
                        just = d2[i]['time_to_go'] # Время отъезда запоминаю, тут можно как раз и сделать доп условие по времени, которое у тебя в тетрадке. ******************ПОДУМАТЬ*******************
                        its_time_to_go[i] = just # Ну и это словарь который дальше используем
                        break

        if condition == 0:     # ЕСЛИ НЕ ПОМЕНЯЛОСЬ, ТО ГОВОРЮ ЧТО НЕ СМОГ ВСТАТЬ В ОЧЕРЕДЬ, ТУТ НИЧЕГО МЕНЯТЬ НЕ НУЖНО
            print(' В', back_time(i), 'новый клиент: ', back_time(i), d2[i]['benz'], d2[i]['V'], d2[i]['time_to_stop'],
                  'не смог заправить автомобиль и покинул АЗС.')
            queue += 1  # Сколько покинуло
        for k in range(1, value + 1):
            print('Автомат №', k, 'максимальная очередь:', d1[str(k)]['max'], 'Марки бензина:', *(d1[str(k)]['benz']),
                  '->', '*' * d4[k])

    # Убираю из очереди. Здесь тоже ничего трогать не нужно.

    if i in its_time_to_go.values():
        g = 0
        pribitie_s_povtorom_otbitiya = []
        lst = list(its_time_to_go.values())
        llst = list(its_time_to_go.keys())
        for z in range(len(its_time_to_go.keys())):
            if i == lst[z]:
                g += 1
                pribitie_s_povtorom_otbitiya.append(llst[z])
        for s in range(g):
            arrive = pribitie_s_povtorom_otbitiya[s]
            l = d2[arrive]['station']
            d4[l] -= 1
            print(' В', back_time(i), 'клиент: ', back_time(arrive), d2[arrive]['benz'], d2[arrive]['V'],
                  d2[arrive]['time_to_stop'],
                  'заправил свой автомобиль и покинул АЗС.')
            for k in range(1, value + 1):
                print('Автомат №', k, 'максимальная очередь:', d1[str(k)]['max'], 'Марки бензина:',
                      *(d1[str(k)]['benz']),
                      '->', '*' * d4[k])
            its_time_to_go.pop(arrive)


print('Количество литров, проданное за сутки по каждой марке бензина:', d5) # можно сделать красивый вывод, без словарей
money=0
our_patrol=['АИ-80', 'АИ-92', 'АИ-98', 'АИ-95']
for p in our_patrol:
    money+=d5[p]*d3[p]
print('Общая сумма продаж за сутки:', money)
print('Количество клиентов, которые покинули АЗС не заправив автомобиль из-за «скопившейся» очереди:', queue)

# добавить 0 перед временем, рулокал - АЙГЕРИМ

# умная очередь, время ожидания(по возможности) - ЛИЗА
