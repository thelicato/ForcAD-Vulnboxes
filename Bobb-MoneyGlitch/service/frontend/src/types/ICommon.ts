export interface ICoupon {
  coupon: string,
  value: number,
}

export interface IUserStatus {
  id: string;
  username: string;
  credit: number;
  coupons: ICoupon[]
}