import React from "react";
import { Route,Switch, Redirect } from 'react-router-dom'
import { Provider } from 'react-redux'
import { Navi, Home } from "common";
import { BackTracking, BruteForce, DivideConquer, DP, Greedy } from "features/algorithms";
//import { Counter } from "features/counter";
import { CounterOld } from "features/counterOld";
import { Linear, NonLinear, Mathematics } from "features/datastructure";
import { TodoInput, TodoList, Todo } from "features/todos";
import { UserJoin, UserList, SignIn, SignUp } from "features/user";
import { store } from 'app/store';

const App = () => (
    <Provider store={store}>
      <Navi/>
        <Switch>
          <Route exact path = '/' component = {Home}/>
          <Redirect from='/home' to= { '/' }/>
          <Route exact path = '/counter-old' component = {CounterOld}/>
          <Route exact path = '/todo' component = {Todo}/>
          <Route exact path = '/sign-up' component = {SignUp}/>
          <Route exact path = '/mathematics' component = {Mathematics}/>
          <Route exact path = '/linear' component = {Linear}/>
          <Route exact path = '/nonLinear' component = {NonLinear}/>
          <Route exact path = '/back-tracking' component = {BackTracking}/>
          <Route exact path = '/brute-force' component = {BruteForce}/>
          <Route exact path = '/divide-conquer' component = {DivideConquer}/>
          <Route exact path = '/dp' component = {DP}/>
          <Route exact path = '/greedy' component = {Greedy}/>
        </Switch>
    </Provider>
)
export default App


// import React from 'react';
// import logo from './logo.svg';
// import { Counter } from './features/counter/Counter';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <Counter />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <span>
//           <span>Learn </span>
//           <a
//             className="App-link"
//             href="https://reactjs.org/"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             React
//           </a>
//           <span>, </span>
//           <a
//             className="App-link"
//             href="https://redux.js.org/"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             Redux
//           </a>
//           <span>, </span>
//           <a
//             className="App-link"
//             href="https://redux-toolkit.js.org/"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             Redux Toolkit
//           </a>
//           ,<span> and </span>
//           <a
//             className="App-link"
//             href="https://react-redux.js.org/"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             React Redux
//           </a>
//         </span>
//       </header>
//     </div>
//   );
// }

// export default App;
