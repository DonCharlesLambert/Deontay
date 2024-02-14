
 # Todo

- [x] Write dummy strategies for other strats, include meta data
- [x] Include meta data on base class too
- [x] Replace STRATEGIES dict with list of Strategies classes
- [x] Remove server.media.logos
- [x] Rename quant folder to strategies, make another folder called ts analytics
- [x] Create methods to calculate analytics
- [x] Write method to cache results and analytics
- [x] backtest will check if cache exists for the day and only backtest if it doesn't -- include param to invalidate cache
- [x] Call backtest on server start
- [ ] with timer
- [x] Write method to shape data in UI friendly format
- [x] Write strategies
- [x] improve graph
- [x] prevent zoom
- [x] Deep refactor the js
- [ ] Write unit tests
- [ ] Dockerise
- [ ] SEPARATE INTO MICROSERVICES ?? (base, strategies, tsanalytics)

Open port 8888 / turn off private firewall / make sure current connection is private for LAN

run
deontay/server> python3 -m base.server
deontay/client> npm start

test
deontay/server> python3 -m coverage run -m unittest
deontay/server> python3 -m coverage report

## Deontay

#### 🌎 What is Deontay?

#### 🏃 Running Deontay

#### 🥊 Adding More Strategies & TS Analytics

<img src="https://github.com/DonCharlesLambert/Deontay/blob/main/misc/forreadme/compressed-phone.gif?raw=true"
style="margin:auto"
height="600px"
alt="Deontay used on iPhone X"
/>
#### Dev Practices

Name                                    Stmts   Miss  Cover
-----------------------------------------------------------
base\__init__.py                            0      0   100%
base\backend.py                            53      2    96%
base\const.py                              39      0   100%
base\server.py                             35      3    91%
strategies\__init__.py                      0      0   100%
strategies\alphazero.py                    20      1    95%
strategies\backtest.py                     72      2    97%
strategies\const.py                        12      0   100%
strategies\earlybird.py                    34      3    91%
strategies\logos.py                         7      0   100%
strategies\retraceentry.py                 39      1    97%
tests\__init__.py                           0      0   100%
tests\base\__init__.py                      0      0   100%
tests\base\test_backend.py                 58      1    98%
tests\base\test_server.py                  27      1    96%
tests\strategies\__init__.py                0      0   100%
tests\strategies\test_backtest.py          75      1    99%
tests\strategies\test_strategies.py        71      0   100%
tests\tsanalytics\__init__.py               0      0   100%
tests\tsanalytics\test_tsanalytics.py      85      1    99%
tsanalytics\__init__.py                     0      0   100%
tsanalytics\const.py                        9      0   100%
tsanalytics\lib.py                         44      2    95%
tsanalytics\maxdrawdown.py                 11      0   100%
tsanalytics\nominalreturns.py               8      0   100%
tsanalytics\percentagereturns.py           10      0   100%
tsanalytics\sharperatio.py                 16      0   100%
-----------------------------------------------------------
TOTAL                                     725     18    98%
