from backtesting.lib import crossover
import pandas as pd
from .backtest import DeontayStrat, Deontay
from .const import Assets
from .logos import BIRD_LOGO
from ta.momentum import RSIIndicator

class EarlyBirdStrat(DeontayStrat):
    """ 
    Early Bird uses technial analysis to anticipates trends and enter during trend
    reversals. The strategy is primarily reliant on the RSI, an indicator used to
    to measure the magnitude of the assets recent price change.

    If the asset is determined to be over sold, we enter a long position. We use
    assets with historically strong performance and have a long bias so open no
    short positions. We use overbought conditions to close our positions.
    """
    ASSET = Assets.BITCOIN
    EXCLUSIVE_ORDERS = False

    RSI_WINDOW = 14
    RSI_UPPER = 75
    RSI_LOWER = 50

    POSITION_SIZE = 0.1

    def init(self):
        close = pd.Series(self.data.Close)
        rsi = lambda : RSIIndicator(close=close, window=self.RSI_WINDOW).rsi()
        self.rsi = self.I(rsi)

    def next(self):
        currentPrice = self.data.Close[-1]
        if crossover(self.rsi, self.RSI_LOWER):
            self.buy(sl = currentPrice*0.95)
        
        if crossover(self.rsi, self.RSI_UPPER):
            self.position.close()

class EarlyBird(Deontay):
    def name(self):
        return "Early Bird"

    def image(self):
        return BIRD_LOGO
    
    def description(self):
        return "Anticipates trends through reversal patterns."
    
    def strategy(self):
        return EarlyBirdStrat