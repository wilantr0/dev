import { conn } from '@/libs/db'
import axios from 'axios'
import { NextResponse } from 'next/server'

export async function GET () {
  const res = await conn.query('SELECT * FROM products')
}
export async function POST (req) {
  NextResponse.json(req)
}
