import React, {useState} from "react";
import { useDispatch } from "react-redux";
import { v4 as uuidv4} from 'uuid'
import styled from 'styled-components'
import { addTodoAction } from 'reducers'

export default function TodoInput () {

    const [todo, setTodo] = useState('')

    const dispatch = useDispatch

    const submitForm = e => {
        e.preventDefault()
        const newTodo = {
            id : uuidv4(),
            name : todo,
            complete:false
        }
        addTodo(newTodo)
        setTodo('')
    }

    const addTodo = todo => dispatch(addTodoAction(todo))

    const handleChange = e => {
        e.preventDefault()
        setTodo(e.target.value)
    }

    return (<>
    <div>
        <form onSubmit={submitForm} method='post'>
            <TodoDiv>
                <input type='text'
                        id='todo-input'
                        placeholder = "todo?"
                        value = {todo}
                        onChange={handleChange} />
                <input type='submit'
                        value='ADD'/> 
                <br/>
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