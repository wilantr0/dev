const fs = require('node:fs/promises')
const path = require('node:path')
const pc = require('picocolors')

const folder = process.argv[2] ?? '.'

async function ls (folder) {
  let files
  try {
    files = await fs.readdir(folder)
  } catch {
    console.log(pc.red(`❌ No se pudo leer el directorio ${pc.bold(folder)}`))
    process.exit(1)
  }

  const filesPromise = files.map(async file => {
    const filePath = path.join(folder, file)
    let stats

    try {
      stats = await fs.stat(filePath)
    } catch {
      console.error('No se pudo leer el archivo', filePath)
      process.exit(1)
    }

    const isDirectory = stats.isDirectory()
    const fileType = isDirectory ? '📂' : '📃'
    const fileSize = stats.size.toString()
    const fileModified = stats.mtime.toLocaleString()

    return `${fileType} ${pc.cyan(file.padEnd(20))} ${
      fileSize <= 500
        ? pc.green(fileSize.padStart(10))
        : pc.magenta(fileSize.padStart(10))
    } ${pc.yellow(fileModified)}`
  })

  const filesInfo = await Promise.all(filesPromise)

  filesInfo.forEach(fileInfo => console.log(fileInfo))
}

ls(folder)
