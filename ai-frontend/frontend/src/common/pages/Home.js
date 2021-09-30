import React from 'react'
// import { Switch, Route, Redirect } from 'react-router'
import { SignIn } from 'common'

// const Home = () => {
//     return (<><div>interview</div> </>)
// }
// export default Home

export default function Home () {
    return (<>
    <div style={{margin:'10px', textAlign: 'center'}}>interview</div>
    <br/>
    <SignIn/>
     </>)
}
