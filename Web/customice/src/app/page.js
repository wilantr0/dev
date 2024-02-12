import { conn } from '@/libs/db'

const products = await conn.query('Select * from product')

console.log(products)

export default function Home () {
  return <main>Que PAsa LOKOSS</main>
}
