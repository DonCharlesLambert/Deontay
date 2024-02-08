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

    def next(self):
        """
        If no position exists, open one.
        Do not close this position.
        -- WILL CHANGE
        """
        if not self.position:
            self.buy()