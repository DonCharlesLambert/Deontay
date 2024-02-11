import '../styles/assetPanel.css'
import ReturnArrow from '../atoms/returnArrow'

function AssetPanel({asset}) {
  return (
    <div className="assetPanel">
        <div className="assetTitleDiv">
            <img src={asset.imagesrc} className="assetPanelLogo" alt={`logo for ${asset.name} asset`}/>
            <h3 className="assetTitle"> {asset.name}</h3>
        </div>
        <p className="assetReturnsText"> {(Math.round(asset.price * 100) / 100).toFixed(2)} </p>
        <ReturnArrow change={asset.change}/>
    </div>
  );
}

export default AssetPanel;