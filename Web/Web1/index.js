const random = Math.floor(Math.random() * 101)
const counter = document.getElementById('contador')
const input = document.getElementById('number')
const solucion = document.getElementById('solucion')
const boton = document.getElementById('submit')
const intentos = document.getElementById('intentos')
let contador = 5
counter.innerText = contador.toString()

function send () {
  let mensaje = ''

  if (input.value >= 0 && input.value != '') {
    if (input.value < random) {
      mensaje = 'El numero a adivinar es mas alto'
      solucion.innerText = mensaje
      contador = contador - 1
    } else if (input.value > random) {
      mensaje = 'El numero a adivinar es mas bajo'
      solucion.innerText = mensaje
      contador = contador - 1
    } else {
      mensaje = 'Correcto, ahora intenta adivinar el siguiente'
      solucion.innerText = mensaje
      intentos.classList.add('hidden')
      boton.innerHTML =
        '<button id="submit" onClick="location.reload()">Volver a intentar</button>'
    }
    counter.innerText = contador.toString()
    if (contador == 0) {
      mensaje =
        'Joder qué malo eres chaval. Inténtalo otra vez. Que el numero era el ' +
        random
      solucion.innerText = mensaje
      intentos.classList.add('hidden')
      boton.innerHTML =
        '<button id="submit" class="reddy" onClick="location.reload()">Volver a intentar</button>'
    }
  } else {
    contador = contador
  }
}

function enviar (e) {
  if (e.keyCode === 13 && !e.shiftKey) {
    e.preventDefault()
    send()
  }
}
