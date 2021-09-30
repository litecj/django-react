import * as React from 'react';
import {useState} from "react";
// import { useDispatch } from "react-redux";
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
// import Link from '@mui/material/Link';
// import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
// import { addUserAction } from 'reducers/user.reducer';
import { userRetriever } from 'api';


const theme = createTheme();

export default function UserJoin() {
    const [user, setUser] = useState({
      username: '',
      name: '',
      birth: '',
      address: '',
      email: '',
      password: ''
    })
    const {username, name, birth, address, email, password} = `user`
    //user이라는 주소값을 불러야 하기에 백포인트

    // 위의 줄과 동일한 내용 : java style
    // const [username, setUsername] = useState('')
    // const [birth, setBirth] = useState('')
    // const [address, setAdress] = useState('')
    // const [email, setEmail] = useState('')
    // const [password, setPassword] = useState('')
    // const dispatch = useDispatch()
    
    const handleSubmit = e => {
        e.preventDefault();
    // const data = new FormData(e.currentTarget);
    // // eslint-disable-next-line no-console
    // console.log({
    //   email: data.get('email'),
    //   password: data.get('password'),
    // });
        // const payload = {email, password, username, birth, address}
            // = email: email, password:password = 동일 명칭이라 생략함
        alert(`가입회원 정보: ${JSON.stringify(user)}`)
        userRetriever({...user})
        .then(res => {alert(`회원 가입 완료: ${res.data.result}`)})
        .catch(err => {alert(`회원가입 실패: ${err}`)})
        //...user vs user : 전부 입력 시 상관 無 BUT 비필수 항목 하나라도 있으면 must ...user
        // addUser(user)    : userRetriever({...user})로 함으로써 DB와 연결
        // setEmail('')
        // setPassword('')
        // setUsername('')
        // setBirth('')
        // setAdress('')
    }
    // const addUser = user => dispatch(addUserAction(user))  
    // dispatch 함수 中 액션 생성 합수 : addUserAction(--)
    // const addUser = user => / {return}  = () / /dispatch 사용 이유 : 리액트에서 리덕스 공간으로 이동 시키기 위해
    const handleChange = e => {
          e.preventDefault()
          const {name, value} = e.target
          setUser({
            ...user,
            [name]:value
          })
      }
      // 이때의 name은 속성의 name, 그래서 백개도 가능
   
    // 위의 스타일로 할 경우 여러개의 target.value 만들 필요 없음. 但 java의 경우 target.value를 set 갯수 만큼 필요
    // 다른 칸에 입력이 불가한 모습 보임
    // const handleChange1 = e =>{
    //     e.preventDefault()
    //     setEmail(e.target.value)
    // }
    // const handleChange2 = e =>{
    //   e.preventDefault()
    //   setPassword(e.target.value)
    // }
    // const handleChange3 = e =>{
    //   e.preventDefault()
    //   setUsername(e.target.value)
    // }
    // const handleChange4 = e =>{
    //   e.preventDefault()
    //   setBirth(e.target.value)
    // }
    // const handleChange5 = e =>{
    //   e.preventDefault()
    //   setAdress(e.target.value)
    // }

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              name="username"
              label="username"
              type="text"
              id="username"
              value={username}
              autoFocus
              onChange={handleChange}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="name"
              label="name"
              type="text"
              id="name"
              value={name}
              autoFocus
              onChange={handleChange}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              value={email}
              autoFocus
              onChange={handleChange}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              value={password}
              autoComplete="current-password"
              onChange={handleChange}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="birth"
              label="birth"
              type="text"
              id="birth"
              value={birth}
              autoFocus
              onChange={handleChange}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="address"
              label="address"
              type="text"
              id="address"
              value={address}
              autoFocus
              onChange={handleChange}
            />
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign In
            </Button>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              ReSet
            </Button>
            {/* <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                  You want Sign Up?
                </Link>
              </Grid>
              <Grid item>
                <Link href="#" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid> */}
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
