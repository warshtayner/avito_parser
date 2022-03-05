from bs4 import BeautifulSoup
from datetime import datetime
from requests import get
import json


class AvitoParserApartment:
    """
    AvitoParserHouse:
        Скрапинг даных с сайта Avito.ru по адресу кокретного запроса.

    __parsing_pages():
        Возвращает двухмерный список данных по каждой квартире ввиде строк.

    __data_typing():
        Убирает лишние переводит в числа данные по каждой квартире.

    """

    def __init__(self, test=False):
        if test:
            with open('file/houses_list_2022-03-04_21-44.json', 'r', encoding="utf-8") as fd:
                self.apartment_list = json.load(fd)
                print('Читаем с файла ((( РЕЖИМ ТЕСТ )))')
        else:
            self._parsing_pages(test=True)

    def _parsing_pages(self, test=False):
        # Переменные для парсинга
        url = "https://www.avito.ru/petrozavodsk/kvartiry/prodam-ASgBAgICAUSSA8YQ?p="
        _cl_address = "geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL"
        cl_district = "geo-georeferences-SEtee text-text-LurtD text-size-s-BxGpL"
        cl_description = "iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL"
        cl_agent = "iva-item-text-Ge6dR iva-item-hideWide-_C9JT text-text-LurtD text-size-s-BxGpL"
        cl_agent_2 = "iva-item-text-Ge6dR iva-item-textColor-gray44-S6NCQ " \
                     "iva-item-hideWide-_C9JT text-text-LurtD text-size-s-BxGpL"
        cl_time = "date-text-KmWDf text-text-LurtD text-size-s-BxGpL text-color-noaccent-P1Rfs"
        houses = []
        page = 1

        # В цикле парсим по одной странице
        while True:

            # На случай проблем с "requests"
            if test:
                with open('file/test_html_avito.txt', 'r', encoding='utf-8') as html:
                    response = html.read()
                soup = BeautifulSoup(response, 'lxml')
            else:
                url_next = f'{url}' + str(page)
                response = get(url_next)
                soup = BeautifulSoup(response.text, 'lxml')

            # Ищем  все квартиры на странице
            house_list_ml = soup.find_all('div', class_='iva-item-body-KLUuy')

            # Снимаем данные по одной кв.
            for house_ml in house_list_ml:
                # [харктеристика, цена, адрес]
                tmp = [(house_ml.a['title']), house_ml.find('meta', itemprop="price")['content'],
                       house_ml.find('span', class_=_cl_address).text]
                # район
                try:
                    tmp.append(house_ml.find('div', class_=cl_district).text)
                except AttributeError:
                    tmp.append('')
                # Описание
                try:
                    tmp.append(house_ml.find('div', class_=cl_description).text)
                except AttributeError:
                    tmp.append('')
                # сылка
                tmp.append('https://www.avito.ru' + house_ml.a['href'])
                # Кто продает
                try:
                    tmp.append(house_ml.find('div', class_=cl_agent).text)
                except AttributeError:
                    try:
                        tmp.append(house_ml.find('span', class_=cl_agent_2).text)
                    except AttributeError:
                        tmp.append('Собственик')
                # время
                tmp.append(house_ml.find('div', class_=cl_time).text)
                # Итог
                houses.append(tmp)

            # выходим если нет объявлений
            if not house_list_ml or test:
                print('- конец -')
                break

            # номер страницы
            page += 1

        # создаем атрибут
        self.apartment_list = houses

        # сохраняем в файл
        name_file = 'file/houses_list_' + str(datetime.now())[:16].replace(':', '-').replace(' ', '_') + '.json'
        with open(name_file, 'w', encoding="utf-8") as out_f:
            json.dump(houses, out_f)

        print('- парсинг выполнен -')

    # def __data_typing(self, test=False):


if __name__ == "__main__":
    data_houses = AvitoParserApartment()

    # ТЕСТЫ
    #
    print(f'Количество квартир = {len(data_houses.apartment_list)}')
    print(data_houses.apartment_list[0])
    for i in data_houses.apartment_list:
        print(len(i))
