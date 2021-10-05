import React from "react";
import styled from 'styled-components'
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';
import { useSelector, useDispatch } from "react-redux";
import { changePasswordAction } from 'reducers/userU.reducer'


export default function UserUpdate() {
    const userus = useSelector(state => state.userUpReducer.userus)
    const dispatch = useDispatch()
    let target = ''
    let edit_pw = ''
    const submitForm = e => {
        e.preventDefault()
        const editUseru = {
            email : target,
            password : edit_pw
        }
        dispatch(changePasswordAction(editUseru))
        alert("email : " + editUseru.email +" // pw : " + editUseru.password)

        target = ''
        edit_pw = ''
        
    }
    const changePassword = e => {
        e.preventDefault()
        target = e.target.id
        edit_pw = e.target.value
    }
    return(<><Div>
    {userus.length === 0 &&
        <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
        <Alert severity="warning">
        <AlertTitle>등록된 회원이 없습니다.</AlertTitle>
        </Alert>
        </Stack> }
    {userus.length !== 0 &&
        <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
        <Alert severity="warning">
        <AlertTitle>{userus.length}건의 회원 목록이 있습니다</AlertTitle>
        </Alert>
        </Stack>}
    {userus.length !== 0 && userus.map(useru => (
        <div key={useru.email}>
            {useru.email !== '' ?
            <span> email : {useru.email} , password : {useru.password}</span> :
            <span>이메일이 없는 회원
                </span>}
            <form onSubmit={submitForm}>
                <input type='text' id={useru.email} onChange={changePassword}/>
                <input type='submit' value='PW 수정'/>
            </form>
        </div>

    ))
    
    }
    </Div>
    </>)
}

const Div = styled.div`
    text-align : center;
    padding : 10px;
`