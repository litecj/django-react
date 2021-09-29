// import logo from './logo.svg';
// import './App.css';
import React from "react"
import { Route, Switch, Redirect } from 'react-router-dom'
import { Navigation, Home, Counter, ToDo, SignIn} from 'common'
import {Algorithm, BruteForce, DivideConquer, Greedy, DynamicProgramming, BackTracking} from 'algorithm'
import {DateStructure, Math, LinearData, Array, List, NonLinearData, Graph, Tree} from 'datastructure'

import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux'
import { todoReducer, userReducer } from 'reducers'

const rootReducer = combineReducers({todoReducer, userReducer})
const store = createStore(rootReducer)

const App = () => (<>
  <div>
    <Provider store={store}>
      <Navigation/>
      <Switch>
        <Route exact path='/' component={Home}/>
        <Redirect from = 'home' to={'/'}/>
        <Route exact path='/hook' component={Counter}/>
        <Route exact path='/todo' component={ToDo}/>
        <Route exact path='/sign-in' component={SignIn}/>

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
    </Provider>
  </div>

</>)

export default App;
