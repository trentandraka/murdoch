from binance.client import Client
from binance.exceptions import BinanceAPIException
from binance.websockets import BinanceSocketManager
from binance.enums import *
from api_key import api_key

client = Client(api_key['api_key'], api_key['api_secret'])
symbol = 'BNBBTC'

# [
#     [
#         1499040000000,      # Open time
#         "0.01634790",       # Open
#         "0.80000000",       # High
#         "0.01575800",       # Low
#         "0.01577100",       # Close
#         "148976.11427815",  # Volume
#         1499644799999,      # Close time
#         "2434.19055334",    # Quote asset volume
#         308,                # Number of trades
#         "1756.87402397",    # Taker buy base asset volume
#         "28.46694368",      # Taker buy quote asset volume
#         "17928899.62484339" # Can be ignored
#     ]
# ]

if __name__== "__main__":
    bm = BinanceSocketManager(client)
    # order = client.order_market_buy(
    #     symbol=symbol,
    #     quantity=100)
    # klines = candles
    candles = client.get_historical_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE, start_str='1 hour ago UTC')
    print(candles)

# rsi = 14 days
# bollinger bands length = 20 days
# middle = 20 day sma
# each value is from the CLOSING price on the candle

# have array of last 20 values
# every min, delete back, add to front
# loop
