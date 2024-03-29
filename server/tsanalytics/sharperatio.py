from .lib import BaseAnalyticCalculator

class SharpeRatioCalculator(BaseAnalyticCalculator):
    def _getAnalyticName(self):
        return "Sharpe Ratio"
    
    def _riskFreeRate(self):
        # what is this
        return 0.08

    def _run(self, equityCurve):
        equitySeries = equityCurve['Equity']
        intialEquity = equitySeries.iat[0]
        finalEquity = equitySeries.iat[-1]
        returnRatio =  ((finalEquity - intialEquity)/intialEquity)

        dailyReturnSeries = equitySeries.pct_change()
        stdDailyReturn = dailyReturnSeries.std()
        if stdDailyReturn == 0: sharpeRatio = 0 
        else: sharpeRatio = (returnRatio - self._riskFreeRate())/stdDailyReturn
        return round(sharpeRatio, 2)
