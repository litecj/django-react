import axios from 'axios';
import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

export default function UserRemove() {
  const [password, setPassword] = useState({})
  const sessionUser = JSON.parse(localStorage.getItem('sessionUser'));
  const history = useHistory()
  const SERVER = 'http://localhost:8000/api/users'
  const headers = {
    'Content-Type' : 'application/json',
    'Authorization': 'JWT fefege..'
  }

  const handleChange = e => {
    setPassword(e.target.value)
  }
  const handleClick = e => {
    e.preventDefault()
    const removeRequest = sessionUser
    if(sessionUser.password === password){
      axios.delete(`${SERVER}/check/${sessionUser.username}`, JSON.stringify(sessionUser.username), {headers})
      .then(res => {
        console.log(res.data)
        localStorage.setItem('sessionUser', '')
        history.push('/')
      })
      .catch(err => console.log(err))
    }else{
      alert('입력된 비밀번호가 틀립니다')
      document.getElementById('password').value = ''
    }

  }

  return (
      <div>
          <h1>User Remove</h1>
          <form method="DELETE">
            <ul>
              {/* <li>
                <label>
                    <span>회원번호 : {sessionUser.userId} </span>
                </label>
              </li> */}
              <li>    
                <label>
                    아이디: <span> {sessionUser.username} </span>
                </label>
              </li>

                <li><label for="pw">비밀번호</label>
                <input type="password" id="password" name="password" onChange={handleChange}/></li>
                <li><input type="submit" value="탈퇴 요청" onClick={handleClick}/></li>
                <li><input type="button" value="탈퇴 취소" onClick={e => history.push("/users/detail")}/></li>
            </ul>
          </form>
      </div>
  );
}