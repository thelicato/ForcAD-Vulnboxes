import { Link } from 'react-router-dom';
import NoMatchImg from '@/assets/images/404.png';

export const NoMatch = () => {
  return (
    <div className='m-auto'>
      <div className='inset-0 text-center flex flex-col justify-center p-8'>
        <div className='flex flex-col items-center'>
          <img src={NoMatchImg} className='w-72 h-72 mb-4' />
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
