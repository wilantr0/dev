import axios from 'axios'
import { conn } from '/src/libs/db'
import { NextResponse } from 'next/server'

export async function GET () {
  try {
    const res = await conn.query('SELECT * FROM prueba')
    return NextResponse.json(res)
  } catch (e) {
    console.log(e)
    return NextResponse.json({ message: e.message }, { status: 500 })
  }
}

export async function POST (req) {
  try {
    const res = await conn.query('INSERT INTO prueba SET ?', {
      name: 'Ramón',
      description: 'Ramón',
      price: 15
    })

    console.log(res)

    return NextResponse.json({
      name,
      description,
      price,
      id
    })
  } catch (e) {
    console.log(e)
    return NextResponse.json({ message: e.message }, { status: 500 })
  }
}
