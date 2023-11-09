import Pizza from '@/assets/pizza.svg?react'
import Curvy from '@/assets/curvy-yellow.png'
import { useBobb } from '@/context';
import toast from 'react-hot-toast';
import { RESTManagerInstance } from '@/utils/rest';
import { Link } from 'react-router-dom';

interface INavlink {
  name: string;
  link: string;
}

const PUBLIC_LINKS: INavlink[] = [
  { name: 'Signup', link:'/signup' },
  { name: 'Login', link:'/login' }
]

const PRIVATE_LINKS: INavlink[] = [
  { name: 'Profile', link:'/profile' },
  { name: 'Products', link:'/products' },
]

export const Header = () => {
  const { status } = useBobb();

  const logout = async () => {
    try {
      await RESTManagerInstance.logout();
      location.reload()
    } catch {
      toast.error("Error during logout")
    }
  }

  return (
    <>
    <header className="bg-cYellow h-20 sticky">
      <div className="flex justify-between items-center container m-auto">
        <Link to='/'><h1 className="font-Belanosima text-5xl h-full p-2 text-slate-800">Bobb</h1></Link>
        <nav>{status ? (
          <div className='flex gap-8'>
            {PRIVATE_LINKS.map((link: INavlink, key: number) => {
              return (
                <Link to={link.link}> 
                  <button
                    className="default-tr text-cBlack"
                    key={key}
                  >
                    {link.name}
                  </button>
                </Link>
              );
            })}
            <button onClick={logout} className="text-cBlack">Logout</button>
          </div> ) : (
          <div className='flex gap-8'>
            {PUBLIC_LINKS.map((link: INavlink, key: number) => {
              return (
                <Link to={link.link}>
                  <button
                  className="default-tr text-cBlack"
                  key={key}
                  >
                    {link.name}
                  </button>
                </Link>
              );
            })}
          </div>
          )}
        </nav>
      </div>
    </header>

    <div className="flex flex-col items-center h-80 bg-cYellow m-auto text-center">
      <Pizza className='w-24 h-24'/>
      <h2 className='font-Jost text-6xl mt-6 font-bold'>The best pizza in Cercola</h2>
    </div>
    <img src={Curvy} className='w-screen' />
    </>
  )
}