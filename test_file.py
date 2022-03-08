from datetime import datetime, timedelta, date
import time

house = ['Квартира-студия, 32 м², 3/11 эт. в Петрозаводске',
             '3700000',
             'Пограничная ул., 54',
             'р-н Сулажгора',
             'В продаже однокомнатная квартира на 4-м этаже 5-ти этажного кирпичного дома с большой кухней, общей'
             ' площадью 40,8 кв. М. (+ балкон 2,8 кв. М.).\n\n· Пластиковые окна.\n\n· Санузел совмещенный'
             ' (кафель).\n\n· Большая кухня 11,5 кв. М. \n\n· Кухонный гарнитур остается будущему владельцу'
             ' квартиры.\n\n· Видеонаблюдениевокруг всего дома.\n\n· Небольшие коммунальные платежи.\n\n· Чистый'
             ' подъезд.\n\n· Всегда есть парковочные места.\n\n· Остановка в шаговой доступности (50 м).\n\n·'
             ' Идеальный вариант въехать и жить.\n\nОбременения и долги отсутствуют! \n\nКирпичный дом обладает'
             ' огромным количеством преимуществ, главные из которых: отличная тепло и звукоизоляция, а также'
             ' рациональная планировка квартиры. \n\nВопреки расхожему мнению об удаленности района от центра'
             ' города расположение дома имеет много преимуществ\xa0— неподалеку школа № 12, детский сад №22.'
             ' В шаговой доступности детская поликлиника, больница, отделение Сбербанка, почта, «Магнит», «Пятерочка»,'
             ' «Сигма у дома», стоматология, аптека, салон красоты, парикмахерская, магазин для дачников,'
             ' частный детский сад, ТЦ «Сулажгорский», большая детская площадка с ограждением, дворец спорта'
             ' «Коралл» (секции для детей и взрослых), а также остановка общественного транспорта (более 12 маршрутов'
             ' в разные концы города, регулярно №2, №3, №5, №9, №15), питомник (большая территория для прогулок'
             ' и отдыха, лесо-парковая зона), ламба, родник, горка для катания зимой. \n\nПробок нет\xa0— три'
             ' ветки доступа в город (через переезд, 5-й посёлок, объездная дорога).\n\nЛеруа Мерлен и Лотос Plaza,'
             ' Сигма в 10 мин. На автомобиле по Объездной.',
             'https://www.avito.ru/petrozavodsk/kvartiry/1-k._kvartira_408m_45et._2318495042',
             'Застройщик',
             '7 февраля 13:10']

ru_month = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12,
    }


def int_value_from_ru_month(date_str):
    for k, v in ru_month.items():
        date_str = date_str.replace(k, str(v))

    return date_str


def get_data_start(date_str):

    if date_str.find('мин') != -1:
        return str(datetime.now().date())
    elif date_str.find('час') != -1:
        return str(datetime.now().date() - timedelta(hours=int(date_str.split(' ')[0])))
    elif date_str.find('день') != -1 or date_str.find('дн') != -1:
        return str(datetime.now().date() - timedelta(days=int(date_str.split(' ')[0])))
    elif date_str.find('нед') != -1:
        return str(datetime.now().date() - timedelta(weeks=int(date_str.split(' ')[0])))
    elif date_str.find('назад') == -1:
        date_str = int_value_from_ru_month(date_str)
        return str(date(datetime.now().year, int(date_str.split(' ')[1]), int(date_str.split(' ')[0])))


df = {
    'room': [],
    'size': [],
    'floor': [],
    'total_floors': [],
    'address': [],
    'area': [],
    'agent': [],
    'start_time': [],
    'url': [],
    'Description': [],
    'price': []
}
house[0] = house[0].split()
print(house[0])

if len(house[0]) == 8:
    df['room'].append(int(house[0][0][:-3]))
    df['size'].append(float(house[0][2].replace(',', '.')))
    df['floor'].append(int(house[0][4].split('/')[0]))
    df['total_floors'].append(int(house[0][4].split('/')[1]))
else:
    df['room'].append(0)
    df['size'].append(float(house[0][1].replace(',', '.')))
    df['floor'].append(int(house[0][3].split('/')[0]))
    df['total_floors'].append(int(house[0][3].split('/')[1]))

df['address'].append(house[2])
df['area'].append(house[3])
df['agent'].append(house[6])
df['start_time'].append(get_data_start(house[7]))
df['url'].append(house[5])
df['Description'].append(house[4])
df['price'].append(int(house[1]))



print(df)
