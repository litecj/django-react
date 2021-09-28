// import logo from './logo.svg';
// import './App.css';
import React from "react"
import { Route, Switch, Redirect } from 'react-router-dom'
import { Navigation, Home, Counter, ToDo} from 'interview/common'
import {Algorithm, BruteForce, DivideConquer, Greedy, DynamicProgramming, BackTracking} from 'interview/algorithm'
import {DateStructure, Math, LinearData, Array, List, NonLinearData, Graph, Tree} from 'interview/datastructure'

const App = () => (<>
  <div>
    <header>
    <Navigation/>
    <Switch>
      <Route exact path='/' component={Home}/>
      <Redirect from = 'home' to={'/'}/>
      <Route exact path='/hook' component={Counter}/>
      <Route exact path='/todo' component={ToDo}/>

      <Route exact path ='/data-structure' component={DateStructure}/>
      <Route exact path ='/data-structure/math' component={Math}/>
      <Route exact path ='/data-structure/linear-data' component={LinearData}/>
      <Route exact path ='/data-structure/linear-data/array' component={Array}/>
      <Route exact path ='/data-structure/linear-data/list' component={List}/>
      <Route exact path ='/data-structure/non-linear-data' component={NonLinearData}/>
      <Route exact path ='/data-structure/non-linear-data/graph' component={Graph}/>
      <Route exact path ='/data-structure/non-linear-data/tree' component={Tree}/>

      <Route exact path ='/algorithom' component={Algorithm}/>
      <Route exact path ='/algorithom/brute-force' component={BruteForce}/>
      <Route exact path ='/algorithom/divide+conquer' component={DivideConquer}/>
      <Route exact path ='/algorithom/greedy' component={Greedy}/>
      <Route exact path ='/algorithom/dynamic-programming' component={DynamicProgramming}/>
      <Route exact path ='/algorithom/back-tracking' component={BackTracking}/>

    </Switch>
    </header>
  </div>

</>)
{/* function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
} */}

export default App;
