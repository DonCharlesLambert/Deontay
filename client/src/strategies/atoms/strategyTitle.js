function StrategyTitle({strategy, logoSize, fontSize}) {
  return (
        <div className="panelTitleDiv">
            <img src={strategy.imagesrc} style={{"height": logoSize}} className="panelLogo" alt={`logo for ${strategy.name} strategy`}/>
            <h3 className="panelTitle" style={{"font-size": fontSize, "margin": 0}}> {strategy.name}</h3>
        </div>
  );
}

export default StrategyTitle;
