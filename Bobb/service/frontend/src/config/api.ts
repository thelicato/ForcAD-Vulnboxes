interface IApiConfig {
  BASE_API: string;
  PUBLIC_ROUTES: {
    LOGIN: string;
    REGISTER: string;
    PRODUCTS: string;
    IMAGE: string;
  };
  PRIVATE_ROUTES: {
    STATUS: string;
    REDEEM: string;
    BUY: string;
    LOGOUT: string;
  };
}

export const API_CONFIG: IApiConfig = {
  BASE_API: `/api`,
  PUBLIC_ROUTES: {
    LOGIN: '/login',
    REGISTER: '/register',
    PRODUCTS: '/products',
    IMAGE: '/image',
  },
  PRIVATE_ROUTES: {
    STATUS: '/me',
    REDEEM: '/redeem',
    BUY: '/buy',
    LOGOUT: '/logout',
  },
};
