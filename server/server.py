import asyncio
import tornado
from backend import MarketDataBackend, StrategiesBackend
from const import Params

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PATCH, PUT')

    def options(self, *args):
        self.set_status(204)
        self.finish()


class MarketDataHandler(BaseHandler):
    def initialize(self):
        self.backend = MarketDataBackend()

    def get(self):
        # 'http://localhost:8888/get-market-data?symbol=BTC&startDate=2022-02-28&endDate=2022-03-01'
        symbol = self.get_argument(Params.SYMBOL, None, True)
        startDate = self.get_argument(Params.START_DATE, None, True)
        endDate = self.get_argument(Params.END_DATE, None, True)
        marketData = self.backend.getMarketData(symbol=symbol, startDate=startDate, endDate=endDate)
        self.write(marketData)

class StrategiesHandler(BaseHandler):
    def initialize(self):
        self.backend = StrategiesBackend()

    def get(self):
        # 'http://localhost:8888/get-strategies'
        strategies = self.backend.getStrategies()
        self.write(strategies)

    

def make_app():
    return tornado.web.Application([
        (r"/get-market-data", MarketDataHandler),
        (r"/get-strategies", StrategiesHandler),
    ])

async def main(port=8888):
    app = make_app()
    print("Service is running at http://localhost:8888/")
    app.listen(8888)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
    