from bot4binance import settings
import datetime
from binance import Client

client = Client(settings.APIKEY, settings.SECRET)
trades = client.get_my_trades(symbol='IOTABTC')

for trade in trades:
    etime = int(trade['time']) / 1000
    tradetime = datetime.datetime.fromtimestamp(etime)
    print("Time: {} | Price: {} | Quantity: {} | Commission: {}".format(
                                                            str(tradetime),
                                                          trade['price'],
                                                            trade['qty'],
                                                    trade['commission']))