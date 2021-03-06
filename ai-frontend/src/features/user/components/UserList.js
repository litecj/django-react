import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { UserListForm } from '..';

export default function UserList() {
  const [list, setList] = useState([])
  const SERVER = 'http://localhost:8000/api/users'


  const  fetchList = () => {
      axios.get(`${SERVER}/list`)
      .then(res => setList(res.data))
      .catch(err => console.log(err))
  }
  useEffect(() => {
    fetchList()
  }, [])

  
  return (
    <div>
        <h1>User List</h1>
        <UserListForm list={list}/>
    </div>
  );
}