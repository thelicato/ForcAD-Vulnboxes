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
  
  return <>{products.map((p: IProduct, key: number) => {
    return (
      <div key={key}>
        {p.name}
        {p.image}
        {p.description}
        {p.price}
      </div>
    )
  })}</>
}