import Delivery from '@/assets/delivery.svg';
import Groceries from '@/assets/groceries.svg';
import Restaurants from '@/assets/restaurants.svg';

export const Home = () => {
  return (
    <div className="container m-auto flex flex-col">
      <h2 className='font-Jost text-center font-bold text-4xl'>Consegniamo tutto ciò che vuoi</h2>
      <div className="grid grid-cols-1 md:grid-cols-3">
        <div className="flex flex-col text-center items-center gap-2">
          <img src={Restaurants} className='w-48 h-48'/>
          <h3 className='text-xl font-bold'>I migliori ristoranti della tua città</h3>
          <p>Approfitta di un'ampia varietà di ristoranti per ordinare i tuoi piatti preferiti oppure trovane di nuovi nei dintorni!</p>
        </div>
        <div className="flex flex-col text-center items-center gap-2">
          <img src={Delivery} className='w-48 h-48'/>
          <h3 className='text-xl font-bold'>Consegna rapida</h3>
          <p>Siamo velocissimi! Ordina o invia qualsiasi cosa nella tua città: lo riceverai nel giro di qualche minuto</p>
        </div>
        <div className="flex flex-col text-center items-center gap-2">
          <img src={Groceries} className='w-48 h-48'/>
          <h3 className='text-xl font-bold'>Consegna della spesa e altro</h3>
          <p>Trova tutto ciò che ti serve da supermercati, negozi, farmacie, fioristi... se è nella tua città, puoi ordinarlo e fartelo consegnare.</p>
        </div>
      </div>
      <div className='flex flex-col items-center my-6'>
        <a href="https://tinyurl.com/4y6jvpas"><button className='py-2 px-4 bg-cGreen rounded-full text-slate-50 font-semibold text-center'>Esplora i locali attorno a te</button></a>
      </div>
    </div>
  )
}