import React from 'react'
import { Link } from 'react-router-dom'

const  NavigationA = () => {
    return(
        <>
            <div>
                <ul>
                    <button><Link to= '/algorithom/brute-force'>Brute Force</Link></button>
                    <button><Link to= '/algorithom/divide+conquer'>Divide & Conquer</Link></button>
                    <button><Link to= '/algorithom/greedy'>Greedy</Link></button>
                    <button><Link to= '/algorithom/dynamic-programming'>Dynamic Programming</Link></button>
                    <button><Link to= '/algorithom/back-tracking'>Back Tracking</Link></button>
                </ul>  
            </div>
        </>)}

export default NavigationA