import unittest
import mock
import datetime
from datetime import datetime as dt
import pandas as pd
from strategies.alphazero import AlphaZero
from strategies.earlybird import EarlyBird
from strategies.retraceentry import RetraceEntry

def mockPriceData():
    data = {
        'Date': [dt.strptime("2020-02-12", "%Y-%m-%d") - datetime.timedelta(days=x) for x in range(0, 30)],
        'Open': [5*x for x in range(0,30)],
        'High': [15*x for x in range(0,30)],
        'Low': [1*x for x in range(0,30)],
        'Close': [10*x for x in range(0,30)],
    }
    return pd.DataFrame.from_dict(data)

class TestAlphaZero(unittest.TestCase):
    def test_name(self):
        strat = AlphaZero()
        self.assertEqual(strat.name(), "Alpha Zero")

    def test_image(self):
        strat = AlphaZero()
        image = strat.image()
        self.assertEqual(type(image), str)
        self.assertTrue(image.startswith("data:image/png;base64"))

    def test_descrption(self):
        strat = AlphaZero()
        self.assertEqual(strat.description(), "Dollar-cost average strategy for a bitcoin believer.")

    def test_description(self):
        strat = AlphaZero()
        self.assertEqual(type(strat.description()), str)

    @mock.patch("strategies.backtest.yfinance.download", return_value=mockPriceData())
    def test_backtest(self, mockYfinance):
        strat = AlphaZero()
        res = strat.backtest()
        self.assertEqual(len(res._trades), 1)

class TestRetraceEntry(unittest.TestCase):
    def test_name(self):
        strat = RetraceEntry()
        self.assertEqual(strat.name(), "Retrace Entry")

    def test_image(self):
        strat = RetraceEntry()
        image = strat.image()
        self.assertEqual(type(image), str)
        self.assertTrue(image.startswith("data:image/png;base64"))

    def test_descrption(self):
        strat = RetraceEntry()
        self.assertEqual(strat.description(), "Trend-following strategy entering on retracement.")

    def test_description(self):
        strat = RetraceEntry()
        self.assertEqual(type(strat.description()), str)

    @mock.patch("strategies.backtest.yfinance.download", return_value=mockPriceData())
    def test_backtest(self, mockYfinance):
        strat = RetraceEntry()
        res = strat.backtest()
        self.assertEqual(len(res._trades), 1)
        
class TestEarlyBird(unittest.TestCase):
    def test_name(self):
        strat = EarlyBird()
        self.assertEqual(strat.name(), "Early Bird")

    def test_image(self):
        strat = EarlyBird()
        image = strat.image()
        self.assertEqual(type(image), str)
        self.assertTrue(image.startswith("data:image/png;base64"))

    def test_descrption(self):
        strat = EarlyBird()
        self.assertEqual(strat.description(), "Anticipates trends through reversal patterns.")

    def test_description(self):
        strat = EarlyBird()
        self.assertEqual(type(strat.description()), str)

    @mock.patch("strategies.backtest.yfinance.download", return_value=mockPriceData())
    def test_backtest(self, mockYfinance):
        strat = EarlyBird()
        res = strat.backtest()
        self.assertEqual(len(res._trades), 0) # no reversals, no entry which is cool
