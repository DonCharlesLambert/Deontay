import { useState, useEffect } from 'react'
import './styles/list.css'
import { ASSETS_ENDPOINT, STRATEGIES_ENDPOINT } from '../api/const'
import { SOL_IMAGE, BITCOIN_IMAGE, ETH_IMAGE, USDT_IMAGE } from './img'
import StrategyPanel from './panel'
import AssetPanel from './assetpanel'

function StrategiesList({searchString, selectStrategy}) {
  const [strategies, setStrategies] = useState([])
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

  const assets = [
    {
      imagesrc: BITCOIN_IMAGE,
      name: "BTC",
      price: 47585.15,
      change: -6.93
    },
    {
      imagesrc: ETH_IMAGE,
      name: "ETH",
      price: 17585,
      change: 2.27
    },
    {
      imagesrc: SOL_IMAGE,
      name: "SOL",
      price: 90.15,
      change: -0.23
    },
    {
      imagesrc: USDT_IMAGE,
      name: "UST",
      price: 0.98,
      change: 0.23
    }
  ]

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
