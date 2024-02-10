from .lib import BaseAnalyticCalculator

class MaxDrawdownCalculator(BaseAnalyticCalculator):
    def _getAnalyticName(self):
        return "Max Drawdown"
    
    def _run(self, equityCurve):
        equitySeries = equityCurve['Equity']
        maxEquitySeries = equitySeries.rolling(window=len(equitySeries), min_periods=1).max()
        drawdownSeries = (equitySeries/maxEquitySeries) - 1
        # min() value to get largest negative %
        maxDrawdownSeries = drawdownSeries.rolling(window=len(equitySeries), min_periods=1).min()
        maxDrawDown = maxDrawdownSeries.min() * 100
        return round(maxDrawDown, 2)
