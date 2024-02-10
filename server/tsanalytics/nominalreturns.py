from .lib import BaseAnalyticCalculator

class NominalReturnsCalculator(BaseAnalyticCalculator):
    def _getAnalyticName(self):
        return "Nominal Returns"
    
    def _run(self, equityCurve):
        equitySeries = equityCurve['Equity']
        returns = equitySeries.iat[-1] - equitySeries.iat[0]
        return round(returns, 2)