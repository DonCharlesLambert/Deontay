import { useState, useEffect } from 'react'
import './styles/list.css'
import { STRATEGIES_ENDPOINT } from '../api/const'
import StrategyPanel from './panel'

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

  return (
    <div className="strategiesList">
      <h1> Strategies </h1>
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
