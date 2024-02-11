import './styles/panel.css'
import './styles/assetPanel.css'

function AssetPanel({asset}) {
  const change = asset.change
  const changeClass = change < 0 ? "panelNegative" : "panelPositive"
  const changeArrow = change < 0 ? "▼" : "▲"
  const changeSign = change < 0 ? "" : "+"
  return (
    <div className="assetPanel">
        <div className="assetTitleDiv">
            <img src={asset.imagesrc} className="assetPanelLogo" alt={`logo for ${asset.name} asset`}/>
            <h3 className="assetTitle"> {asset.name}</h3>
        </div>
        <p className="assetReturnsText"> {asset.price} </p>
        <p className={`assertReturnsChange ${changeClass}`}> {changeArrow} {changeSign}{change}% </p>
    </div>
  );
}

export default AssetPanel;