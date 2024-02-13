import '../styles/panel.css'
import ReturnArrow from '../atoms/returnArrow'
import StrategyTitle from '../atoms/strategyTitle';

function StrategyPanel({selectStrategy, strategy}) {
  return (
    <div className="strategiesPanel" onClick={() => selectStrategy(strategy)}>
        <StrategyTitle strategy={strategy}/>
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
