from datetime import datetime, timedelta, date
from oop_avito import AvitoParserHouse
import pandas as pd
import os


class ApartmentDataFrame(AvitoParserHouse):
    """
       __data_typing():
       Уберает лишние, переводит в числа данные по каждой квартире.
    """

    def __init__(self, my_url, my_headers, test=False):
        super().__init__(my_url, my_headers, test)
        self._data_typing()

    def _data_typing(self):

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
            'price': [],
        }
        i = 0
        for house in self.houses_list:
            i += 1
            print(i)
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

                if 'мин' in date_str:
                    return str(datetime.now().date())
                elif 'час' in date_str:
                    return str(datetime.now().date() - timedelta(hours=int(date_str.split(' ')[0])))
                elif 'день' in date_str or 'дн' in date_str:
                    return str(datetime.now().date() - timedelta(days=int(date_str.split(' ')[0])))
                elif 'нед' in date_str:
                    return str(datetime.now().date() - timedelta(weeks=int(date_str.split(' ')[0])))
                elif 'назад' not in date_str:
                    date_str = int_value_from_ru_month(date_str)
                    return str(date(datetime.now().year, int(date_str.split(' ')[1]), int(date_str.split(' ')[0])))

            house[0] = house[0].split()

            if (len(house[0]) == 8 or len(house[0]) == 9) and 'студ' not in house[0][0]:
                if 'Своб' in house[0][0]:
                    df['room'].append(0)
                else:
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

        for v, k in df.items():
            print('len -' + v + '- :' + str(len(k)))

        pd_df = pd.DataFrame(df)

        name_file = 'df_' + str(datetime.now().date()) + '_SPB.csv'
        out_dir = './file/csv'
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        fullname = os.path.join(out_dir, name_file)
        pd_df.to_csv(fullname, index=False)

        self.apartment_df = pd_df

        print('DF to .csv -> OK')


if __name__ == "__main__":
    url = "https://www.avito.ru/sankt-peterburg/kvartiry/prodam-ASgBAgICAUSSA8YQ?p="
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/36.0.1985.125 Safari/537.36',
        'upgrade-insecure-requests': '1'
    }
    data_houses = ApartmentDataFrame(url, headers, test=True)

    # ТЕСТЫ
    #
    # print(f'Количество квартир = {len(data_houses.houses_list)}')
    # print(data_houses.houses_list[0])
    # for i in data_houses.houses_list:
    #     print(len(i))
    # print(data_houses.apartment_df)
