print('Данная программа позволяет вычислить промежуток времени в зависимости от продолжительности в секундах ')
second = int(input('Введите количество секунд: '))
if second <= 3600:
    duration_min = second // 60
    duration_sec = (second / 60 - duration_min) * 60
    print('Продолжительность времени', second, 'будет: ', duration_min, 'минуты,', round(duration_sec), 'секунды')
if second >= 3600 and second <= 86400:
    duration_hour = second // 3600
    duration_min = (second / 3600 - duration_hour)*60
    duration_sec = (duration_min - int(duration_min))*60
    print('Продолжительность времени', second,'будет: ', round(duration_hour), 'час', int(duration_min), 'минут',
    round(duration_sec), 'секунд')
if second > 86400:
    duration_day = second // 86400
    duration_hour = (second / 86400 - duration_day)*24
    duration_min = (duration_hour - int(duration_hour))*60
    duration_sec = (duration_min - int(duration_min))*60
    print('Продолжительность времени', second, 'будет: ', round (duration_day), 'дней', round(duration_hour),
    'час', int(duration_min), 'минут',round(duration_sec), 'секунд')

