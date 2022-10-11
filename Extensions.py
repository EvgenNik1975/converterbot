import json
import requests
from config import *




class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = dict[base.lower()]
        except KeyError:
            raise APIException(f'Валюта {base} не найдена!')
        try:
            sym_key = dict[sym.lower()]
        except KeyError:
            raise APIException(f'Валюта {sym} не найдена!')
        if base == sym:
            raise APIException(f'Нелзя обработать одинаковые параметры!')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Некорректный ввод количества!')

        url = (
            f"https://api.apilayer.com/exchangerates_data/latest?symbols={sym_key}&base={base_key}")

        output = {}

        response = requests.request("GET", url, headers=headers, data=output)
        resp = json.loads(response.content)
        price = resp['rates'][sym_key]
        new_price = price * float(amount)
        message = f'{amount} {base} стоит {new_price} {sym}'

        return message
