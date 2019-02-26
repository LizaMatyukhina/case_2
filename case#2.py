from random import randint
from ru_local import *


def time(hours):
    """Counting the number of minutes."""
    h, m = hours.split(':')
    minutes = int(h) * 60 + int(m)
    return minutes


def back_time(minutes):
    """Determining the time."""
    h = minutes // 60
    m = minutes - h * 60
    if h < 10:
        h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)
    phrase = str(h) + ':' + str(m)
    return phrase


def time_for_benz(volume):
    """Determining the time for gas station."""
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


d3 = {}
d3[AI_80] = 38
d3[AI_92] = 41
d3[AI_95] = 44
d3[AI_98] = 49


colichestvo_kolonok = value
d4 = {}
d6 = {}
for n in range(1, colichestvo_kolonok+1):
    d4[n] = 0
    d6[n] = []


d5 = {}
d5[AI_80] = 0
d5[AI_92] = 0
d5[AI_95] = 0
d5[AI_98] = 0

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
                        print(V, back_time(i), NEW_CLIENT, back_time(i), d2[i]['benz'], d2[i]['V'],
                              d2[i]['time_to_stop'], QUEUE, j)
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
            print(V, back_time(i), NEW_CLIENT, back_time(i), d2[i]['benz'], d2[i]['V'], d2[i]['time_to_stop'],
                  COULD_NOT_FILL_THE_CAR)
            queue += 1
        for k in range(1, value + 1):
            print(MACHINE_NUMBER, k, MAX_QUEUE, d1[str(k)]['max'], GASOLINE_BRANDS, *(d1[str(k)]['benz']),
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
            print(V, back_time(i), CLIENT, back_time(arrive), d2[arrive]['benz'], d2[arrive]['V'],
                  d2[arrive]['time_to_stop'], FILLED_THE_CAR)
            for k in range(1, value + 1):
                print(MACHINE_NUMBER, k, MAX_QUEUE, d1[str(k)]['max'], GASOLINE_BRANDS,
                      *(d1[str(k)]['benz']),
                      '->', '*' * d4[k])
            its_time_to_go.pop(arrive)


print(TOTAL_LITERS)
for key in d5:
    print(key, ':', d5[key], sep='')
money = 0
our_patrol = [AI_80, AI_92, AI_98, AI_95]
for p in our_patrol:
    money += d5[p]*d3[p]
print(TOTAL_SUM, money)
print(LEFT_AZS, queue)
