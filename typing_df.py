from oop_avito import AvitoParserHouse
import pandas as pd


class ApartmentDataFrame(AvitoParserHouse):

    def __init__(self, test=False):
        super().__init__(test)
        self._data_typing()

    def _data_typing(self):
        df = pd.DataFrame({
            'room': [],
            'size': [],
            'floor': [],
            'total floors': [],
            'address': [],
            'area': [],
            'agent': [],
            'start_time': [],
            'Description': []
        })

        for house in self.houses_list:
            house[0] = house[0].split()
            if len(house[0]) == 6:
                df['room'].append(int(house[0][:-3]))

        self.apartment_df = df

# if __name__ == "__main__":
#     data_houses = ApartmentDataFrame()
#
#     # ТЕСТЫ
#     #
#     print(f'Количество квартир = {len(data_houses.houses_list)}')
#     print(data_houses.houses_list[0])
#     for i in data_houses.houses_list:
#         print(len(i))