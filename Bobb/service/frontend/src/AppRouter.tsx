import { createBrowserRouter, Outlet, redirect, RouteObject } from 'react-router-dom';
import { ErrorBoundary } from 'react-error-boundary';
import { Header, Content, Footer } from '@/layout';
import {
  Home,
  Products,
  Profile,
  Signup,
  Login,
  NoMatch,
  Error,
} from '@/views';
import { PRIVATE_REACT_ROUTES, PUBLIC_REACT_ROUTES } from '@/config';
import { removeSlash } from '@/utils/helpers';
import { RESTManagerInstance } from '@/utils/rest';

const userLoader = async (): Promise<boolean> => {
  try {
    await RESTManagerInstance.status();
    return true;
  } catch {
    return false;
  }
};

const routeLoader = async (redirectEndpoint: string) => {
  const isLoggedIn = await userLoader();
  if (!isLoggedIn) {
    return redirect(redirectEndpoint);
  }
  return null;
};

const NoMatchElement = () => {
  return <NoMatch />;
};

const DefaultLayout = () => {
  return (
    <ErrorBoundary fallback={<Error />}>
      <Header />
      <Content>
        <Outlet />
      </Content>
      <Footer />
    </ErrorBoundary>
  );
};

const RouteObjects: RouteObject[] = [
  {
    element: <DefaultLayout />,
    children: [
      {
        path: removeSlash(PUBLIC_REACT_ROUTES.HOME_ROUTE),
        element: <Home />,
      },
      {
        path: removeSlash(PUBLIC_REACT_ROUTES.LOGIN_ROUTE),
        element: <Login />,
        loader: async () => {
          const isLoggedIn = await userLoader();
          if (isLoggedIn) {
            return redirect('/');
          } else {
            return null;
          }
        },
      },
      {
        path: removeSlash(PUBLIC_REACT_ROUTES.REGISTER_ROUTE),
        element: <Signup />,
        loader: async () => {
          const isLoggedIn = await userLoader();
          if (isLoggedIn) {
            return redirect('/');
          } else {
            return null;
          }
        },
      },
      {
        path: removeSlash(PRIVATE_REACT_ROUTES.PRODUCTS_ROUTE),
        element: <Products />,
        loader: async () => await routeLoader(PUBLIC_REACT_ROUTES.LOGIN_ROUTE),
      },
      {
        path: removeSlash(PRIVATE_REACT_ROUTES.PROFILE_ROUTE),
        element: <Profile />,
        loader: async () => await routeLoader(PUBLIC_REACT_ROUTES.LOGIN_ROUTE),
      },
    ],
  },
];


export const AppRouter = createBrowserRouter([
  {
    path: '',
    children: RouteObjects,
  },
  { path: '*', element: <NoMatchElement /> },
]);
