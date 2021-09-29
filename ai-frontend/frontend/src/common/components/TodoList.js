import React from 'react'
import styled from 'styled-components'
import {useDispatch, useSelector} from 'react-redux'

export default function TodoList() {

    const todos = useSelector(state => state.todos)
    const dispatch = useDispatch()

    return (<>
        
        <TodoDiv>
        {todos.lengh === 0 && (<h1>No List!</h1>)}
        {todos.lengh !== 0
            && (<h1>일찍 집에 가기 항목을 추가해 주세요.</h1>)}
        </TodoDiv>
    </>)
}

const TodoDiv = styled.div`
    text-align: center;
    margin: 0 ;
`