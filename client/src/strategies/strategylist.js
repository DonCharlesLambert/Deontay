import './strategylist.css'
import StrategyPanel from './strategypanel'

// image imports will need to be removed -- find why to connect on the backend
import STRATEGIES from './strategies'

function StrategiesList() {
  return (
    <div className="strategiesList">
      <h1> Strategies </h1>
      {STRATEGIES.map((strategy) => (
        <StrategyPanel
          imagesrc={strategy.imagesrc}
          name={strategy.name}
          description={strategy.description}
          returns={strategy.returns}
          change={strategy.change}
        />
      ))}
    </div>
  );
}

export default StrategiesList;
