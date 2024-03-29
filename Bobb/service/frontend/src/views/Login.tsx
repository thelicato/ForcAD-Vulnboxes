import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import toast from 'react-hot-toast';
import { useForm } from 'react-hook-form';
import { RESTManagerInstance } from '@/utils/rest';
import { ILoginOrRegisterReq } from '@/types';
import { Loading, PasswordInput } from '@/components';
import { sleep } from '@/utils/helpers';
import { useBobb } from '@/context';

type loginInputs = {
  username: string;
  password: string;
};

export const Login = () => {
  const { refreshStatus } = useBobb();
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const loginForm = useForm<loginInputs>();

  const login = async (inputData: loginInputs) => {
    try {
      setIsLoading(true);
      const loginData: ILoginOrRegisterReq = {
        username: inputData.username,
        password: inputData.password,
      };
      await RESTManagerInstance.login(loginData);
      await refreshStatus();
      await sleep(500); // Just to show the spinner
      setIsLoading(false);
      toast.success('Login completed successfully');
      await sleep(500); // Just to show the toast message
      navigate('/products');
    } catch (err) {
      const errMsg = 'Error during login';
      await sleep(500); // Just to show the spinner
      setIsLoading(false);
      toast.error(errMsg);
    }
  };

  if (isLoading) {
    return <Loading />;
  }

  return (
    <>
      <div className='w-full h-full m-auto font-Jost'>
        <div className='flex flex-col m-auto justify-center items-center w-5/6 sm:w-3/6 lg:w-4/12 xl:w-3/12 2xl:w-1/6 h-full text-center'>
          <h2 className="font-semibold font-Jost text-3xl">Login</h2>
          <div className='card bg-white shadow-xl w-full mt-8 p-8'>
            <form className='grid grid-cols-1 gap-5' onSubmit={loginForm.handleSubmit(login)}>
              <input
                className='h-12 bg-white shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
                type='text'
                placeholder='Username'
                {...loginForm.register('username', { required: true })}
              />
              <PasswordInput
                className='h-12 bg-white shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
                type='password'
                placeholder='Password'
                register={loginForm.register('password', { required: true })}
              />
              <button
                type='submit'
                disabled={!loginForm.formState.isValid}
                className='flex w-full items-center justify-center disabled:bg-gray-500  h-12  p-2 rounded-md bg-cGreen text-white'
              >
                Login
              </button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};