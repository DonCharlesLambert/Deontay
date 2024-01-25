import asyncio
import tornado
from backend import MarketDataBackend
from const import Params

class MarketDataHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.backend = MarketDataBackend()

    def get(self):
        # 'http://localhost:8888/get-market-data?symbol=BTC&startDate=2022-02-28&endDate=2022-03-01'
        symbol = self.get_argument(Params.SYMBOL, None, True)
        startDate = self.get_argument(Params.START_DATE, None, True)
        endDate = self.get_argument(Params.END_DATE, None, True)
        marketData = self.backend.getMarketData(symbol=symbol, startDate=startDate, endDate=endDate)
        self.write(marketData)

def make_app():
    return tornado.web.Application([
        (r"/get-market-data", MarketDataHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
    