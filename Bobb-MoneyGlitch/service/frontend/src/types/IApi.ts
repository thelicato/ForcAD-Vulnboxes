/**
 * Interfaces for requests
 */

import { IUserStatus } from "@/types/ICommon";

export interface ILoginOrRegisterReq {
  username: string;
  password: string;
}

export interface IRedeemReq {
  coupon: string
}


/**
 * Interfaces for responses
 */

export interface IGenericRes {
  message: string
}

export interface IStatusRes extends IUserStatus {};