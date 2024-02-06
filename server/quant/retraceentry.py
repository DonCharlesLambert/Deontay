from backtesting import Strategy
from .backtest import DeontayStrat
from .const import Assets
from .logos import RETRACE_LOGO

class RetraceEntry(DeontayStrat):
    """ 
    Retrace Entry detailed description...
    """
    ASSET = Assets.BITCOIN
    EXCLUSIVE_ORDERS = True

    @staticmethod
    def name():
        return "Retrace Entry"

    @staticmethod
    def image():
        return RETRACE_LOGO
    
    @staticmethod
    def description():
        return "Trend-following strategy entering on retracement."
    
    @staticmethod
    def data():
        return {
            "offsets": ["All", "1Y", "6M", "1M"],
            "analytics": {
                "nominalReturns": {"All": 17585.15, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "percentageReturns": {"All": -0.25, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "sharpeRatio": {"All": 3.7, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "maxDrawdown": {"All": 9.84, "1Y": 27.2, "6M": 2.0, "1M": 0}
            },
            "timeseries": { "All": [
                ["Day", "", "", "", ""],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
              ]
            },
            "trades": [] # use simple format
        }

    def next(self):
        """
        If no position exists, open one.
        Do not close this position.
        -- WILL CHANGE
        """
        if not self.position:
            self.buy()