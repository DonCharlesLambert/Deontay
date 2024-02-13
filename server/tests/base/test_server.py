import unittest
import mock
from base.server import make_app, main
from tornado.testing import AsyncHTTPTestCase, gen_test

class TestServer(AsyncHTTPTestCase):

    def get_app(self):
        return make_app()

    @mock.patch("base.server.StrategiesBackend.getStrategies")
    def test_get_strategies(self, mockGetStrategies):
        mockGetStrategies.return_value = {}
        response = self.fetch('/get-strategies')
        self.assertEqual(response.code, 200)
        self.assertEqual(mockGetStrategies.call_count, 1)

    @mock.patch("base.server.AssetBackend.getAssets")
    def test_get_assets(self, mockGetAssets):
        mockGetAssets.return_value = {}
        response = self.fetch('/get-assets')
        self.assertEqual(response.code, 200)
        self.assertEqual(mockGetAssets.call_count, 1)

    @gen_test
    @mock.patch("base.server.BacktestBackend.dailyBacktest")
    @mock.patch("base.server.asyncio.Event.wait")
    async def test_main(self, mockWait, mockWarmup):
        await main()
        self.assertEqual(mockWarmup.call_count, 1)


if __name__ == '__main__':
    unittest.main()