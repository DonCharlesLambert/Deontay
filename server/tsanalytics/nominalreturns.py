from .lib import BaseAnalyticCalculator

class NominalReturnsCalculator(BaseAnalyticCalculator):
    def _getAnalyticName(self):
        return "Nominal Returns"
    
    def _run(self, equityCurve):
        # must ensure curve is in correct date order
        returns = equityCurve['Equity'].iat[-1] - equityCurve['Equity'].iat[0]
        formattedReturns = round(returns, 2)
        return formattedReturns