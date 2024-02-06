from backtesting import Backtest, Strategy
from datetime import datetime
from dateutil.relativedelta import relativedelta
import yfinance
from .const import DataEnum

class DeontayStrat(Strategy):
    EXCLUSIVE_ORDERS = False

    def init(self):
        pass

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
    

    # for each of the follow functions, check if data in cache and read -- read last available date in cache if data not there
    # should have analytics object -- do not read from cached backtest obj
    # do not implement in child classes, this should be scale for all of them as long as analytics object is consistent
    @staticmethod
    def data():
        return {
            DataEnum.OFFSETS: DeontayStrat.offsets(),
            DataEnum.ANALYTICS: DeontayStrat.analytics(),
            DataEnum.TIMESERIES: DeontayStrat.timeseries(),
            DataEnum.TRADES: DeontayStrat.trades()
        }
    
    @staticmethod
    def offsets():
        return ["All", "1Y", "6M", "1M"]
    
    @staticmethod
    def analytics():
        return {
                DataEnum.NOMINAL_RETURNS: {"All": 17585.15, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                DataEnum.PERCENTAGE_RETURNS: {"All": -0.25, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                DataEnum.SHARPE_RATIO: {"All": 3.7, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                DataEnum.MAX_DRAWDOWN: {"All": 9.84, "1Y": 27.2, "6M": 2.0, "1M": 0}
        }
    
    @staticmethod
    def timeseries():
        return { "All": [
                ["Day", "", "", "", ""],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
              ]
            }
    
    @staticmethod
    def trades():
        return []

    def backtest(self, startDate="", cash=100000, commission=0.002):
        startDate = startDate or (datetime.now() - relativedelta(years=5)).strftime("%Y-%m-%d")
        marketData = yfinance.download(self.ASSET, start=startDate) # check if market data in cache
        res = Backtest(marketData, self, cash=cash, commission=commission, exclusive_orders=self.EXCLUSIVE_ORDERS)
        return res.run()