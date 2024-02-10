from backtesting import Strategy
from .backtest import DeontayStrat, Deontay
from .const import Assets
from .logos import RETRACE_LOGO

class RetraceEntryStrat(DeontayStrat):
    """ 
    Retrace Entry detailed description...
    """
    ASSET = Assets.BITCOIN
    EXCLUSIVE_ORDERS = True


    def next(self):
        """
        If no position exists, open one.
        Do not close this position.
        -- WILL CHANGE
        """
        if not self.position:
            self.buy()

class RetraceEntry(Deontay):
    def name(self):
        return "Retrace Entry"

    def image(self):
        return RETRACE_LOGO
    
    def description(self):
        return "Trend-following strategy entering on retracement."
    
    def strategy(self):
        return RetraceEntryStrat