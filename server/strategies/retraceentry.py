from backtesting.lib import crossover, cross
import pandas as pd
from .backtest import DeontayStrat, Deontay
from .const import Assets
from .logos import RETRACE_LOGO
from ta.trend import ADXIndicator

class RetraceEntryStrat(DeontayStrat):
    """ 
    Retrace Entry is an aggresive trend following strategy which aims to benefit from 
    strength of established trends. The strategy uses the Average Directional Indicator (ADI),
    the Plus Directional Indicator (PDI) and the Minus Directional Indicator (MDI).

    The ADI indicates the strength of the trend while the PDI and the MDI indicate the direction.
    Once the ADX has crossed the "mid level" the trend is strong and the strategy enters in the
    direction of the trend. After crossing the "scale level" we scale in on the position, increasing
    the size. Once the ADX indicates that the trend is slowing down or reversing we exit the trade.
    """
    ASSET = Assets.BITCOIN
    EXCLUSIVE_ORDERS = True
    ADX_WINDOW = 14

    ADX_LOW_LEVEL = 20
    ADX_MID_LEVEL = 50
    ADX_SCALE_LEVEL = 60

    def init(self):
        high = pd.Series(self.data.High)
        low = pd.Series(self.data.Low)
        close = pd.Series(self.data.Close)
        adx = ADXIndicator(high=high, low=low, close=close, window=self.ADX_WINDOW)
        self.adx = self.I(adx.adx)
        self.pdi = self.I(adx.adx_pos)
        self.mdi = self.I(adx.adx_neg)

    def next(self):
        # LONG POSITIONS
        if crossover(self.adx, self.ADX_MID_LEVEL) and self.pdi > self.mdi:
            self.buy(size=0.5)
        if crossover(self.adx, self.ADX_SCALE_LEVEL) and self.pdi > self.mdi:
            self.buy(size=1)
        if (cross(self.adx, self.ADX_LOW_LEVEL) and self.adx > self.ADX_LOW_LEVEL + 1) or self.mdi > self.pdi:
            self.position.close()

class RetraceEntry(Deontay):
    def name(self):
        return "Retrace Entry"

    def image(self):
        return RETRACE_LOGO
    
    def description(self):
        return "Trend-following strategy entering on retracement."
    
    def strategy(self):
        return RetraceEntryStrat