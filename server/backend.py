from const import STRATEGIES, ANALYTICS, StrategyResponse
import os
from datetime import datetime

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
            