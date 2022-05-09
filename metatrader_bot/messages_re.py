# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
import re
import locale

from dataclasses import dataclass

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

regex = r"NOVO\s+SINAL\s+ordem\s*(?P<ordem>compra|venda):\s*criptomoeda:\s+(?P<cripto>.*)\s*entrada:\s*(?P<entrada>[0-9]+\.[0-9]{2})\s*stop:\s*(?P<stop>[0-9]+\.[0-9]{2})\s*alvo:\s*(?P<alvo>[0-9]+\.[0-9]{2})"

test_str = "NOVO SINAL ordem compra: criptomoeda: BTCUSDentrada:  36288.59stop: 36203.29alvo: 36354.59"
# test_str = 'NOVO SINAL ordem venda: criptomoeda: BTCUSDentrada:  36288.59stop: 36203.29alvo: 36354.59'


@dataclass
class Signal:
    ordem: str
    cripto: str
    entrada: float
    stop: float
    alvo: float


def get_match_dict(str_to_match) -> Signal:
    match = re.match(regex, str_to_match, re.MULTILINE | re.IGNORECASE)
    if match:
        print('Found a match!')
        return Signal(**match.groupdict())


def convert_signal(signal: Signal):
    ordem_icon = '⬆️' if signal.ordem.lower() == 'compra' else '⬇️'

    return f'⚠️ NOVO SINAL ⚠️\n\n💰 Criptomoeda: {signal.cripto}\n{ordem_icon} Ordem: {signal.ordem.capitalize()}\n🚀 Entrada: {locale.currency(float(signal.entrada), symbol=False, grouping=True)}\n🛑 Stop: {locale.currency(float(signal.stop), symbol=False, grouping=True)}\n🎯 Alvo: {locale.currency(float(signal.alvo), symbol=False, grouping=True)}'


if __name__ == '__main__':
    new_signal = get_match_dict(test_str)
    print(convert_signal(new_signal))
