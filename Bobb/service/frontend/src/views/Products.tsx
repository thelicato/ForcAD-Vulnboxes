import { IProduct } from "@/types"
import { RESTManagerInstance } from "@/utils/rest"
import { useEffect, useState } from "react"
import toast from "react-hot-toast"

export const Products = () => {
  const [products, setProducts] = useState<IProduct[]>([])

  const getProducts = async () => {
    try {
      const res = await RESTManagerInstance.products();
      setProducts(res.data.products)
    } catch {
      toast.error("Error while loading products")
    }
  }

  useEffect(() => {
    getProducts()
  }, [])

  if (products.length === 0) {
    return <div className="container text-center m-auto"><h1 className="font-Jost font-semibold text-6xl my-8">There are no products!</h1></div>
  }
  
  return (
    <div className="container m-auto flex flex-col my-6 gap-4">
      <h2 className="font-semibold font-Jost text-3xl">Products</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {products.map((p: IProduct, key: number) => {
          return (
            <div key={key} className="bg-white shadow-xl drop-shadow-xl rounded-lg p-5">
              {p.name}
              {p.image}
              {p.description}
              {p.price}
              {p.id}
            </div>
          )
        })}
      </div>
    </div>
  );
}