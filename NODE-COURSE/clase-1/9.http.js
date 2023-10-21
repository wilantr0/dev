const http = require('node:http')
const { findAvailiblePort } = require('./10.free-port.js')

const server = http.createServer((req, res) => {
  console.log('request recived')
  res.end('Hola Mundo')
})

findAvailiblePort(3000).then(port => {
  server.listen(port, () => {
    console.log(`Server is listening on port http://localhost:${port}`)
  })
})
