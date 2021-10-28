import React, { useState, useEffect, useCallback } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

export default function UserDetail() {
    const SERVER = 'http://localhost:8000/api/users/'
    const history = useHistory()
    const [detail, setDetail] = useState({
        userId:'', username:'', password:'', email:'', name:'', regDate: new Date().toLocaleDateString()
    })
  
    const fetchOne = () => {
        const sessionUser = JSON.parse(localStorage.getItem('sessionUser'))
        console.log("디테일 들어왔어 " + JSON.stringify(sessionUser))
        alert('사용자 아이디 : '+ sessionUser.userId)
        axios.get(`${SERVER}/users/${sessionUser.userId}`)
        .then(res => {
            setDetail(res.data)
        })
        .catch(err => {
            alert(`${err}`)
        })
    }
    useEffect(()=> {
        fetchOne()}, 
        [])
    const logout = e => {
        e.preventDefault()
        localStorage.setItem('sessionUser','')
        history.push('/')
    }


  return (
    <div>
          <h1>회원 정보</h1>
          <ul>
              <li>
                  <label>
                      <span>회원번호 : {detail.userId} </span>
                  </label>
              </li>
              <li>    
                  <label>
                      아이디: <span> {detail.username} </span>
                  </label>
              </li>
              <li>
                  <label>
                      이메일: <span> {detail.email} </span>
                  </label>
              </li>
              <li>
                  <label>
                      비밀번호: <span>***안 알려 줄꺼지롱 ~****</span>
                  </label>
              </li>
              <li>
                  <label>
                      이름: <span> {detail.name} </span>
                  </label>
              </li>
              <li>
                  <input type="button" value="회원정보 수정" onClick={()=> history.push('/users/modify')}/>
                  <input type="button" value="로그아웃" onClick={logout}/>
              </li>
          </ul>

    </div>
  );
}