import { useState, useEffect } from 'react'
import './styles/list.css'
import { ASSETS_ENDPOINT, STRATEGIES_ENDPOINT } from '../api/const'
import StrategyPanel from './panel'
import AssetPanel from './assetpanel'

function StrategiesList({searchString, selectStrategy}) {
  const [strategies, setStrategies] = useState([])
  const [assets, setAssets] = useState([])
  useEffect(() => {
    fetch(STRATEGIES_ENDPOINT, {
        mode: 'cors',
        method: 'GET',
        headers: {'Content-Type':'application/json'}
    }).then(
      (response) => response.json()
    ).then(
      (data) => {
        setStrategies(Object.values(data).filter((stratData) => {
          if(searchString === ""){return true}
          if(stratData.name.toLowerCase().includes(searchString.toLowerCase())){return true}
          return false
        }))
      }
    )
  }, [searchString])

  useEffect(() => {
    fetch(ASSETS_ENDPOINT, {
        mode: 'cors',
        method: 'GET',
        headers: {'Content-Type':'application/json'}
    }).then(
      (response) => response.json()
    ).then(
      (data) => {
        console.log(data)
        setAssets(Object.values(data))
      }
    )}
  )

  return (
    <div className="strategiesList">
      <h2> Assets </h2>
      <div style={{display: 'flex', overflowX: 'scroll'}}>
        {assets.map((asset) => (
          <AssetPanel
            key={Math.random()}
            asset={asset}
          />
        ))}
      </div>

      <h2> Strategies </h2>
      {strategies.map((strategy) => (
        <StrategyPanel
          key={Math.random()}
          selectStrategy={selectStrategy}
          strategy={strategy}
        />
      ))}
    </div>
  );
}

export default StrategiesList;
