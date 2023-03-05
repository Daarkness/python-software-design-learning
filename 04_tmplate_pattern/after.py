from abc import ABC,abstractmethod

from typing import List

class TradingBot(ABC):

    # 不是单一指责
    def connect(self):
        print(f"Connecting to Crypto exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]

    def check_prices(self, coin: str):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")


    #抽象子类需要实现的方法
    @abstractmethod
    def should_buy(self, prices: List[float]) -> bool:
        ...
    @abstractmethod
    def should_sell(self, prices: List[float]) -> bool:
        ...




class AverageTrader(TradingBot):
    # 实现不同的功能

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)

class MinMaxTrader(TradingBot):

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)


application = MinMaxTrader()
#如果需要扩展 重写一个抽象子类即可，并不影响其他代码
application.check_prices("BTC/USD")
