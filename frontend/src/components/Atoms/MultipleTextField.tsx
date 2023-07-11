import TextField from '@mui/material/TextField';
import TextFieldPropsType from '@/types/TextFieldProps';

// テキストの入力
export const MultipleTextField = (props: TextFieldPropsType) => {
  return (
    <>
      <TextField 
        id={props.id}
        label={props.label}
        value={props.text}
        onChange={(event) => props.setText(event.target.value)}
        variant={props.variant}
        type={props.type}
        placeholder={props.placeholder}
        sx={props.sx} 
      />
    </>
  )
}

export default MultipleTextField;