import { IProduct, IProductWithImage } from "@/types"
import { RESTManagerInstance } from "@/utils/rest"
import { useEffect, useState } from "react"
import toast from "react-hot-toast"

export const Products = () => {
  const [products, setProducts] = useState<IProductWithImage[]>([])

  const getProducts = async () => {
    try {
      const res = await RESTManagerInstance.products();
      const productsWithImages = await Promise.all(res.data.products.map(async (p: IProduct) => {
        const imageData = await getImage(p.image)
        return {
          ...p,
          imageData: imageData
        }
      }))
      setProducts(productsWithImages)
    } catch {
      toast.error("Error while loading products")
    }
  }

  const getImage = async (imagePath: string) => {
    const res = await RESTManagerInstance.image(imagePath);
    return Buffer.from(res.data as unknown as any, 'binary').toString('base64')
  }

  useEffect(() => {
    getProducts()
  }, [])

  const buy = async (productId: string) => {
    try {
      const res = await RESTManagerInstance.buy(productId);
    } catch {

    }

  }

  if (products.length === 0) {
    return <div className="container text-center m-auto"><h1 className="font-Jost font-semibold text-6xl my-8">There are no products!</h1></div>
  }
  
  return (
    <>
    <div className="container m-auto flex flex-col my-6 gap-4">
      <h2 className="font-semibold font-Jost text-3xl">Products</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {products.map((p: IProductWithImage, key: number) => {
          return (
            <div key={key} className="bg-white flex flex-col shadow-xl drop-shadow-xl rounded-lg p-5">
              <h3 className="font-Jost text-xl text-center">{p.name}</h3>
              <img src={`data:;base64,${p.imageData}`} className="w-20 h-20 rounded"/>
              <p>{p.description}</p>
              <p><b>Price: </b>{p.price}</p>
              <button onClick={() => buy(p.id)} className="bg-cGreen rounded-lg p-2 text-center">Buy</button>
            </div>
          )
        })}
      </div>
    </div>
    {/** Dialog */}
    <dialog id="my_modal_2" className="modal">
      <div className="modal-box">
        <h3 className="font-bold text-lg">Hello!</h3>
        <p className="py-4">Press ESC key or click outside to close</p>
      </div>
      <form method="dialog" className="modal-backdrop">
        <button>close</button>
      </form>
    </dialog>
    </>
  );
}