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

export interface IProduct {
  id: string;
  name: string;
  description: string;
  image: string;
  price: number;
}

export interface IProductWithImage extends IProduct {
  imageData: string;
}

export interface IProductReveal {
  id: string;
  name: string;
  value: string;
}