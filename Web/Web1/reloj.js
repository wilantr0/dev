let mostrarFecha = document.getElementById('fecha');
let mostrarReloj = document.getElementById('reloj');

let fecha = new Date();

let diasSemana = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'];

let mesesAño = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

let fechaSemana = diasSemana[fecha.getDay()];
let fechaDia = fecha.getDate();
let fechaMes = mesesAño[fecha.getMonth()];
let fechaAño = fecha.getFullYear();

mostrarFecha.innerHTML = `${fechaSemana}, ${fechaDia} de ${fechaMes} de ${fechaAño}`;

setInterval(()=>{
    let hora = new Date;
    mostrarReloj.innerHTML = hora.toLocaleTimeString();
}, 1000)



