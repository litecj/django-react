import React, {useState} from 'react'
import styled from 'styled-components'

// import { Button, TextField} from '@mui/material'
// import Badge from '@mui/material/Badge'
// import MailIcon from '@mui/icons-material/Mail'
// import styled from 'styled-components'
// import Alert from '@mui/material/Alert';
// import AlertTitle from '@mui/material/AlertTitle';
// import Stack from '@mui/material/Stack';

import { TodoList } from 'common'

export default function ToDo () {

    const [todo, setTodo] = useState('')

    let hello = ''

    const add = e => {
        e.preventDefault()
        // setTodo(e.target.value) : 실시간 반영
        hello = e.target.value
    }

    const del = e => {
        e.preventDefault()
        setTodo('')
    }

    const submitForm = e => {
        e.preventDefault()
        setTodo(hello)
        document.getElementById('todo-input').value =''
        
    }

    return (<>
    <div>
        <form onSubmit={submitForm} method='post'>
            <TodoDiv>
                <input type='text'  id='todo-input' onChange={add} />
                <input type='submit' value='ADD'/> 
                {/* <TextField id="standard-basic" label="Standard" variant="standard" />
                <Button onChange={(handleChange)}>ADD</Button> */}
                <br/><br/>
                <span>todo list : {todo}</span>
                <br/>
                <TodoList/>
                <input type='submit'onClick={del} value='DEL'/>
                {/* <Button onClick={()=>setTodo(todo-1)}>DEl</Button> */}
            </TodoDiv>
        </form>
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