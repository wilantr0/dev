import { API_URL } from '@/app/config'

export async function getGames ({ page = 1 }) {
  console.log(page)
  const res = await fetch(
    `${API_URL}/api/videogames?populate[platforms][fields][0]=name&populate[cover][fields][0]=url&pagination[page]=${page}&pagination[pageSize]=1]`
  )
  console.log(res)

  if (!res.ok) {
    throw new Error(`Ooops! Something went wrong.${page}`)
  }

  const { data, meta } = await res.json()
  const { pagination } = meta
  return { data, pagination }
}

export function getCoverImage ({ attributes }) {
  const url = attributes.cover.data.attributes.url
  return `${API_URL}${url}`
}
