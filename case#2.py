from random import randint


def time(hours):
    h, m = hours.split(':')
    minutes = int(h) * 60 + int(m)
    return minutes


# Специально для Айгерим!
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


d5 = {}
d5['АИ-80'] = 0
d5['АИ-92'] = 0
d5['АИ-95'] = 0
d5['АИ-98'] = 0


its_time_to_go = {}
queue = 0

for i in range(1440):
    condition = 0
    if i in d2.keys():
        patrol = d2[i]['benz']
        mini = 1000
        for j in range(1, colichestvo_kolonok + 1):
            if patrol in d1[str(j)]['benz']:
                if d4[j] < int(d1[str(j)]['max']):
                    if d4[j] < mini:
                        hil = j
                        mini = d4[j]
                        d4[j] += 1
                        print(' В', back_time(i), 'новый клиент: ', back_time(i), d2[i]['benz'], d2[i]['V'],
                              d2[i]['time_to_stop'],
                              'встал в очередь к автомату №', j)
                        d6[j].append(i)
                        condition = 1
                        d5[d2[i]['benz']] += int(d2[i]['V'])
                        d2[i].update({'station': j})
                        count_ozhid = 0
                        if len(d6[j]) == 1:
                            time1 = d2[d6[j][0]]['time_to_go']
                        if len(d6[j]) > 1:
                            time1 = d2[d6[j][0]]['time_to_go']
                            its_time_to_go[i] = time1
                            count_ozhid = d2[d6[j][0]]['time_to_stop']
                            for f in range(1, len(d6[j])):
                                r = d6[j][f]
                                count_ozhid += d2[r]['time_to_stop']
                                time1 = d6[j][0] + count_ozhid
                                d2[d6[j][f]]['time_to_go'] = time1
                        its_time_to_go[i] = time1
                        break

        if condition == 0:
            print(' В', back_time(i), 'новый клиент: ', back_time(i), d2[i]['benz'], d2[i]['V'], d2[i]['time_to_stop'],
                  'не смог заправить автомобиль и покинул АЗС.')
            queue += 1
        for k in range(1, value + 1):
            print('Автомат №', k, 'максимальная очередь:', d1[str(k)]['max'], 'Марки бензина:', *(d1[str(k)]['benz']),
                  '->', '*' * d4[k])

    if i in its_time_to_go.values():
        for n, m in its_time_to_go.items():
            if m == i:
                for o, p in d6.items():
                    if n in p:
                        d6[o].remove(n)
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
