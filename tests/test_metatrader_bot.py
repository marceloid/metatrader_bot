from metatrader_bot import __version__
from metatrader_bot.messages_re import convert_signal, get_match_dict

TEST_MESSAGES = {
    'NOVO SINAL ordem compra: criptomoeda: ETHUSDentrada:  36288.59stop: 36203.29alvo: 36354.59': '⚠️ NOVO SINAL ⚠️\n\n💰 Criptomoeda: ETHUSD\n⬆️ Ordem: Compra\n🚀 Entrada: 36.288,59\n🛑 Stop: 36.203,29\n🎯 Alvo: 36.354,59',
    'NOVO SINAL ordem venda: criptomoeda: BTCUSDentrada:  36288.59stop: 36203.29alvo: 36354.59': '⚠️ NOVO SINAL ⚠️\n\n💰 Criptomoeda: BTCUSD\n⬇️ Ordem: Venda\n🚀 Entrada: 36.288,59\n🛑 Stop: 36.203,29\n🎯 Alvo: 36.354,59',
    'NOVO SINAL ordem compra: criptomoeda: BTCUSDentrada:  45000.59stop: 47000.29alvo: 50000.59': '⚠️ NOVO SINAL ⚠️\n\n💰 Criptomoeda: BTCUSD\n⬆️ Ordem: Compra\n🚀 Entrada: 45.000,59\n🛑 Stop: 47.000,29\n🎯 Alvo: 50.000,59',
}


def test_version():
    assert __version__ == '0.1.0'


def test_convert_signals():
    assert all(
        [
            TEST_MESSAGES[k] == convert_signal(get_match_dict(k))
            for k in TEST_MESSAGES.keys()
        ]
    )
