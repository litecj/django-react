import React, {useState} from 'react'
import styled from 'styled-components'

export default function ToDo () {

    const [todo, setTodo] = useState('')

    let hello = ''

    const add = e => {
        e.preventDefault()
        // setTodo(e.target.value) : 실시간 반영
        hello = e.target.value
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