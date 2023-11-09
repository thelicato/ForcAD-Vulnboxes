import { FaGithub } from 'react-icons/fa';
import { FaXTwitter } from 'react-icons/fa6';

export const Footer = () => {
  return (
    <footer className='mt-4 bg-cBlack text-slate-100 p-4'>
      <div className='w-full grid grid-cols-3 gap-4'>
        {/* Left links */}
        <div className='flex justify-center md:justify-start col-span-3 md:col-span-1'>
          <a
            className='ml-3 text-cYellow'
            href='https://github.com/cybersecsi'
            target='_blank'
            rel='noopener noreferrer'
          >
            <FaGithub size={24} />
          </a>
          <a
            className='ml-3 text-cYellow'
            href='https://twitter.com/cybersecsi'
            target='_blank'
            rel='noopener noreferrer'
          >
            <FaXTwitter size={24} />
          </a>
        </div>
        {/* SecSI credits */}
        <div className='text-center col-span-3 md:col-span-1'>
          A{' '}
          <a
            className='text-cYellow'
            href='https://secsi.io'
            target='_blank'
            rel='noreferrer'
          >
            SecSI
          </a>{' '}
          project
        </div>
      </div>
    </footer>
  );
};