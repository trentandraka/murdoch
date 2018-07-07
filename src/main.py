from binance.client import Client
from api_key import api_key

client = Client(api_key['api_key'], api_key['api_secret'])

if __name__== "__main__":
    depth = client.get_order_book(symbol='BNBBTC')
    print(depth)

# rsi = 14 days
# bollinger bands length = 20 days
# middle = 20 day sma

# have array of last 20 values
# every min, delete back, add to front
# loop
