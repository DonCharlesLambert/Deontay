from backtesting import Strategy
from .backtest import DeontayStrat
from .const import Assets
from .logos import BIRD_LOGO

class EarlyBird(DeontayStrat):
    """ 
    Early Bird detailed description...
    """
    ASSET = Assets.BITCOIN
    EXCLUSIVE_ORDERS = True

    @staticmethod
    def name():
        return "Early Bird"

    @staticmethod
    def image():
        return BIRD_LOGO
    
    @staticmethod
    def description():
        return "Anticipates trends through reversal patterns."

    def next(self):
        """
        If no position exists, open one.
        Do not close this position.
        -- WILL CHANGE
        """
        if not self.position:
            self.buy()