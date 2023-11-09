import { createContext, useContext, useEffect, useState } from 'react';
import { RESTManagerInstance } from '@/utils/rest';
import { IUserStatus } from '@/types';

interface ProviderInterface {
  // REST related stuff
  status: IUserStatus | undefined
  refreshStatus: () => Promise<void>
}

const BobbContext = createContext<ProviderInterface | null>(null);

const BobbProvider = ({ children }: any): any => {
  const [status, setStatus] = useState<IUserStatus>();

  const getStatus = async () => {
    try {
      const res = await RESTManagerInstance.status();
      setStatus(res.data);
    } catch {
      setStatus(undefined);
    }
  }

  useEffect(() => {
    getStatus()
  }, []);

  return (
    <BobbContext.Provider
      value={{
        status: status,
        refreshStatus: getStatus
      }}
    >
      {children}
    </BobbContext.Provider>
  );
};

const useBobb = () => {
  const context = useContext(BobbContext);
  if (!context) {
    throw new Error('useBobb must be used within BobbProvider');
  }
  return context;
};

export { BobbProvider, useBobb };
