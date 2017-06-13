// Variables
let xhttp = new XMLHttpRequest()

// Añade las alertas al formulario de dashboard
let alertSuccess = document.querySelector('.alert-success');
if (alertSuccess != null) {
    document.querySelector('#name').value = '';
    document.querySelector('#year').value = '';
    document.querySelector('#score').value = '';
}

// Oculta las alertas pasadas un tiempo
let alerts = document.querySelectorAll('.alert');
let tiempo = 2000;
setTimeout(function() {
    for (alert of alerts)
        alert.style.display = 'none';
}, tiempo);

// Ajax para Me gusta
let addLike = function(ruta, id) {
	xhttp.open('GET', ruta, true);
	xhttp.send();
	let like = document.querySelector('#' + id);
	like.innerHTML = parseInt(like.innerHTML) + 1
}


