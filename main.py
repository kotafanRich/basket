help = '''
-----------------------------------------------------------------
|  команда 'add' - добавить броски (two or three)               |
|  команда 'print 2' - вывести 2ух очковые броски за всё время  |
-----------------------------------------------------------------
'''

two = {
    'made': [],
    'attemp': []
}

three = {
    'made': [],
    'attemp': []
}




def add(shot, mades, attemps):
    if shot == 'two':
        two['made'].append(mades)
        two['attemp'].append(attemps)

    elif shot == 'three':
        three['made'].append(mades)
        three['attemp'].append(attemps)


print(help)
while True:
    command: str = input('введите команду: ')
    if command == 'add':
        shots = input('введите бросок: ')
        mades = int(input('очки - '))
        attemps = int(input('попытки - '))
        add(shots, mades, attemps)
        print('броски добавлены')

    elif command == 'print 2':
        s_made = 0
        s_attemp = 0
        for m, n in two.items():
            if m == 'made':
                s_made = sum(n)
            elif m == 'attemp':
                s_attemp = sum(n)
        proc_two = round(sum(two['made']) * 100 / sum(two['attemp']), 2)
        print(f'{s_made} из {s_attemp}. {proc_two}%')

    elif command == 'print 3':
        s_made = 0
        s_attemp = 0
        for m, n in three.items():
            if m == 'made':
                s_made = sum(n)
            elif m == 'attemp':
                s_attemp = sum(n)
        proc_three = round(sum(three['made']) * 100 / sum(three['made']), 2)
        print(f'{s_made} из {s_attemp}. {proc_three}%')

    elif command == 'help':
        print(help)
