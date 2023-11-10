import { Loading } from "@/components";
import { useBobb } from "@/context";
import { ICoupon, IRedeemReq } from "@/types";
import { sleep } from "@/utils/helpers";
import { RESTManagerInstance } from "@/utils/rest";
import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import toast from "react-hot-toast";

export const Profile = () => {
  const { status, refreshStatus } = useBobb();
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const redeemForm = useForm<IRedeemReq>();

  useEffect(() => {
    const throttleStatus = async () => {
      await sleep(1000);
      setIsLoading(false)
    }

    if (status) {
      throttleStatus()
    }
  }, [status])

  const redeem = async (redeemData: IRedeemReq) => {
    try {
      setIsLoading(true);
      await RESTManagerInstance.redeem(redeemData);
      await refreshStatus();
      redeemForm.setValue('coupon', '')
      await sleep(500); // Just to show the spinner
      setIsLoading(false);
      toast.success('Coupon redeem completed successfully');
      await sleep(500); // Just to show the toast message
    } catch (err) {
      const errMsg = 'Error during redeem';
      redeemForm.setValue('coupon', '')
      await sleep(500); // Just to show the spinner
      setIsLoading(false);
      toast.error(errMsg);
    }
  }
  

  if (isLoading || !status) {
    return <Loading />
  }

  const coupons = status?.coupons as ICoupon[]

  return (
    <div className="container m-auto flex flex-col my-6 gap-4">
      <div className="flex flex-col items-center">
        <h2 className="font-semibold font-Jost text-4xl">Your Credit is</h2>
        <h1 className="font-semibold font-Jost text-8xl">{status.credit}</h1>
      </div>
      <h2 className="font-semibold font-Jost text-3xl">Your Coupons</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {coupons.map((c:ICoupon, key: number) => {
          return (
            <div key={key} className="bg-white shadow-xl drop-shadow-xl rounded-lg p-5">
              <p><b>Code: </b>{c.coupon}</p>
              <p><b>Value: </b>{c.value}</p>
            </div>
          )
        })}
      </div>
      <h2 className="font-semibold font-Jost text-3xl">Redeem</h2>
      <p>Redeem a coupon</p>
      <form className='grid grid-cols-1 gap-5' onSubmit={redeemForm.handleSubmit(redeem)}>
        <input
          className='h-12 bg-white shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
          type='text'
          placeholder='Coupon'
          {...redeemForm.register('coupon', { required: true })}
        />
        <button
          type='submit'
          disabled={!redeemForm.formState.isValid}
          className='flex w-full items-center justify-center disabled:bg-gray-500  h-12  p-2 rounded-md bg-cGreen text-white'
        >
          Redeem
        </button>
      </form>
    </div>
  );
}