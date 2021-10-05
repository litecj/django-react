import React from "react";
import styled from 'styled-components'
import { useSelector, useDispatch } from 'react-redux'
import { deleteUserAction } from 'reducers/user.reducer'

export default function UserList() {
    const users = useSelector( state => state.userReducer.users)
    const dispatch = useDispatch()
    const deleteUser = id => dispatch(deleteUserAction(id))

    return ( 
        <UserListDiv>
            {users.length === 0 && (<h1>No user!</h1>)}
            {users.length !== 0 && (<h3>we have {users.length} users !</h3>)}
            {users.length !== 0 && users.map(
                user => (<div key={user.email}>
                    <span>user email : {user.email}</span> &nbsp;&nbsp;
                    <button onClick={deleteUser.bind(null, user.email)}>X</button>
                </div>)
            )}
        </UserListDiv>
    )
}
const UserListDiv = styled.div`text-align: center;`