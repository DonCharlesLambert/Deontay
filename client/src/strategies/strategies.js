
import alphalogo from "../images/logonn-transparent.png"
import retracelogo from "../images/retracelogonn-transparent.png"
import birdlogo from "../images/entrylogonn-transparent.png"
// image imports will need to be removed -- find why to connect on the backend
// where we will get data from the api
const STRATEGIES = [
    {
        imagesrc: alphalogo,
        name: "Alpha Zero",
        description: "Dollar-cost average strategy for a bitcoin believer.",
        data: {
            offsets: ["All", "1Y", "6M", "1M"],
            analytics: {
                nominalReturns: {"All": 17585.15, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                percentageReturns: {"All": -0.25, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                sharpeRatio: {"All": 3.7, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                maxDrawdown: {"All": 9.84, "1Y": 27.2, "6M": 2.0, "1M": 0}
            },
        }
        //need another key "data" which is a dict with keys
            // offsets: [All, 1Y, 6M, 1M]
            // analytics: {sharpeRatio: {All: a, 1Y: x, 6M: y, 1M: z}, maxDrawdown: {All: a, 1Y: x, 6M: y, 1M: z}}
            // trades: [{direction: BUY, entryTime: today, exitTime: yesterday, size: 1.0, returns: 0.2},...]
            // timeseries: timeseries of price changes with high, low, open and close
    },
    {
        imagesrc: retracelogo,
        name: "Retrace Enry",
        description: "Trend-following strategy entering on retracement.",
        data: {
            offsets: ["All", "1Y", "6M", "1M"],
            analytics: {
                nominalReturns: {"All": 22493.48, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                percentageReturns: {"All": 0.25, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                sharpeRatio: {"All": 3.7, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                maxDrawdown: {"All": 9.1, "1Y": 27.2, "6M": 2.0, "1M": 0}
            },
        }
    },
    {
        imagesrc: birdlogo,
        name: "Early Bird",
        description: "Anticipates trends through reversal patterns.",
        data: {
            offsets: ["All", "1Y", "6M", "1M"],
            analytics: {
                nominalReturns: {"All": 19577.01, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                percentageReturns: {"All": -0.14, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                sharpeRatio: {"All": 3.7, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                maxDrawdown: {"All": 9.1, "1Y": 27.2, "6M": 2.0, "1M": 0}
            },
        }
    }
]

export default STRATEGIES;
