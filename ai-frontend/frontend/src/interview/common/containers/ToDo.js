import React, {useState} from 'react'
import styled from 'styled-components'

// import { Button, TextField} from '@mui/material'
// import Badge from '@mui/material/Badge'
// import MailIcon from '@mui/icons-material/Mail'
// import styled from 'styled-components'
// import Alert from '@mui/material/Alert';
// import AlertTitle from '@mui/material/AlertTitle';
// import Stack from '@mui/material/Stack';

export default function ToDo () {
    const [todo, setTodo] = useState('')

    let val =''

    const add = e => {
        e.preventDefault()
        val = e.target.value
        // alert(`입력한 갑 : ${val}`)
    }

    const del = e => {
        e.preventDefault()
        setTodo('')
    }

    const submitForm =e => {
        e.preventDefault()
        setTodo(val)
        document.getElementById('todo-input').value = ''

    }

    return (<>
    <div>
        <form onSubmit={submitForm} method='post'>
            <TodoDiv>
                <input type='text'  id='todo-input' onChange={add}/>
                <input type='submit' value='ADD'/> 
                {/* <TextField id="standard-basic" label="Standard" variant="standard" />
                <Button onChange={(handleChange)}>ADD</Button> */}
                <br/>
                <span>{todo}</span>
                <input type='submit'onClick={del} value='DEL'/>
                {/* <Button onClick={()=>setTodo(todo-1)}>DEl</Button> */}
            </TodoDiv>
        </form>

    </div>
    </>)
    }

const TodoDiv = styled.div`
    text-align: center;
    margin: 0 ;
`
