import './styles/panel.css'

function StrategyPanel({selectStrategy, strategy}) {
  const change = strategy.data.analytics.percentageReturns.All
  const changeClass = change < 0 ? "panelNegative" : "panelPositive"
  const changeArrow = change < 0 ? "▼" : "▲"
  const changeSign = change < 0 ? "" : "+"
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
                <p className={`panelReturnsChange ${changeClass}`}> {changeArrow} {changeSign}{change}% </p>
            </div>
        </div>
    </div>
  );
}

export default StrategyPanel;
