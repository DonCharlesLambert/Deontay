import './styles/review.css'
import React, { useState } from 'react';
import Chart from '../lib/charts'
import ReturnArrow from './returnArrow';

function StrategiesReview({strategy, goBack}) {
  const [offset, setOffset] = useState("All")
  return (
    <div className="review">
        <div className="backButton" onClick={() => goBack({})}>
            <p> {`← Return to Strategies`} </p>
        </div>
        <div className="headerDiv">
            <div>
                <div className="titleDiv">
                    <img className="logo" src={strategy.imagesrc} alt={`logo for ${strategy.name} strategy`}/>
                    <h3 className="title"> {strategy.name} </h3>
                </div>
                <p className="description"> {strategy.description} </p>
            </div>
            <div className="buttonDiv">
                {strategy.data.offsets.map((_offset) => (
                    <button
                        className={_offset === offset ? "currentOffsetButton" : "offsetButton"}
                        onClick={() => setOffset(_offset)}
                        key={Math.random()}
                    >
                        {_offset}
                    </button>
                ))}
            </div>
        </div>
        <div className="analyticsDiv">
            <p className="analyticName"> Returns </p>
            <p className="analyticValue"> {strategy.data.analytics.nominalReturns[offset]}</p>
            <ReturnArrow change={strategy.data.analytics.percentageReturns[offset]}/>
            <p className="analyticName"> Sharpe Ratio </p>
            <p className="analyticValue"> {strategy.data.analytics.sharpeRatio[offset]}</p>
            <div></div>
            <p className="analyticName"> Max Drawdown </p>
            <p className="analyticValue"> {strategy.data.analytics.maxDrawdown[offset] + "%"}</p>
            <div></div>
        </div>
        <div className="chartDiv">
            <Chart data={strategy.data.timeseries[offset]}/>
        </div>
    </div>
  );
}

export default StrategiesReview;
