import React from "react";
import { useHistory } from 'react-router-dom';

export default function Home() {
    const sessionUser = localStorage.getItem("sessionUser")
    const history = useHistory()
    const logout = e => {
        e.preventDefault()
        localStorage.setItem('sessionUser','')
        history.push('/')
    }
    

    return (<>
        {sessionUser !== '' && <input type="button" value="로그아웃" onClick={logout}/> }
        {sessionUser === '' && <input type="button" value="로그인" onClick={e => history.push('/users/login')}/> }
        <h1>Home</h1>
        {sessionUser === '' 
            ? <><button onClick = {e => history.push('/users/add')}>회원가입</button><button onClick = {e => history.push('/users/login')}>로그인</button></>
            : <h1>{sessionUser.username} 안녕 :) <br/> 로그인 중이네? ...</h1> }
    </>)
}