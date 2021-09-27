import React from 'react'
import { Link } from 'react-router-dom'

const NavigationD = () => {
    return(
        <>
        <div>
            <ul>
                <button><Link to='/data-structure/math'>Math</Link></button>
                <button><Link to='/data-structure/linear-data'>Linear Data</Link></button>
                    <li><button><Link to='/data-structure/linear-data/array'>Array</Link></button></li>
                    <li><button><Link to='/data-structure/linear-data/list'>List</Link></button></li>
            </ul>
            <ul>
                <button><Link to='/data-structure/non-linear-data'>Non Linear Data</Link></button>
                    <li><button><Link to='/data-structure/non-linear-data/graph'>Graph</Link></button></li>
                 <li><button><Link to='/data-structure/non-linear-data/tree'>Tree</Link></button></li>
            </ul>
        </div>
        </>)}


export default NavigationD;