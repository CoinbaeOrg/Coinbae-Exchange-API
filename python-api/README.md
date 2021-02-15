# Coinbae Exchange API 
## Python API Usage

The basic usage:

``` python
import Coinbae

exchange_url = "https://e.coinbae.org/api"
api = Coinbae(exchange_url)

resp = api.market_list()
market_names = [m["name"] for m in resp["result"]]
print("Exchange markets: ", market_names)

print()
print("Orderbooks:")
for market in market_names:
    ob = api.order_depth(market=market)
    print(market, ob["result"])
```
