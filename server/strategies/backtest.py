from backtesting import Backtest, Strategy
from datetime import datetime
from dateutil.relativedelta import relativedelta
import yfinance
from .const import DataEnum
import json
import pandas as pd

class DeontayStrat(Strategy):
    EXCLUSIVE_ORDERS = False

    def init(self):
        pass

class Deontay():
    def name(self):
        raise NotImplementedError("Cannot call name func from DeontayStrat, implement method in subclass")

    def image(self):
        raise NotImplementedError("Cannot call image func from DeontayStrat, implement method in subclass")
    
    def description(self):
        return NotImplementedError("Cannot call description func from DeontayStrat, implement method in subclass")
    
    def details(self):
        return NotImplementedError("Cannot call description func from DeontayStrat, implement method in subclass")
    
    def data(self):
        return NotImplementedError("Cannot call data func from DeontayStrat, implement method in subclass")
    
    def strategy(self):
        return NotImplementedError("Cannot call strategy func from DeontayStrat, implement method in subclass")

    def data(self):
        return {
            DataEnum.OFFSETS: self.offsets(),
            DataEnum.ANALYTICS: self.analytics(),
            DataEnum.TIMESERIES: self.timeseries(),
            DataEnum.TRADES: self.trades()
        }
    
    def offsets(self):
        return ["All", "1Y", "6M", "1M"]
    
    def analytics(self):
        return {
            DataEnum.NOMINAL_RETURNS: self.nominalReturns(),
            DataEnum.PERCENTAGE_RETURNS: self.percentageReturns(),
            DataEnum.SHARPE_RATIO: self.sharpeRatio(),
            DataEnum.MAX_DRAWDOWN: self.maxDrawdown()
        }
    
    def timeseries(self):
        return { 
            offset: self.offsetTimeseries(offset) for offset in self.offsets()
        }
    
    def nominalReturns(self):
        return self._readData("Nominal Returns")
    
    def percentageReturns(self):
        return self._readData("Percentage Returns")
    
    def sharpeRatio(self):
        return self._readData("Sharpe Ratio")
    
    def maxDrawdown(self):
        return self._readData("Max Drawdown")
        
    def offsetTimeseries(self, offset):
        timeseriesPath = self._cachePath(offset)
        timeseriesDf = pd.read_csv(timeseriesPath)
        cols = ['Date', 'Equity']
        equityCurve = timeseriesDf[cols]
        return [cols] + equityCurve.values.tolist()
    
    @staticmethod
    def trades():
        return []

    def backtest(self, startDate="", cash=100000, commission=0.002):
        strategy = self.strategy()
        startDate = startDate or (datetime.now() - relativedelta(years=5)).strftime("%Y-%m-%d")
        marketData = yfinance.download(strategy.ASSET, start=startDate) # check if market data in cache
        res = Backtest(marketData, strategy, cash=cash, commission=commission, exclusive_orders=strategy.EXCLUSIVE_ORDERS)
        return res.run()
    
    # CACHE
    def _readData(self, stratName):
        res = self._read(stratName)
        return json.loads(res)

    def _cachePath(self, fileName):
        import os
        PATH = os.path.split(os.path.dirname(__file__))[0]
        relativeCachePath = "cache/{}/{}.json".format(self.name(), fileName)
        return os.path.join(PATH, relativeCachePath)

    def _read(self, fileName):
        cachePath = self._cachePath(fileName)
        with open(cachePath, "r") as resultFile:
            res = resultFile.read()
            return res