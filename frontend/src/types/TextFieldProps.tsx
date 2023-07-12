import { SxProps, Theme } from '@mui/material/styles';

type TextFieldPropsType = {
  id?: string;
  label?: string;
  text: string;
  setText: (value: string) => void;
  variant?: 'filled' | 'outlined' | 'standard';
  placeholder?: string;
  sx?: SxProps<Theme>;
  type?: string;
};

export default TextFieldPropsType;