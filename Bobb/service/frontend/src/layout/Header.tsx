import Pizza from '@/assets/pizza.svg?react'
import Curvy from '@/assets/curvy-yellow.png'

export const Header = () => {
  return (
    <>
    <header className="bg-cYellow h-20 sticky">
      <div className="container m-auto">
        <h1 className="font-Belanosima text-5xl h-full p-2 text-slate-800">Bobb</h1>
        <nav></nav>
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