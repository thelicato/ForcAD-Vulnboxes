import { AxiosResponse } from 'axios';
import { http, cookieHttp } from '@/utils/axios';
import { API_CONFIG } from '@/config';
import { IGenericRes, ILoginOrRegisterReq, IRedeemReq, IStatusRes } from '@/types';

class RESTManager {
  async login(data: ILoginOrRegisterReq): Promise<AxiosResponse<IStatusRes>> {
    const res = await http.post<IStatusRes>(API_CONFIG.PUBLIC_ROUTES.LOGIN, data);
    return res;
  }

  async register(data: ILoginOrRegisterReq): Promise<AxiosResponse<IGenericRes>> {
    const res = await http.post<IGenericRes>(API_CONFIG.PUBLIC_ROUTES.REGISTER, data);
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
}

export const RESTManagerInstance = new RESTManager();
