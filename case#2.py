from random import randint


def time(hours):
    h, m = hours.split(':')
    minutes = int(h) * 60 + int(m)
    return minutes

def back_time(minutes):
    h=minutes//60
    m=minutes-h*60
    phrase = str(h)+':'+str(m)
    return(phrase)

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
print(d1)

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
print(d3)

# Queue.
d4 = {}
d4[1] = 0
d4[2] = 0
d4[3] = 0
print(d4)

its_time_to_go = {}
queue = 0
# Ставлю в очередь без учета очереди.
for i in range(1440):
    condition = 0
    if i in d2.keys():
        for j in range(1, value + 1):
            patrol = d2[i]['benz']
            if patrol in d1[str(j)]['benz']:
                if d4[j] < int(d1[str(j)]['max']):
                    d4[j] += 1
                    print(' В', back_time(i), 'новый клиент: ', back_time(i), d2[i]['benz'], d2[i]['V'], d2[i]['time_to_stop'],
                          'встал в очередь к автомату №', j)
                    condition = 1
                    d2[i].update({'station': j})
                    just = d2[i]['time_to_go']
                    its_time_to_go[just] = i
                    break
        if condition == 0:
            print(' В', back_time(i), 'новый клиент: ', back_time(i), d2[i]['benz'], d2[i]['V'], d2[i]['time_to_stop'],
                  'не смог заправить автомобиль и покинул АЗС.')
            queue += 1  # Сколько покинуло
        for k in range(1, value + 1):
            print('Автомат №', k, 'максимальная очередь:', d1[str(k)]['max'], 'Марки бензина:', d1[str(k)]['benz'],
                  '->', '*' * d4[k])

    if i in its_time_to_go.keys():
        what_we_need = its_time_to_go[i]
        l = d2[what_we_need]['station']
        d4[l] -= 1
        print(' В', back_time(i), 'клиент: ', back_time(what_we_need), d2[what_we_need]['benz'], d2[what_we_need]['V'], d2[what_we_need]['time_to_stop'],
              'заправил свой автомобиль и покинул АЗС.')
        for k in range(1, value + 1):
            print('Автомат №', k, 'максимальная очередь:', d1[str(k)]['max'], 'Марки бензина:', d1[str(k)]['benz'],
                  '->', '*' * d4[k])


print(d2)
print ('Из-за очередей было потеряно', queue, 'человека.') #тут можно исправить падеж или формулировку