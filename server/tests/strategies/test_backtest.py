import unittest
import mock
from datetime import datetime
import pandas as pd
from strategies.backtest import Deontay

def mockPriceData():
    data = {'Date': ["2020-02-12", "2020-02-11", "2022-02-10", "2022-02-09"], 'Equity': [10, 20, 30, 40]}
    return pd.DataFrame.from_dict(data)

class TestDeontay(unittest.TestCase):
    def test_name(self):
        strat = Deontay()
        self.assertRaises(NotImplementedError, strat.name)

    def test_image(self):
        strat = Deontay()
        self.assertRaises(NotImplementedError, strat.image)

    def test_description(self):
        strat = Deontay()
        self.assertRaises(NotImplementedError, strat.description)

    def test_details(self):
        strat = Deontay()
        self.assertRaises(NotImplementedError, strat.details)
        
    def test_strategy(self):
        strat = Deontay()
        self.assertRaises(NotImplementedError, strat.strategy)

    def test_offsets(self):
        strat = Deontay()
        offsets = strat.offsets()
        self.assertEqual(offsets, ["All", "1Y", "6M", "1M"])

    @mock.patch("strategies.backtest.open")
    def test_nominalReturns(self, mockRead):
        """ also tests readData, other ts analytics don't """
        strat = Deontay()
        strat.name = mock.MagicMock()
        strat.name.return_value = "TestStrat"

        mockFile = mock.MagicMock()
        mockFile.read.return_value = '{"All": 1250552.42, "1Y": 748454.98, "6M": 554388.73, "1M": 219917.43}'
        mockRead.return_value.__enter__.return_value = mockFile

        nominalReturns = strat.nominalReturns()
        self.assertEqual(nominalReturns, {"All": 1250552.42, "1Y": 748454.98, "6M": 554388.73, "1M": 219917.43})

    def test_percentageReturns(self):
        strat = Deontay()
        strat._readData = mock.MagicMock()
        res = strat.percentageReturns()
        self.assertEqual(strat._readData.call_count, 1)

    def test_sharpeRatio(self):
        strat = Deontay()
        strat._readData = mock.MagicMock()
        res = strat.sharpeRatio()
        self.assertEqual(strat._readData.call_count, 1)

    def test_maxDrawdown(self):
        strat = Deontay()
        strat._readData = mock.MagicMock()
        res = strat.maxDrawdown()
        self.assertEqual(strat._readData.call_count, 1)


    def test_data(self):
        strat = Deontay()
        strat.offsets = mock.MagicMock()
        strat.analytics = mock.MagicMock()
        strat.timeseries = mock.MagicMock()
        strat.trades = mock.MagicMock()
        res = strat.data()
        self.assertEqual(type(res), dict)
        self.assertEqual(strat.offsets.call_count, 1)
        self.assertEqual(strat.analytics.call_count, 1)
        self.assertEqual(strat.timeseries.call_count, 1)
        self.assertEqual(strat.trades.call_count, 1)

    @mock.patch("strategies.backtest.pd.read_csv", return_value=mockPriceData())
    def test_timeseries(self, mockRead):
        strat = Deontay()
        strat.name = mock.MagicMock()
        strat.name.return_value = "TestStrat"
        res = strat.timeseries()
        self.assertEqual(type(res), dict)
        self.assertEqual(res['All'], [['Date', 'Equity'], ['Feb 2020', 10], ['Feb 2020', 20], ['Feb 2022', 30], ['Feb 2022', 40]])

if __name__ == '__main__':
    unittest.main()