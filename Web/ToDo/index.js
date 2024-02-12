const inputTD = document.getElementById('todo')
const toDos = document.getElementById('toDos')
const stats = document.getElementById('stats')

let idCounter = 0
let pendientes = 0
let completadas = 0

function añadir () {
  if (inputTD.value != '') {
    console.log(inputTD.value)
    toDos.innerHTML += `
    <span class="task" id=${idCounter++}>
      <h2>${inputTD.value}</h2>
      <button class="delete" onclick="eliminar(this)">
        <span class="material-symbols-outlined">done</span>
      </button>
    </span>`
    inputTD.value = ''
    pendientes += 1
    stats.innerHTML = `<h3>Tareas Pendientes: ${pendientes}</h3> <h3>Tareas Completadas: ${completadas}</h3>`
  }
}

function eliminar (btn) {
  const idEliminar = btn.parentElement.getAttribute('id')
  const eliminar = document.getElementById(idEliminar)

  eliminar.classList.add('remove')

  pendientes -= 1
  completadas += 1
  stats.innerHTML = `<h3>Tareas Pendientes: ${pendientes}</h3> <h3>Tareas Completadas: ${completadas}</h3>`
  setTimeout(() => {
    eliminar.parentNode.removeChild(eliminar)
  }, 2000)
}

stats.innerHTML = `<h3>Tareas Pendientes: ${pendientes}</h3> <h3>Tareas Completadas: ${completadas}</h3>`

function enviar (e) {
  if (e.keyCode === 13 && !e.shiftKey) {
    e.preventDefault()
    añadir()
  }
}
