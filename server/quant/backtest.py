from backtesting import Backtest, Strategy
from datetime import datetime
from dateutil.relativedelta import relativedelta
import yfinance

class DeontayStrat(Strategy):
    EXCLUSIVE_ORDERS = False
    def init(self):
        pass

    def backtest(self, startDate="", cash=100000, commission=0.002):
        startDate = startDate or (datetime.now() - relativedelta(years=5)).strftime("%Y-%m-%d")
        marketData = yfinance.download(self.ASSET, start=startDate)
        res = Backtest(marketData, self, cash=cash, commission=commission, exclusive_orders=self.EXCLUSIVE_ORDERS)
        return res.run()