import React from 'react'
import styled from 'styled-components'

// import { Button, TextField} from '@mui/material'
// import Badge from '@mui/material/Badge'
// import MailIcon from '@mui/icons-material/Mail'
// import styled from 'styled-components'
// import Alert from '@mui/material/Alert';
// import AlertTitle from '@mui/material/AlertTitle';
// import Stack from '@mui/material/Stack';

import { UserJoin, UserList } from 'common'

export default function SignIn () {

    return (<>
    <div>
        <SignInDiv>
            <UserJoin/>
            <UserList/>
        </SignInDiv>
    </div>
    </>)
    }

const SignInDiv = styled.div`
    text-align: center;
    margin: 0 ;
`