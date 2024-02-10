from .lib import BaseAnalyticCalculator

class PercentageReturnsCalculator(BaseAnalyticCalculator):
    def _getAnalyticName(self):
        return "Percentage Returns"
    
    def _run(self, equityCurve):
        equitySeries = equityCurve['Equity']
        intialEquity = equitySeries.iat[0]
        finalEquity = equitySeries.iat[-1]
        returns =  ((finalEquity - intialEquity)/intialEquity) * 100
        return round(returns, 2)
