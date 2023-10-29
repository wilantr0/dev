let range = ''
function agregar (number) {
  const display = document.getElementById('display')
  display.innerHTML = range += number
  console.log(range)
}

function borrar () {
  display.innerHTML = ''
  range = ''
}

function calcular () {
  const resultado = eval(range)
  display.innerHTML = resultado
  range = resultado
}
