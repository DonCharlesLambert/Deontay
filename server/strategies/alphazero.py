from .backtest import DeontayStrat, Deontay
from .const import Assets
from .logos import ALPHA_LOGO

class AlphaZeroStrat(DeontayStrat):
    """ 
    Alpha Zero is a BUY and HOLD strategy for bitcoin 
    We regard the performance of bitcoin as the benchmark,
    thus the performance of this strategy with regard to Alpha is zero

    Other strategies can be viewed as methods to hedge against the
    volatility and market risk of bitcoin despite providing
    weaker returns.
    """
    ASSET = Assets.BITCOIN
    EXCLUSIVE_ORDERS = True

    def next(self):
        """
        If no position exists, open one.
        Do not close this position.
        """
        if not self.position:
            self.buy()

class AlphaZero(Deontay):
    def name(self):
        return "Alpha Zero"

    def image(self):
        return ALPHA_LOGO
    
    def description(self):
        return "Dollar-cost average strategy for a bitcoin believer."
    
    def strategy(self):
        return AlphaZeroStrat
