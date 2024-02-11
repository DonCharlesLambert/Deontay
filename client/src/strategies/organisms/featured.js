import ReturnArrow from '../atoms/returnArrow'
import StrategyTitle from '../atoms/strategyTitle';
import Chart from '../../lib/charts'

function FeauredSection({featured, render}) {
  if (!render){return null}
  return (
    <div>
        <h2> Featured </h2>
        <div style={{"display": "flex", "align-items": "center"}}>
            <StrategyTitle strategy={featured} logoSize={"5vh"} fontSize={32}/>
            <div style={{"margin": "10px"}}>
            <ReturnArrow change={featured.data.analytics.percentageReturns.All}/>
            </div>
        </div>
        {
          featured.details.map((paragraph) => (
            <p style={{"marginTop": "0px", "marginBottom": "5px" , "fontWeight": 100, "fontSize": 14}}>{paragraph}</p>
          ))
        }
        <div className="chartDiv">
            <Chart data={featured.data.timeseries["All"]}/>
        </div>
        
    </div>
  );
}

export default FeauredSection;
