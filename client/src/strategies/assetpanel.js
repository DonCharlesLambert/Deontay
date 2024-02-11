import './styles/panel.css'
import './styles/assetPanel.css'
import ReturnArrow from './returnArrow'

function AssetPanel({asset}) {
  return (
    <div className="assetPanel">
        <div className="assetTitleDiv">
            <img src={asset.imagesrc} className="assetPanelLogo" alt={`logo for ${asset.name} asset`}/>
            <h3 className="assetTitle"> {asset.name}</h3>
        </div>
        <p className="assetReturnsText"> {asset.price} </p>
        <ReturnArrow change={asset.change}/>
    </div>
  );
}

export default AssetPanel;