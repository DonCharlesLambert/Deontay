import './styles/list.css'
import StrategyPanel from './panel'

// import will need to be removed -- find why to connect on the backend
import STRATEGIES from './strategies'

function StrategiesList({selectStrategy}) {
  return (
    <div className="strategiesList">
      <h1> Strategies </h1>
      {STRATEGIES.map((strategy) => (
        <StrategyPanel
          selectStrategy={selectStrategy}
          strategy={strategy}
        />
      ))}
    </div>
  );
}

export default StrategiesList;
