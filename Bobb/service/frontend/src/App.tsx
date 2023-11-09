import { AppRouter } from '@/AppRouter';
import { RouterProvider } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import { BobbProvider} from '@/context';

export const App = () => {
  return (
    <BobbProvider>
        <RouterProvider router={AppRouter} />
        <Toaster position='bottom-left' />
    </BobbProvider>
  );
};
