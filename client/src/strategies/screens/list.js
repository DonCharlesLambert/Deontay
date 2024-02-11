import { useState, useEffect } from 'react'
import '../styles/list.css'
import { ASSETS_ENDPOINT, STRATEGIES_ENDPOINT } from '../../api/const.js'

import FeauredSection from '../organisms/featured.js'
import AssetsSection from '../organisms/assets.js'
import StrategiesSection from '../organisms/strategies.js'

function StrategiesList({searchString, selectStrategy}) {
  const [strategies, setStrategies] = useState([])
  const [assets, setAssets] = useState([])
  const [featured, setFeatured] = useState([])

  useEffect(() => {
    fetch(STRATEGIES_ENDPOINT, {
        mode: 'cors',
        method: 'GET',
        headers: {'Content-Type':'application/json'}
    }).then(
      (response) => response.json()
    ).then(
      (data) => {
        data = Object.values(data)
        setFeatured(data.find(e => !!e))
        setStrategies(data.filter((stratData) => {
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
        setAssets(Object.values(data))
      }
    )}, []
  )
  const renderAssets = searchString === "" && assets
  const renderFeatured = searchString === "" && featured.data
  return (
    <div className="strategiesList">
      <AssetsSection assets={assets} render={renderAssets}/>
      <FeauredSection featured={featured} render={renderFeatured}/>
      <StrategiesSection strategies={strategies} selectStrategy={selectStrategy}/>
    </div>
  );
}

export default StrategiesList;
