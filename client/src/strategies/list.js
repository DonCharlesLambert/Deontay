import './styles/list.css'
import StrategyPanel from './panel'

// import will need to be removed -- find why to connect on the backend
import STRATEGIES from './strategies'

function StrategiesList({searchString, selectStrategy}) {
  const strategies = searchString === "" ? STRATEGIES : STRATEGIES.filter((strategy) => strategy.name.toLowerCase().includes(searchString.toLowerCase()))
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
