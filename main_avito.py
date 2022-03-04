from bs4 import BeautifulSoup
import re
import requests
from requests import get


def main():
    print("--- START PROGRAM ---")
    houses = []
    count = 1

    while count <= 1:
        house = []

        # url_next = f'{url}' + str(count)
        # print(url_next + '\n\n')
        # response = get(url_next)
        with open('file/test_html_avito.txt', 'r', encoding='utf-8') as html:
            response = html.read()
        html_soup = BeautifulSoup(response, 'lxml')
        house_data = html_soup.find_all('div', class_='iva-item-body-KLUuy')
        print('\n' + '=' * 100 + f' (СТРАНИЦА: {count} )\n')
        for house in house_data:
            # харктеристика
            print(house.a['title'].split())
            # # цена
            print(house.find('meta', itemprop="price")['content'])
            # адрес
            print(house.find('span', class_=cl_address).text)
            # район
            try:
                print(house.find('div', class_=cl_district).text)
            except AttributeError:
                print('нет')
            # Описание
            # try:
            #     print(house.find('div', class_=cl_description).text)
            # except AttributeError:
            #     print("нет описания")
            # сылка
            print('https://www.avito.ru' + house.a['href'])
            # Кто продает
            try:
                print(house.find('div', class_=cl_agent).text)
            except AttributeError:
                try:
                    print(house.find('span', class_=cl_agent_2).text)
                except AttributeError:
                    print('Собственик')
            # время
            print(house.find('div', class_=cl_time).text)
            #
            print('-' * 50)

        if not house_data:
            print('- конец -')
            break

        count += 1


if __name__ == "__main__":
    url = "https://www.avito.ru/petrozavodsk/kvartiry/prodam-ASgBAgICAUSSA8YQ?p="
    cl_address = "geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL"
    cl_district = "geo-georeferences-SEtee text-text-LurtD text-size-s-BxGpL"
    cl_description = "iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL"
    cl_agent = "iva-item-text-Ge6dR iva-item-hideWide-_C9JT text-text-LurtD text-size-s-BxGpL"
    cl_agent_2 = "iva-item-text-Ge6dR iva-item-textColor-gray44-S6NCQ " \
                 "iva-item-hideWide-_C9JT text-text-LurtD text-size-s-BxGpL"
    cl_time = "date-text-KmWDf text-text-LurtD text-size-s-BxGpL text-color-noaccent-P1Rfs"

    main()
