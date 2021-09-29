import React from "react";
import styled from 'styled-components'
import { useSelector } from 'react-redux'

export default function UserList() {
    const users = useSelector( state => state.userReducer.users)
    return ( 
        <UserListDiv>
            {users.length === 0 && (<h1>No user!</h1>)}
            {users.length !== 0 && (<h3>we have {users.length} users !</h3>)}
        </UserListDiv>
    )
    
}
const UserListDiv = styled.div`text-align: center;`