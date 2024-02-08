from .backtest import DeontayStrat
from .const import Assets
from .logos import ALPHA_LOGO

class AlphaZero(DeontayStrat):
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

    @staticmethod
    def name():
        return "Alpha Zero"

    @staticmethod
    def image():
        return ALPHA_LOGO
    
    @staticmethod
    def description():
        return "Dollar-cost average strategy for a bitcoin believer."

    def next(self):
        """
        If no position exists, open one.
        Do not close this position.
        """
        if not self.position:
            self.buy()