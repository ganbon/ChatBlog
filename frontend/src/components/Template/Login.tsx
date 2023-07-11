import * as React from 'react';
import type { NextPage } from 'next';
import MultipleTextField from '../Atoms/MultipleTextField';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import MultipleButton from "../Atoms/MultipleButton";

const commonStyles = {
  m: 1,
  width: '18rem',
  height: '15rem',
  margin: 10,
  boxShadow: 3,
  textAlign: "center"
};
const Login:NextPage = () =>{
  const [inputItemName, setInputItemName] = React.useState<string>('');
  const [inputPassword, setInputPassword] = React.useState<string>('');
  
  return(
    <Grid container direction="column" alignItems="center">     
      {/* ログイン */}
      <Box sx = {{ marginTop:4, marginLeft:10 }}>
        <h1>ログイン</h1>
      </Box>

      {/* ユーザー名入力 */}
      <Box sx = {{ marginTop:4, marginLeft:10 }}>
        <MultipleTextField id="outlined-basic" label="ユーザ名" variant="outlined" text={inputItemName} setText={setInputItemName}/>
      </Box>

      {/* パスワード入力 */}
      <Box sx = {{ marginTop:4, marginLeft:10 }}>
        <MultipleTextField id="outlined-password-input" label="パスワード" type="password" text={inputPassword} setText={setInputPassword}/>
      </Box>
      
      {/* ログインボタン */}
      <Box sx = {{ marginTop:4, marginLeft:10 }}>
        <MultipleButton text="ログイン" variant="contained" 
          handleClick={() => window.location.href='/home'}/>
      </Box>
    </Grid>  
  )
}

export default Login;