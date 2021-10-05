
import { UserJoinUp, UserUpdate } from 'common'
import React from "react";
import styled from "styled-components"

export default function SignUp() {
    return(<>
    <Div>
        <h1>Sign Up</h1>
        <UserUpdate/>
        <UserJoinUp/>
    </Div>
    </>)
}
const Div = styled.div`
    text-align : center;
    padding : 100px;
`