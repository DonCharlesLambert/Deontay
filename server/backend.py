from const import STRATEGIES, ANALYTICS, ASSET_IMAGE_MAP, ASSET_NAME_MAP, StrategyResponse
from dateutil.relativedelta import relativedelta
from datetime import datetime
import yfinance
from const import Assets
import os
import pandas as pd

class StrategiesBackend():
    def __init__(self):
        pass

    def getStrategies(self):
        res = {}
        for StrategyClass in STRATEGIES:
            strategy = StrategyClass()
            res[strategy.name()] = {
                StrategyResponse.IMAGE_SRC: strategy.image(),
                StrategyResponse.NAME: strategy.name(),
                StrategyResponse.DESCRIPTION: strategy.description(),
                StrategyResponse.DATA: strategy.data()
            }
        return res

class BacktestBackend():
    def dailyBacktest(self):
        for StrategyClass in STRATEGIES:
            strategy = StrategyClass()
            backtestResult = strategy.backtest()
            equityCurve = backtestResult._equity_curve
            for AnalyticClass in ANALYTICS:
                analytic = AnalyticClass(strategy.name(), equityCurve)
                analytic.run()

class AssetBackend():
    def getAssets(self):
        res = {}
        for asset in Assets:
            today = (datetime.now())
            yesterday = (datetime.now() - relativedelta(days=5))
            todayString = today.strftime("%Y-%m-%d")
            prices = self._getPrices(asset.value, yesterday, todayString)

            tPrice = prices["Close"].iat[-2]
            t1Price = prices["Close"].iat[-1]

            res[asset.value] = {
                "name": ASSET_NAME_MAP[asset],
                "imagesrc": ASSET_IMAGE_MAP[asset],
                "price": round(tPrice, 2),
                "change": round((t1Price/tPrice) - 1, 2)
            }
        return res
            
    # CACHE
    def _getPrices(self, asset, yesterday, todayString):
        cachedDf = self._getFromCache(asset, todayString)
        if cachedDf is not None:
            return cachedDf
        download = yfinance.download(asset, start=yesterday)
        self._storeInCache(asset, todayString, download)
        return download
        

    def _getFromCache(self, asset, todayString):
        try:
            relativeCachePath = "cache/{}/{}.csv".format(asset, todayString)
            return pd.read_csv(relativeCachePath)
        except:
            return None

    def _storeInCache(self, asset, todayString, df):
        cacheFolder = "cache/{}/{}.csv".format(asset, todayString)
        with open(cacheFolder, "a") as resultFile:
            resultFile.write(df.to_csv())
