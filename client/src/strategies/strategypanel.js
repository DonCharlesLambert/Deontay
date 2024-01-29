import './strategypanel.css'

function StrategyPanel({imagesrc, name, description, returns, change}) {
  const changeClass = change < 0 ? "panelNegative" : "panelPositive"
  const changeArrow = change < 0 ? "▼" : "▲"
  const changeSign = change < 0 ? "" : "+"
  return (
    <div className="strategiesPanel">
        <div className="panelTitleDiv">
            <img src={imagesrc} className="panelLogo" alt={`logo for ${name} strategy`}/>
            <h3 className="panelTitle"> {name}</h3>
        </div>
        <p className="panelDescription"> {description} </p>
        <div className="panelReturnsDiv">
            <p className="panelReturnsText"> Returns </p>
            <div className="panelFiguresDiv">
                <p className="panelReturnsFigure"> {returns} </p>
                <p className={`panelReturnsChange ${changeClass}`}> {changeArrow} {changeSign}{change}% </p>
            </div>
        </div>
    </div>
  );
}

export default StrategyPanel;
