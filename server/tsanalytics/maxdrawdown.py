from .lib import BaseAnalyticCalculator

class MaxDrawdownCalculator(BaseAnalyticCalculator):
    def _getAnalyticName(self):
        return "Max Drawdown"
    
    def _run(self, equityCurve):
        return 1000
