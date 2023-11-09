import axios, { AxiosInstance } from 'axios';
import { API_CONFIG } from '@/config';

//const baseURL = import.meta.env.MODE ==='development' ? `http://localhost:500${API_CONFIG.BASE_API}` : API_CONFIG.BASE_API;

const baseURL = API_CONFIG.BASE_API;

const instance: AxiosInstance = axios.create({
  baseURL: baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
});

const loggedInstance: AxiosInstance = axios.create({
  baseURL: baseURL,
  headers: {
    "Content-Type": 'application/json'
  },
  withCredentials: true,
})


export const http = instance;
export const cookieHttp = loggedInstance;
