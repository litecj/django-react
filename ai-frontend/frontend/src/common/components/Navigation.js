import React from 'react'
import { Link } from 'react-router-dom'
import styled from 'styled-components'

const  Navigation = () => {
    return(
        <NaviDiv>
            <NaviList>
                    <ul><NaviItem><Link to= '/home'>INTERVIEW</Link></NaviItem></ul>
                    <ul><NaviItem><Link to= '/hook'>HOOK</Link></NaviItem></ul>
                    <ul><NaviItem><Link to= '/todo'>TODO</Link></NaviItem></ul>
                    <ul><NaviItem><Link to= '/sign-in'>Sign In</Link></NaviItem></ul>
                    <ul><NaviItem><Link to= '/sign-up'>Sign Up</Link></NaviItem></ul>
                    {/* <ul><NaviItem><Link to= '/sign-up'>Sign Up</Link></NaviItem></ul> */}
                    <ul>
                        <NaviItem><Link to= '/data-structure'>Date Structure</Link></NaviItem>
                        {/* <li><button><Link to= '/data-structure/math'>Math</Link></button></li>
                        <li><button><Link to= '/data-structure/linear-data'>Linear Data</Link></button></li>
                        <li><button><Link to= '/data-structure/non-linear-data'>Non Linear Data</Link></button></li> */}
                    </ul>
                    <ul>
                        <NaviItem><Link to= '/algorithom'>Algorithom</Link></NaviItem>
                        {/* <li><button><Link to= '/algorithom/brute-force'>Brute Force</Link></button></li>
                        <li><button><Link to= '/algorithom/divide+conquer'>Divide & Conquer</Link></button></li>
                        <li><button><Link to= '/algorithom/greedy'>Greedy</Link></button></li>
                        <li><button><Link to= '/algorithom/dynamic-programming'>Dynamic Programming</Link></button></li>
                        <li><button><Link to= '/algorithom/back-tracking'>Back Tracking</Link></button></li> */}
                    </ul>
            </NaviList>
                    {/* <ui><button><Link to= '/home'>Home</Link></button></ui>
                    <ui><button><Link to= '/hook'>HOOK</Link></button></ui>
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
                    </ui> */}

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
        </NaviDiv>
    )}

export default Navigation

const NaviList = styled.ul`
    display: flex;
    width: min-content;
    height:10px;
    margin: auto;
    
`

const NaviDiv = styled.div`
    padding-bottom: 30px;
    margin-bottom: auto;
    
`

const NaviItem = styled.li`
    width: 110px;
    color: none;
    font-family: "ls";
    font-size: 1em;
    list-style: none;
    textDecorationLine:'none'
    color:'black'
    `