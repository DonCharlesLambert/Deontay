import React, { useState } from 'react';
import Header from './header/header'
import StrategiesList from './strategies/list'
import StrategiesReview from './strategies/review'
import SlideIn from './lib/slide-in';
import './App.css';

function App() {
  const [strategy, selectStrategy] = useState({})
  const Menu = () => <SlideIn><StrategiesList selectStrategy={selectStrategy}/></SlideIn>
  const Review = () => <SlideIn><StrategiesReview strategy={strategy} goBack={selectStrategy}/></SlideIn>
  const Screen =  Object.keys(strategy).length === 0 ? Menu : Review
  return (
    <div className="App">
      <Header/>
      <Screen/>
    </div>
  );
}

export default App;
