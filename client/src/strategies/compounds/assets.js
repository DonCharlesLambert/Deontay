import AssetPanel from '../molecules/assetPanel'

function AssetsSection({assets, render}) {
  if (!render){return null}
  return (
    <div>
        <h2> Assets </h2>
        <div style={{display: 'flex', overflowX: 'scroll'}}>
          {assets.map((asset) => (
            <AssetPanel
              key={Math.random()}
              asset={asset}
            />
          ))}
        </div>
    </div>
  );
}

export default AssetsSection;
