from datetime import datetime, timedelta, date
import time

house = [
    "10 комнат и больше-к. квартира, 329,3 м², 2/5 эт. в Санкт-Петербурге",
    "52190000",
    "Загородный пр-т, 17",
    "Звенигородская,  400 м",
    "ksjdhflj rlsfjgljdx",
    "https://www.avito.ru/sankt-peterburg/kvartiry/10_komnat_i_bolshe-k._kvartira_3293m_25et._2361309916",
    "Агентство",
    "18 часов назад"
]

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