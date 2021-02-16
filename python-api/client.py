# please consider using python3

import random
import requests

class Coinbae(object):
    headers = {'content-type': 'application/json'}
    base_params = {"jsonrpc": "2.0", "id": 0}
    
    SELL_STR = "SELL"
    BUY_STR = "BUY"
    
    def __init__(self, exchange_url, _use_first_random_op_id=True):
        self.exchange_url = exchange_url
        
        # operation id should be unique for each operation
        self._op_id = 0
        if _use_first_random_op_id:
            self._op_id = random.randint(0, 1000000)
        

    def _execute(self, method, params):
        return requests.post(
            self.exchange_url, 
            json={
                "method": method, 
                "params": params,
                **self.base_params},
            headers=self.headers
        ).json()
    
    def _get_side_code(self, side):
        _side = 1 if side == self.SELL_STR else 2 if side == self.BUY_STR else 0
        if _side == 0:
            raise Exception("Only 'side={}' and 'side={}' allowed.".format(self.SELL_STR, self.BUY_STR))
        return _side
    
    def balance_query(self, user_token, asset=None):
        if asset is None:
            return self._execute("balance.query", [user_token])
        return self._execute("balance.query", [user_token, asset])
    
    def balance_history(
            self, 
            user_token, 
            asset="BTC", 
            business_type="", 
            start_time=0, 
            end_time=0, 
            offset=0, 
            limit=10
        ):
        return self._execute(
            "balance.history", 
            [user_token, asset, "", start_time, end_time, offset, limit]
        )
    
    def asset_list(self):
        return self._execute("asset.list", [])
    
    def asset_summary(self):
        return self._execute("asset.summary", [])
    
    def order_put_limit(
            self, 
            user_token, 
            market="ANKERBTC", 
            side="SELL", 
            amount=100, 
            price=1, 
            taker_fee_rate=0.0001, 
            maker_fee_rate=0.0001, 
            source=""
        ):
        _side = self._get_side_code(side)
        return self._execute(
            "order.put_limit", 
            [user_token, market, _side, str(amount), str(price), 
            str(taker_fee_rate), str(maker_fee_rate), source]
        )
    
    def order_put_market(self, user_token, market, side, amount, maker_fee_rate=0, source=""):
        _side = self._get_side_code(side)
        return self._execute(
            "order.put_market", 
            [user_token, market, _side, str(amount), str(maker_fee_rate), source]
        )
        
    def order_cancel(self, user_token, market, order_id):
        return self._execute("order.cancel", [user_token, market, order_id])
        
    def futures_cancel(self, user_token, market, order_id):
        return self._execute("futures.cancel", [user_token, market, order_id])
        
    def order_deals(self, order_id=1, offset=0, limit=10):
        return self._execute("order.deals", [order_id, offset, limit])
        
    def order_book(self, market="ANKERBTC", limit=10, side="SELL"):
        raise Exception("Official docs are wrong. See: https://github.com/viabtc/viabtc_exchange_server/issues/123")  
#         _side = self._get_side_code(side)
#         return self._execute("order.book", [market, side, 0, limit])
    
    def order_depth(self, market="ANKERBTC", limit=10):
        return self._execute("order.depth", [market, limit, "0"])
        
    def order_pending(self, user_token, market='ANKERBTC', offset=0, limit=100):
        return self._execute("order.pending", [user_token, market, offset, limit])

    def futures_pending(self, user_token, market='ANKERBTC', offset=0, limit=100):
        return self._execute("futures.pending", [user_token, market, offset, limit])

    def order_pending_detail(self):
        raise Exception("Not Implemented") 

    def order_finished(self):
        raise Exception("Not Implemented") 

    def order_finished_detail(self):
        raise Exception("Not Implemented") 

    def market_last(self, market):
        return self._execute("market.last", [market])

    def market_deals(self, market, limit=10000, last_id=0):
        return self._execute("market.deals", [market, limit, last_id])

    def market_user_deals(self, user_token, market, offset, limit):
        raise Exception("Not Implemented") 

    def market_kline(self, market, start, end, interval):
        return self._execute("market.kline", [market, start, end, interval])

    def market_status(self, market="ANKERBTC", period=86400):
        return self._execute("market.status", [market, period])

    def market_status_today(self, market="ANKERBTC"):
        return self._execute("market.status_today", [market])

    def market_list(self):
        return self._execute("market.list", [])

    def market_summary(self, market):
        return self._execute("market.summary", [market])
