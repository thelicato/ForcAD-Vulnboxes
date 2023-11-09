interface IPublicRoutes {
  HOME_ROUTE: string;
  LOGIN_ROUTE: string;
  REGISTER_ROUTE: string;
}

interface IPrivateRoutes {
  PRODUCTS_ROUTE: string;
  PROFILE_ROUTE: string;
}

export const PUBLIC_REACT_ROUTES: IPublicRoutes = {
  HOME_ROUTE: '/',
  LOGIN_ROUTE: '/login',
  REGISTER_ROUTE: '/signup',
};

export const PRIVATE_REACT_ROUTES: IPrivateRoutes = {
  PRODUCTS_ROUTE: '/products',
  PROFILE_ROUTE: '/profile',
};
