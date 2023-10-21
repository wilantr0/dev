// argumentos de entrada
const inputs = process.argv

inputs.forEach(input => {
  console.log(input)
})

// controlar eventos del proceso
// process.on('exit', () =>{
//  //limpiar los recursos
// })

// current working directory
console.log(process.cwd())

// controlar el proceso y su salida
// process.exit(1)

console.log(process.env.PEPITO)
