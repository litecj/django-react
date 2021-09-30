import React from 'react'
// import { Switch, Route, Redirect } from 'react-router'
import { SignIn } from 'common'
import {connect} from 'api'

// const Home = () => {
//     return (<><div>interview</div> </>)
// }
// export default Home

export default function Home () {
    const handleClick = e => {
        e.preventDefault()
        alert("Home Click")
        connect()
        .then(res => {alert(`접속 성공 : ${res.data.connection}`)})
        .catch(err => {alert(`접속 실패 : ${err}`)})
    }
    return (<>
    <div style={{margin:'10px', textAlign: 'center'}}>interview</div>
    <br/>
    <button onClick={handleClick} >Connection</button>
    <SignIn/>
     </>)
}
