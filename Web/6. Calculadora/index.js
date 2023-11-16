const display = document.getElementById('display')
const buttons = document.querySelectorAll('button')

buttons.forEach(item => {
  item.onclick = () => {
    if (item.id == 'clear') {
      display.innerText = ''
    } else if (item.id == 'back') {
      let string = display.innerText.toString()
      display.innerText = string.substring(0, string.length - 1)
    } else if (display.innerText != '' && item.id == 'equal') {
      display.innerText = eval(display.innerText)
    } else if (display.innerText == '' && item.id == 'equal') {
      display.innerText = null
      setTimeout(() => (display.innerText = ''), 20)
    } else {
      display.innerText += item.id
    }
  }
})

const themeToggleBtn = document.querySelector('.theme-toggler')
const calculator = document.querySelector('.calculator')
const toggleIcon = document.querySelector('.toggler-icon')
let isDark = true
themeToggleBtn.onclick = () => {
  calculator.classList.toggle('dark')
  themeToggleBtn.classList.toggle('active')
}
