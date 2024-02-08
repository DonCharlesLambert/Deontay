from .lib import BaseAnalyticCalculator

class NominalReturnsAnalyticCalculator(BaseAnalyticCalculator):
    def _getAnalyticName(self):
        return "Nominal Returns"
    
    def _run(self, equityCurve):
        # must ensure curve is in correct date order
        return equityCurve['Equity'].iat[-1] - equityCurve['Equity'].iat[0]
