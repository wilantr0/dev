import Link from 'next/link'

export default function Pagination ({ pagination }) {
  let { page, pageCount, total } = pagination
  const isFirstPage = page === 1
  const isLastPage = page === pageCount

  const nextPage = page + 1
  const prevPage = page - 1

  const prevPageUrl = isFirstPage ? '#' : `?page=${prevPage}`
  const nextPageUrl = isLastPage ? '#' : `?page=${nextPage}`

  return (
    <div className='flex flex-col items-center mt-6'>
      <span className='text-sm text-gray-700 dark:text-gray-400'>
        Mostrando{' '}
        <span className='font-semibold text-gray-900 dark:text-white'>1</span>{' '}
        to{' '}
        <span className='font-semibold text-gray-900 dark:text-white'>10</span>{' '}
        of{' '}
        <span className='font-semibold text-gray-900 dark:text-white'>100</span>{' '}
        Entries
      </span>

      <div className='inline-flex mt-2 xs:mt-0'>
        <Link
          href={prevPageUrl}
          disabled={isFirstPage}
          className={`${
            isFirstPage ? 'pointer-events-none opacity-50' : ''
          } flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 rounded-s hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white`}
        >
          Prev
        </Link>
        <Link
          href={nextPageUrl}
          disabled={isLastPage}
          className={`${
            isLastPage ? 'pointer-events-none opacity-50' : ''
          } flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 border-0 border-s border-gray-700 rounded-e hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white`}
        >
          Next
        </Link>
      </div>
    </div>
  )
}
