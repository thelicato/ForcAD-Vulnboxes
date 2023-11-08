import { useState } from "react";
import { EyeIcon, EyeSlashIcon } from "@heroicons/react/24/solid";

interface PasswordInputProps
  extends React.InputHTMLAttributes<HTMLInputElement> {
  register?: any;
}

const iconClasses =
  "bg-slate-100 hover:bg-slate-200 cursor-pointer rounded-md p-1 mt-[-16px] transition-colors duration-300";

export const PasswordInput: React.FC<PasswordInputProps> = ({
  register,
  ...props
}: PasswordInputProps) => {
  const [showPassword, setShowPassword] = useState<boolean>(false);
  const Icon = showPassword ? EyeSlashIcon : EyeIcon;
  return (
    <div className="relative">
      <input
        className={`custom-textfield ${props.className}`}
        {...register}
        {...props}
        type={showPassword ? "text" : "password"}
      />
      <div className="absolute right-2 inset-y-1/2">
        <Icon
          className={iconClasses}
          onClick={() => setShowPassword((old) => !old)}
        />
      </div>
    </div>
  );
};