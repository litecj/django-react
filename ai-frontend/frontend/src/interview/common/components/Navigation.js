import React from 'react'
import { Link } from 'react-router-dom'

const  Navigation = () => {
    return(
        <div>
            <ui><button><Link to= '/home'>Home</Link></button></ui>
            <ui>
                <button><Link to= '/data-structure'>Date Structure</Link></button>
                <li><button><Link to= '/data-structure/math'>Math</Link></button></li>
                <li><button><Link to= '/data-structure/linear-data'>Linear Data</Link></button></li>
                <li><button><Link to= '/data-structure/non-linear-data'>Non Linear Data</Link></button></li>
            </ui>
            <ui>
                <button><Link to= '/algorithom'>Algorithom</Link></button>
                <li><button><Link to= '/algorithom/brute-force'>Brute Force</Link></button></li>
                <li><button><Link to= '/algorithom/divide+conquer'>Divide & Conquer</Link></button></li>
                <li><button><Link to= '/algorithom/greedy'>Greedy</Link></button></li>
                <li><button><Link to= '/algorithom/dynamic-programming'>Dynamic Programming</Link></button></li>
                <li><button><Link to= '/algorithom/back-tracking'>Back Tracking</Link></button></li>
            </ui>

            {/* <button><Link to= '/home'>Home</Link></button>
            <button><Link to= '/data-structure'>Date Structure</Link></button>
            <ui>
                <button><Link to= '/data-structure/math'>Math</Link></button>
                <button><Link to= '/data-structure/linear-data'>Linear Data</Link></button>
                    <li><button><Link to= '/data-structure/linear-data/array'>Array</Link></button></li>
                    <li><button><Link to= '/data-structure/linear-data/list'>List</Link></button></li>
                <button><Link to= '/data-structure/non-linear-data'>Non Linear Data</Link></button>
                    <li><button><Link to= '/data-structure/non-linear-data/graph'>Graph</Link></button></li>
                    <li><button><Link to= '/data-structure/non-linear-data/tree'>Tree</Link></button></li>
            </ui>
            <button><Link to= '/algorithom'>Algorithom</Link></button>
            <ui>
                <button><Link to= '/algorithom/brute-force'>Brute Force</Link></button>
                <button><Link to= '/algorithom/divide+conquer'>Divide & Conquer</Link></button>
                <button><Link to= '/algorithom/greedy'>Greedy</Link></button>
                <button><Link to= '/algorithom/dynamic-programming'>Dynamic Programming</Link></button>
                <button><Link to= '/algorithom/back-tracking'>Back Tracking</Link></button>
            </ui> */}
        </div>
    )}

export default Navigation