import React, { useState } from 'react';
import Header from './header/header'
import StrategiesList from './strategies/list'
import StrategiesReview from './strategies/review'
import './App.css';

function App() {
  const [strategy, selectStrategy] = useState({})
  const Menu = () => <StrategiesList selectStrategy={selectStrategy}/>
  const Review = () => <StrategiesReview strategy={strategy} goBack={selectStrategy}/>
  const Screen =  Object.keys(strategy).length === 0 ? Menu : Review
  return (
    <div className="App">
      <Header/>
      <Screen/>
    </div>
  );
}

export default App;
