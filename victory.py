''' В.И Ленин 1870 гр, Марк Твен 1835 гр, Исаак Ньютон 1643 гр, Людвиг VI 1328 гр, Рюрик 830 гр'''
zn = ['В И Ленин', 'Марк Твен', 'Исаак Ньютон', 'Людвиг VI', 'Рюрик']
age_zn = [1870, 1835, 1643, 1328, 830]
pr = 'Да' or 'да'
cou = 0

while pr == 'Да' or 'да':
    for i in range(len(zn)):
        print(f'В каком году родился: {zn[i]}')
        if int(input()) == age_zn[i]:
            cou += 1
    print(f'Количество правильных ответов: {cou}')
    print(f'Количество ошибок: {len(zn) - cou}')
    print(f'Процент правильных ответов: {cou * (100 / len(zn))}')
    print(f'Процент неправильных ответов: {(len(zn) - cou) * (100 / len(zn))}')
    pr = input('=============================\nНачать игру сначала? (Да/...) ')
