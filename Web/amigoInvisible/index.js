const correo = document.getElementById('correo')
const texto = document.getElementById('mail-coint')
const superp = document.getElementById('cont-selections')
let selecciones = document.getElementById('selecciones')

const correos = []
let parejas = []

function elegir () {
  let correos1 = [...correos]
  let correos2 = [...correos]
  while (correos1.length > 0) {
    let choice = Math.floor(Math.random() * correos1.length)
    let choice2 = Math.floor(Math.random() * correos2.length)
    if (choice != choice2 || correos.length == 1) {
      console.log(choice)
      console.log(choice2)
      console.log(correos1)
      console.log(correos2)
      correos1.splice(choice, 1)
      correos2.splice(choice2, 1)
      if (correos1[choice] == correos2[choice2]) {
        elegir()
      }
      parejas.push([correos1[choice], correos2[choice2]])
    } else {
      continue
    }
  }
  console.log(parejas)
}

function añadir () {
  const nuevoCorreo = correo.value
  nuevoCorreo != '' ? correos.push(nuevoCorreo) : (correos = correos)
  texto.innerText = correos.join(`
  `)
  correo.value = ''
}

function eliminar () {
  correos.pop()
  texto.innerText = correos.join(`
  `)
  correo.value = ''
}


function main () {
  console.log(correos)
  superp.classList.remove('hidden')
  const newList = document.createElement('ul')
  newList.id = 'selecciones'
  superp.append(newList)
  selecciones = document.getElementById('selecciones')

  elegir()

  for (const element in correos) {
    console.log(correos[element])
    const newItem = document.createElement('li')
    newItem.appendChild(document.createTextNode(correos[element]))
    selecciones.appendChild(newItem)
  }
}

function closeWin () {
  superp.classList.add('hidden')
  texto.innerText = ''
  correos = []
  selecciones.innerHTML = ''
  parejas = []
}
