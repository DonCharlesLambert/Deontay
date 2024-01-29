
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
        returns: 17585.15,
        change: -0.25
    },
    {
        imagesrc: retracelogo,
        name: "Retrace Enry",
        description: "Trend-following strategy entering on retracement.",
        returns: 22493.48,
        change: +0.25
    },
    {
        imagesrc: birdlogo,
        name: "Early Bird",
        description: "Anticipates trends through reversal patterns.",
        returns: 19577.01,
        change: -0.14
    }
]

export default STRATEGIES;
