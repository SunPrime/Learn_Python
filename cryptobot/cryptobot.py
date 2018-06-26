import socket, time, json, os, psycopg2.extras
from binance.client import Client
from telegram_bot import send_message


def get_current_price():
    array_price = {}
    prices = client.get_all_tickers()
    for coin in prices:
        symbol = coin['symbol']
        price = float(coin['price'])
        array_price[symbol] = price
    return array_price


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client = Client(os.environ['BINANCE_APIKEY'], os.environ['BINANCE_SECRET'])

connect = psycopg2.connect(host='127.0.0.1', port=5432, database='crypto_bot', user='postgres', password='Helen77')

previous = get_current_price()

while True:
    messages = []

    current = get_current_price()

    result = 0.0

    for key, value in current.items():
        if value < previous[key]:
            result = (value - previous[key]) / previous[key]
            if result < -0.005:
                value = key + ': ' + str(current[key]) + ' ' + str(round(result * 100, 2)) + '%'
                messages.append(value)

    now = int(time.time())
    sql = ("""insert into binance_bot(time, data) values (%s, %s::json)""")
    cursore = connect.cursor()
    cursore.execute(sql,(now, json.dumps(current)))
    connect.commit()

    send_message(messages)

    time.sleep(35)

    previous = current

connect.close()
