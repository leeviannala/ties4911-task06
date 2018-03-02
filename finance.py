import json
import requests


def getStockQuote(exchange, stock):
    exchange = exchange.strip().upper() + '+'
    stock = stock.strip().replace(' ', '+').upper()
    rsp = requests.get('https://finance.google.com/finance?q=' + exchange + stock + '&output=json')
    # Parse JSON response
    json_data = json.loads(rsp.content[6:-2].decode('unicode_escape'))
    return(json_data['name'] + ' (' + json_data['exchange'] + ': ' + json_data['symbol'] + ')\n' +
            'Current price: ' + json_data['l'] + ' (' + json_data['c'] + ', ' + json_data['cp'] + ' %)' + '\n' +
            'Opening price: ' + json_data['op'] + '\n' +
            'Day high: ' + json_data['hi'] + '\n' +
            'Day low: ' + json_data['lo'])

# print(getStockQuote('HEL', 'NOKIA'))
