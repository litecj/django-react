import React from 'react'
import styled from 'styled-components'

// import { Button, TextField} from '@mui/material'
// import Badge from '@mui/material/Badge'
// import MailIcon from '@mui/icons-material/Mail'
// import styled from 'styled-components'
// import Alert from '@mui/material/Alert';
// import AlertTitle from '@mui/material/AlertTitle';
// import Stack from '@mui/material/Stack';

import { TodoList, TodoInput } from 'common'

export default function ToDo () {

    return (<>
    <div>
        <TodoDiv>
            <TodoInput/>
            <TodoList/>
        </TodoDiv>
    </div>



    {/* <div>
        <form onSubmit={} method='post'>
            <TodoDiv>
                <input type='text'  id='todo-input' onChange={}/>
                <input type='submit' value='ADD'/> 
                <br/>
                <span>{}</span>
                <input type='submit'onClick={} value='DEL'/>
            </TodoDiv>
        </form>
    </div> */}
    </>)
    }

const TodoDiv = styled.div`
    text-align: center;
    margin: 0 ;
`

// const [todo, setTodo] = useState('')
// let hi = ''

// const add = e => {
//     e.preventDefault()
//     // setTodo(e.target.value) : 실시간 반영
//     hi = e.target.value
// }

// const del = e => {
//     e.preventDefault()
//     setTodo('')
// }

// const submitForm = e => {
//     e.preventDefault()
//     setTodo(hi)
//     document.getElementById('todo-input').value ='' // 화면에 지워 주기
// }