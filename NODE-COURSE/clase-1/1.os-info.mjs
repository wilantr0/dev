import os from 'node:os'

console.log('Información del sistema operativo: ')
console.log('-------------------')
console.log('Nombre del OS', os.platform())
console.log('Nombre del sistema', os.hostname())
console.log('Version del sistema', os.release())
console.log('Arquitectura', os.arch())
console.log('CPU', os.cpus().length)
console.log('Free Memory', os.freemem() / 1024 / 1024)
console.log('Total Memory', os.totalmem() / 1024 / 1024)
