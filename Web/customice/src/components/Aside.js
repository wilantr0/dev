import React from 'react'

export default function Aside ({ isHidden }) {
  return (
    <aside
      className={` flex flex-col gap-2 absolute -left-0 -top-full z-0 w-32 h-screen bg-sky-600/60 transition-all duration-200 ${
        isHidden ? '' : 'translate-y-full'
      } `}
    >
      <button className=' flex justify-center items-center mt-32 w-full bg-sky-600 h-56'>
        <img
          width='64'
          height='64'
          src='https://img.icons8.com/pastel-glyph/64/cap--v2.png'
          alt='cap--v2'
        />
      </button>
      <button className=' flex justify-center items-center w-full bg-sky-600 h-56'>
        <img
          width='64'
          height='64'
          src='https://img.icons8.com/pastel-glyph/64/t-shirt--v3.png'
          alt='t-shirt--v3'
        />
      </button>
      <button className=' flex justify-center items-center w-full bg-sky-600 h-56'>
        <img
          width='64'
          height='64'
          src='https://img.icons8.com/pastel-glyph/64/christmas-stocking--v3.png'
          alt='christmas-stocking--v3'
        />
      </button>
      <button className=' flex justify-center items-center w-full bg-sky-600 h-56'>
        <img src='' alt='' />
      </button>
      <button className=' flex justify-center items-center w-full bg-sky-600 h-56'>
        <img src='' alt='' />
      </button>
    </aside>
  )
}
