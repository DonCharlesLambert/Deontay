from backtesting import Backtest, Strategy
from datetime import datetime
from dateutil.relativedelta import relativedelta
import yfinance

class DeontayStrat(Strategy):
    EXCLUSIVE_ORDERS = False

    @staticmethod
    def init():
        raise NotImplementedError("Cannot call init func from DeontayStrat, implement method in subclass")

    @staticmethod
    def name():
        raise NotImplementedError("Cannot call name func from DeontayStrat, implement method in subclass")

    @staticmethod
    def image():
        raise NotImplementedError("Cannot call image func from DeontayStrat, implement method in subclass")
    
    @staticmethod
    def description():
        return NotImplementedError("Cannot call description func from DeontayStrat, implement method in subclass")
    
    @staticmethod
    def data():
        return NotImplementedError("Cannot call data func from DeontayStrat, implement method in subclass")

    def backtest(self, startDate="", cash=100000, commission=0.002):
        startDate = startDate or (datetime.now() - relativedelta(years=5)).strftime("%Y-%m-%d")
        marketData = yfinance.download(self.ASSET, start=startDate)
        res = Backtest(marketData, self, cash=cash, commission=commission, exclusive_orders=self.EXCLUSIVE_ORDERS)
        return res.run()