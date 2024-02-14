
## Deontay

#### 🌎 What is Deontay?
Deontay is a mobile web application that provides insight on an assortment of cryptocurrency-based investment strategies. Users of the platform are able to gain insight on each strategy through a variety of timeseries analytics which can be viewed across multiple timeframes.
Furthermore, Deontay can serve as a lightweight method for quantitative traders to present their technical analysis based strategies to clients and other traders as the simple codebase provisions a low-code procedure to onboard and routinely backtest new strategies.

##### Deontay on iPhone X
<img src="https://github.com/DonCharlesLambert/Deontay/blob/main/misc/forreadme/compressed-phone.gif?raw=true"
style="margin:auto"
height="600px"
alt="Deontay used on iPhone X"
/>

##### Deontay?


#### 📈Deontay Strategies
The following are strategies native to Deontay. All trade Bitcoin but can be easily adjusted to trade other crypto-assets and even other asset classes.
##### Alpha Zero
Alpha Zero is a BUY and HOLD strategy for bitcoin. We regard the performance of bitcoin as the benchmark, thus the performance of this strategy with regard to Alpha is zero. Other strategies on Deontay can be viewed as methods to hedge against the volatility and market risk of bitcoin despite providing weaker returns.

Alpha Zero makes exactly one trade regardless of the time period, current price or current trend.

##### Early Bird
Early Bird uses technial analysis to anticipates trends and enter during trend reversals. The strategy is primarily reliant on the RSI, an indicator used to measure the magnitude of the assets recent price change.
If the asset is determined to be over sold, we enter a long position. We use assets with historically strong performance and have a long bias so open no short positions. We use overbought conditions to close our positions.
Through Deontay it can be observed that while this strategy has high returns, up to 145% over 5 years, benefitting from the strong performance of the underlying asset - it also features high drawdown.

##### Retrace Entry
Retrace Entry is an aggresive trend following strategy which aims to benefit from strength of established trends. The strategy uses the Average Directional Indicator (ADI), the Plus Directional Indicator (PDI) and the Minus Directional Indicator (MDI).
The ADI indicates the strength of the trend while the PDI and the MDI indicate the direction. Once the ADX has crossed the "mid level" the trend is strong and the strategy enters in the direction of the trend. After crossing the "scale level" we scale in on the position, increasing the size. Once the ADX indicates that the trend is slowing down or reversing we exit the trade.
This strategy has the advantage of low max drawdown, less than 10% over the early 2019-2024 period, despite the intense volatility of the underlying asset. This is in trade off 

#### 🏛️ Deontay Architecture
Deontay uses a client-server architecture. The server, which uses Python's tornado, provides strategy and crypto-asset data to the client which runs React.js.
The tornado service is designed to be run once a day. At launch the equity curve and timeseries analytics are calculated for each strategy and for each time period using T-1 data. These are cached providing quick response time for client queries throughout the day. This cache is then invalidated the next day when the service is torn down and restarted.

#### 🏃 Running Deontay
Deontay will be dockerized soon...
##### Requirements
|Client  |Server  |
|--|--|
|Node.js (14.x) | Python (3.x) |
|Node (6.x)  |  |

##### Download Requirements
```sh
deontay/client> npm install
deontay/server> python3 -m pip install -r requirements.txt
```
##### Run Deontay
The following commands must be run in two separate terminals
Make sure port 8888 is open and your firewall allows ingress traffic if you want to connect from other devices on your network
```sh
deontay/client> npm start
deontay/server> python3 -m base.server
```

##### Run Unit tests
```sh
deontay/server> python3 -m coverage run -m unittest
deontay/server> python3 -m coverage report
```


#### 🥊 Adding More Strategies & TS Analytics



 # Todo

- [ ] Dockerise
- [ ] Host on AWS




