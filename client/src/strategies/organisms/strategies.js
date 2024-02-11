import StrategyPanel from '../molecules/staretgyPanel'

function StrategiesSection({strategies, selectStrategy}) {
  if (!strategies){return null}
  return (
    <div>
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

export default StrategiesSection;
