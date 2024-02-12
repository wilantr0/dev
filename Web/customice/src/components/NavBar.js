'use client'

import { useState } from 'react'
import Aside from './Aside'

export default function NavBar ({ children }) {
  const [isHidden, setIsHidden] = useState(false)
  const [isRotating, setIsRotating] = useState(false)
  let state = false
  return (
    <div className=''>
      <nav className=' px-4 absolute w-full h-32 bg-sky-600 z-20 flex flex-row items-center justify-between shadow-lg'>
        <span>
          <button
            onClick={() => {
              isHidden ? setIsHidden(!isHidden) : setIsHidden(!isHidden)
              setIsRotating(!isRotating)
            }}
            className={`ml-10 transition-all ${
              isRotating ? 'rotate-90 duration-300' : '-rotate-90 duration-300'
            } `}
          >
            <img
              width='48'
              height='48'
              src='https://img.icons8.com/color/48/winter--v1.png'
              alt='winter--v1'
              className=''
            />
          </button>
        </span>
        <span>
          <button>
            <img
              width={60}
              height={60}
              src='/David.png'
              alt='profile'
              className='rounded-full'
            />
          </button>
        </span>
      </nav>
      <section className='flex flex-row justify-start items-start gap-2'>
        <div className=' mt-40 ms-7 '>{children}</div>
        <Aside isHidden={isHidden} />
      </section>
    </div>
  )
}
