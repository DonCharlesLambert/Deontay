from const import STRATEGIES, StrategyResponse
import os
from datetime import datetime

class StrategiesBackend():
    def __init__(self):
        pass

    def getStrategies(self):
        res = {}
        for strategy in STRATEGIES:
            res[strategy.name()] = {
                StrategyResponse.IMAGE_SRC: strategy.image(),
                StrategyResponse.NAME: strategy.name(),
                StrategyResponse.DESCRIPTION: strategy.description(),
                StrategyResponse.DATA: strategy.data()
            }
        return res

class BacktestBackend():
    def dailyBacktest(self):
        for strategy in STRATEGIES:
            backtestResult = strategy.backtest(strategy)
            equityCurve = backtestResult._equity_curve
            folderPath = "cache/{}/".format(strategy.name())
            fileName = datetime.today().strftime("%Y_%m_%d") + ".csv"
            if not os.path.exists(folderPath):
                os.mkdir(folderPath)
            equityCurve.to_csv(folderPath + fileName)
            # run analytics on bt
            # store in same folder
            