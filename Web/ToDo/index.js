let idCounter = 0

userInput.addEventListener('submit', e => {
  e.preventDefault()
  const inputTask = document.getElementById('task')
  const task = inputTask.value
  console.log(task)
  addTask(task, inputTask)
})

const addTask = (task, inputTask) => {
  const list = document.querySelector('.list-container')

  list.innerHTML += `<div class="task-container" id=${(idCounter += 1)}>
      <label>
        <input type="checkbox" name="" id="checked">
        ${task}
      </label>
      <img src="./img/icons8-basura-llena-30.png" class="closeBtn">
    </div>`

  inputTask.value = ''
  updateStats()
}

list.addEventListener('click', event => {
  if (event.srcElement.nodeName == 'INPUT') {
    updateStats()
  } else if (event.srcElement.nodeName == 'IMG') {
    const taskId = event.srcElement.parentNode.id
    deleteTask(taskId)
  }
})

const updateStats = () => {
  const stats = document.getElementById('stats')
  const element = list.querySelectorAll('div')
  const checkbox = list.querySelectorAll('input[type="checkbox"]:checked')

  stats.innerHTML = `<p>Tareas pendientes: ${element.length} Completadas: ${checkbox.length}</p>`
}

const deleteTask = id => {
  const taskToDelete = document.getElementById(id)

  list.removeChild(taskToDelete)
  updateStats()
}
