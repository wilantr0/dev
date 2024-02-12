import { getCoverImage, getGames } from '@/services/videogames'
import Link from 'next/link'
import { API_URL } from '@/app/config'
import mdToHTML from './snarkdown'
import Pagination from './components/pagination'

export default async function Home ({ searchParams }) {
  const { page } = searchParams
  console.log(page)
  const { data: games, pagination } = await getGames({ page: +page })
  return (
    <main className='flex min-h-screen flex-col items-center p-24 '>
      {games.map(({ id, attributes }) => (
        <Link
          href={attributes.slug}
          target='_BLANK'
          class=' m-2 flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700'
          key={id}
        >
          <img
            class='object-cover w-full rounded-t-lg h-96 md:h-auto md:w-48 md:rounded-none md:rounded-s-lg'
            src={getCoverImage({ attributes })}
            alt=''
          />
          <div class='flex flex-col justify-between p-4 leading-normal'>
            <h5 class='mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white'>
              {attributes.title}
            </h5>
            <p
              class='mb-3 font-normal text-gray-700 dark:text-gray-400'
              dangerouslySetInnerHTML={{
                __html: mdToHTML(attributes.description)
              }}
            />
          </div>
        </Link>
      ))}
      <Pagination pagination={pagination} />
    </main>
  )
}
