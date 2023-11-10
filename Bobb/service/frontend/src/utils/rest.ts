import { AxiosResponse } from 'axios';
import { http, cookieHttp, imageHttp } from '@/utils/axios';
import { API_CONFIG } from '@/config';
import { IGenericRes, ILoginOrRegisterReq, IProductReveal, IProductsRes, IRedeemReq, IStatusRes } from '@/types';

class RESTManager {
  async login(data: ILoginOrRegisterReq): Promise<AxiosResponse<IStatusRes>> {
    const res = await http.post<IStatusRes>(API_CONFIG.PUBLIC_ROUTES.LOGIN, data);
    return res;
  }

  async register(data: ILoginOrRegisterReq): Promise<AxiosResponse<IGenericRes>> {
    const res = await http.post<IGenericRes>(API_CONFIG.PUBLIC_ROUTES.REGISTER, data);
    return res;
  }

  async products(): Promise<AxiosResponse<IProductsRes>> {
    const res = await http.get<IProductsRes>(API_CONFIG.PUBLIC_ROUTES.PRODUCTS);
    return res;
  }

  async image(path: string): Promise<AxiosResponse> {
    const res = await imageHttp.get(`${API_CONFIG.PUBLIC_ROUTES.IMAGE}/${path}`);
    return res;
  }

  async logout(): Promise<AxiosResponse<IGenericRes>> {
    const res = await cookieHttp.post<IGenericRes>(API_CONFIG.PRIVATE_ROUTES.LOGOUT);
    return res;
  }

  async status(): Promise<AxiosResponse<IStatusRes>> {
    const res = await cookieHttp.get<IStatusRes>(API_CONFIG.PRIVATE_ROUTES.STATUS);
    return res;
  }

  async redeem(data: IRedeemReq): Promise<AxiosResponse<IGenericRes>> {
    const res = await cookieHttp.post<IGenericRes>(API_CONFIG.PRIVATE_ROUTES.REDEEM, data);
    return res;
  }

  async buy(data: IRedeemReq): Promise<AxiosResponse<IProductReveal>> {
    const res = await cookieHttp.post<IProductReveal>(API_CONFIG.PRIVATE_ROUTES.REDEEM, data);
    return res;
  }
}

export const RESTManagerInstance = new RESTManager();
