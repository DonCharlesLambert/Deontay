from .lib import BaseAnalyticCalculator

class PercentageReturnsCalculator(BaseAnalyticCalculator):
    def _getAnalyticName(self):
        return "Percentage Returns"
    
    def _run(self, equityCurve):
        return -0.02
