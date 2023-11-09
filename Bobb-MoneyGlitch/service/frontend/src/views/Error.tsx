import { Link } from 'react-router-dom';
import ErrorImg from '@/assets/images/error.png';

export const Error = () => {
  return (
    <div className='m-auto'>
      <div className='inset-0 text-center flex flex-col justify-center p-8'>
        <div className='flex flex-col items-center'>
          <img src={ErrorImg} className='w-64 h-64 mb-4' />
          <h3 className='text-cTertiary text-5xl font-bold py-4'>Error occurred.</h3>
          <h4>Check the URL in the address bar or go back to the homepage.</h4>
          <Link to={'/'}>
            <button className='rounded bg-cTertiary p-3 mt-4 hover:bg-cQuaternary transition-all duration-300 text-cPrimary'>
              Homepage
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
};
