from backtesting import Strategy
from .backtest import DeontayStrat, Deontay
from .const import Assets
from .logos import BIRD_LOGO

class EarlyBirdStrat(DeontayStrat):
    """ 
    Early Bird detailed description...
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

class EarlyBird(Deontay):
    def name(self):
        return "Early Bird"

    def image(self):
        return BIRD_LOGO
    
    def description(self):
        return "Anticipates trends through reversal patterns."
    
    def strategy(self):
        return EarlyBirdStrat