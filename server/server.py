import asyncio
import tornado
from backend import StrategiesBackend, BacktestBackend, AssetBackend

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PATCH, PUT')

    def options(self, *args):
        self.set_status(204)
        self.finish()

class StrategiesHandler(BaseHandler):
    def initialize(self):
        self.backend = StrategiesBackend()

    def get(self):
        # 'http://localhost:8888/get-strategies'
        strategies = self.backend.getStrategies()
        self.write(strategies)

class AssetsHandler(BaseHandler):
    def initialize(self):
        self.backend = AssetBackend()

    def get(self):
        # 'http://localhost:8888/get-assets'
        assets = self.backend.getAssets()
        self.write(assets)

def make_app():
    return tornado.web.Application([
        (r"/get-strategies", StrategiesHandler),
        (r"/get-assets", AssetsHandler),
    ])

async def main(port=8888):
    BacktestBackend().dailyBacktest()
    app = make_app()
    print("Service is running at http://localhost:8888/")
    app.listen(8888)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
    