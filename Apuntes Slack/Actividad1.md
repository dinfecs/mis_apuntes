Realiza una página, con comprobaciones en Javascript, donde un usuario se pueda identificar. Para entrar se necesitará indicar el DNI en dos campos diferentes, uno para los números y otro la letra. Además se tendrá que pedir la contraseña por duplicado, (para verificar que el usuario no se ha equivocado).
En caso de existir algún error, informa al usuario con un alert().
Todas las comprobaciones se tendrán que hacer antes de enviarlo.

Estructura:

DNI_numero
DNI_letra
Contraseña
Vuelve_A_introducir_contraseña

Enviar


Pro: Cambia el color de campo a rojo cuando se equivoque. Pista!! document.getElementById.classList.add("rojo")