import pandas as pd
import numpy as np


class Number:
    def __init__(self) -> None:
        self.number_table_df = pd.read_csv('number_table.csv')
        self.position_table_df = pd.read_csv('position.csv')

    @property
    def number_table(self):
        return self.number_table_df


class NepaliNumber(Number):
    """Return english number into nepali number and word"""

    def __init__(self) -> None:
        super().__init__()

    def get_nepali_number(self, number) -> str:
        row = self.number_table_df[self.number_table_df['Numbers in English script'] == number]
        return row['Nepali Numbers'].values[0]

    def get_nepali_number_in_roman(self, number) -> str:
        row = self.number_table_df[self.number_table_df['Numbers in English script'] == number]
        return row['Nepali Numbers'].values[0]

    def get_nepali_number_in_devnagiri(self, number) -> str:
        row = self.number_table_df[self.number_table_df['Numbers in English script'] == number]
        return row['Nepali Numbers in Devnagiri'].values[0]

    def get_english_number(self, number) -> str:
        row = self.number_table_df[self.number_table_df['Numbers in English script'] == number]
        return row['Nepali Numbers'].values[0]

    def get_nepali_number_pronounciation(self, number) -> str:
        row = self.number_table_df[self.number_table_df['Numbers in English script'] == number]
        return row['Nepali Numbers'].values[0]

    def english_number_to_nepali_number(self, number) -> str:
        nepali_number = ""
        number_str = str(number)
        for i in number_str:
            nepali_number += self.get_nepali_number(int(i))
        return nepali_number

    def english_number_to_nepali_word(self, number, amount=True) -> str:
        nepali_word = ""
        number_str = str(number).split(".")  # split number by decimal
        if len(number_str) == 2:
            number = int(number_str[0])
            decimal = int(number_str[1][:2])
        else:
            decimal = 0
        if number == 0:
            return "शुन्य"
        if number // 100000000000 > 0:
            nepali_word += self.get_nepali_number_in_devnagiri(number // 100000000000) + " खर्ब "
            number = number % 100000000000
        if number // 1000000000 > 0:
            nepali_word += self.get_nepali_number_in_devnagiri(number // 1000000000) + " अर्ब "
            number = number % 1000000000
        if number // 10000000 > 0:
            nepali_word += self.get_nepali_number_in_devnagiri(number // 10000000) + " करोड "
            number = number % 10000000
        if number // 100000 > 0:
            nepali_word += self.get_nepali_number_in_devnagiri(number // 100000) + " लाख "
            number = number % 100000
        if number // 1000 > 0:
            nepali_word += self.get_nepali_number_in_devnagiri(number // 1000) + " हजार "
            number = number % 1000
        if number // 100 > 0:
            nepali_word += self.get_nepali_number_in_devnagiri(number // 100) + " सय "
            number = number % 100
        if number < 100 and number > 0:
            nepali_word += self.get_nepali_number_in_devnagiri(number)
        if decimal > 0:
            nepali_word += " दशमलव "
            for des in str(decimal):
                nepali_word += " " + self.get_nepali_number_in_devnagiri(int(des))
        return nepali_word



print(NepaliNumber().english_number_to_nepali_number(100002))
print(NepaliNumber().english_number_to_nepali_word(242424.456))