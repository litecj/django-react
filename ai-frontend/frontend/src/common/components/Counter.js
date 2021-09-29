import React, {useState} from 'react'
import Button from '@mui/material/Button'
import Badge from '@mui/material/Badge'
import MailIcon from '@mui/icons-material/Mail'
import styled from 'styled-components'
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';


export default function Counter () {
    const [count, setCount] = useState(0)


    return (<>
        <div>
            <CounterDiv>
                {count === 0 &&
                    <Stack sx={{ width: '50%', margin: '0 auto' }} spacing={2}>
                    <Alert severity="error">
                        <AlertTitle>Error</AlertTitle>
                        No Mail
                        {/* This is an error alert — <strong>check it out!</strong> */}
                    </Alert>
                    </Stack>}
                <Badge badgeContent={count >=0 ? count : setCount(0)} color="secondary">
                    <MailIcon color="action"/>
                </Badge>
                <br/>
                <Button variant="outlined" onClick={()=> setCount(count + 1)}>
                    ADD
                </Button>
                <Button variant="outlined" onClick={()=> setCount(count - 1)}>
                    DEL
                </Button>
            </CounterDiv>
        </div>
    </>)
}

const CounterDiv = styled.div`
    text-align: center;
    margin: 10px;
`
