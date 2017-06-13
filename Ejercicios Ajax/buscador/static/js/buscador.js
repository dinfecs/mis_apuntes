// Variables
let xhttp = new XMLHttpRequest();
let busqueda = document.querySelector('#busqueda');
let resultados = document.querySelector('#resultados');

// Funciones
let obtenerPaises = function () {
    let textoBusqueda = busqueda.value;
    if(busqueda.value != '') {
        xhttp.open('GET', `/busqueda/${textoBusqueda}`, true);
        xhttp.send();
    } else {
        resultados.innerHTML = '';
    }
}

let grabar = function(pais) {
    busqueda.value = pais;
    resultados.innerHTML = '';
}

// Eventos
busqueda.addEventListener('keyup', obtenerPaises, false);

xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
        let paises = JSON.parse(this.responseText);
        let html = '';
        for(let pais of paises) {
            html += `<span onclick="grabar('${pais.nombre}')">${pais.nombre}</span><br>`
        }
        resultados.innerHTML = html;
    }
};