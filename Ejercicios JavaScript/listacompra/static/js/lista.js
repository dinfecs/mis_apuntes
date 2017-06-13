let obj = [];
let add = function() {
  let campo_producto = document.querySelector('#producto');
  let campo_cantidad = document.querySelector('#cantidad');
  let todos_productos = document.querySelector('#todos_productos');
  let checked_evaluacion;
  obj.push({producto: campo_producto.value, cantidad: campo_cantidad.value});
  let html = '';
  for(cosas of obj) {
    html += '<tr><th>' + cosas.producto + '</td><br><th>' + cosas.cantidad + '</th></tr>';
  }
  todos_productos.innerHTML = html;
}