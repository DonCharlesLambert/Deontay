import React, { useState } from 'react';
import HeaderComponent from './header/header'
import StrategiesList from './strategies/organisms/list'
import StrategiesReview from './strategies/organisms/review'
import SlideIn from './lib/slide-in';
import './App.css';

function App() {
  const [strategy, selectStrategy] = useState({})
  const [searchString, setSearchString] = useState("")
  const Header = () => <HeaderComponent searchString={searchString} setSearchString={setSearchString}/>
  const Menu = () => <SlideIn><StrategiesList searchString={searchString} selectStrategy={selectStrategy}/></SlideIn>
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
