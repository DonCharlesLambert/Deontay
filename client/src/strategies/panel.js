import './styles/panel.css'
import ReturnArrow from './returnArrow'

function StrategyPanel({selectStrategy, strategy}) {
  return (
    <div className="strategiesPanel" onClick={() => selectStrategy(strategy)}>
        <div className="panelTitleDiv">
            <img src={strategy.imagesrc} className="panelLogo" alt={`logo for ${strategy.name} strategy`}/>
            <h3 className="panelTitle"> {strategy.name}</h3>
        </div>
        <p className="panelDescription"> {strategy.description} </p>
        <div className="panelReturnsDiv">
            <p className="panelReturnsText"> Returns </p>
            <div className="panelFiguresDiv">
                <p className="panelReturnsFigure"> {strategy.data.analytics.nominalReturns.All} </p>
                <ReturnArrow change={strategy.data.analytics.percentageReturns.All}/>
            </div>
        </div>
    </div>
  );
}

export default StrategyPanel;
