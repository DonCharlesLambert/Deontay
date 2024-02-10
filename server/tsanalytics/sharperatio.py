from .lib import BaseAnalyticCalculator

class SharpeRatioCalculator(BaseAnalyticCalculator):
    def _getAnalyticName(self):
        return "Sharpe Ratio"
    
    def _run(self, equityCurve):
        return -1
