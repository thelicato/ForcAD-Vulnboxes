import { IProduct, IProductWithImage } from "@/types"
import { RESTManagerInstance } from "@/utils/rest"
import { useEffect, useRef, useState } from "react"
import { Buffer } from 'buffer';
import toast from "react-hot-toast"
import { sleep } from "@/utils/helpers";
import { Loading } from "@/components";
import { useBobb } from "@/context";

export const Products = () => {
  const { status, refreshStatus } = useBobb();
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [products, setProducts] = useState<IProductWithImage[]>([])
  const [modalContent, setModalContent] = useState<string>('');
  const modalRef = useRef<any>()

  const getProducts = async () => {
    try {
      const res = await RESTManagerInstance.products();
      if (res.data.products.length > 0) {
        await sleep(500)
      }
      const productsWithImages = await Promise.all(res.data.products.map(async (p: IProduct) => {
        const imageData = await getImage(p.image)
        return {
          ...p,
          imageData: imageData ?? ''
        }
      }))
      setProducts(productsWithImages)
      setIsLoading(false)
    } catch {
      toast.error("Error while loading products")
      setIsLoading(false)
    }
  }

  const getImage = async (imagePath: string) => {
    try {
      const res = await RESTManagerInstance.image(imagePath);
      return Buffer.from(res.data as unknown as any, 'binary').toString('base64')
    } catch (e) {
      console.log(e)
    }
  }

  useEffect(() => {
    getProducts()
  }, [])

  const buy = async (productId: string) => {
    try {
      const res = await RESTManagerInstance.buy(productId);
      await refreshStatus()
      setModalContent(`Product ${res.data.name}: ${res.data.value}`)
    } catch {
      setModalContent("You don't have enough money to buy this product!")
    }
    //@ts-ignore
    modalRef.current.showModal()
  }

  if (isLoading || !status) {
    return <Loading />
  }

  if (products.length === 0) {
    return <div className="container text-center m-auto"><h1 className="font-Jost font-semibold text-6xl my-8">There are no products!</h1></div>
  }
  
  return (
    <>
    <div className="container m-auto flex flex-col my-6 gap-4">
      <div className="flex flex-col items-center">
        <h2 className="font-semibold font-Jost text-4xl">Your Credit is</h2>
        <h1 className="font-semibold font-Jost text-8xl">{status.credit}</h1>
      </div>
      <h2 className="font-semibold font-Jost text-3xl">Products</h2>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        {products.map((p: IProductWithImage, key: number) => {
          return (
            <div key={key} className="bg-white flex flex-col items-center justify-between gap-4 shadow-xl drop-shadow-xl rounded-lg p-5">
              <h3 className="font-Jost font-semibold text-2xl text-center">{p.name}</h3>
              <img src={`data:;base64,${p.imageData}`} className="w-32 h-32 rounded-lg"/>
              <p className="text-center">{p.description}</p>
              <p><b>Price: </b>{p.price}</p>
              <button onClick={() => buy(p.id)} className="bg-cGreen rounded-lg px-4 py-2 text-slate-100 text-center">Buy</button>
            </div>
          )
        })}
      </div>
    </div>
    {/** Dialog */}
    <dialog ref={modalRef} className="modal">
      <div className="modal-box text-center">
        <h3 className="font-bold text-lg">Purchase result</h3>
        <p className="py-4">{modalContent}</p>
      </div>
      <form method="dialog" className="modal-backdrop">
        <button>Close</button>
      </form>
    </dialog>
    </>
  );
}