var botonActivado = false;

document.addEventListener('DOMContentLoaded',function(){
    document.getElementById('botonInicio').addEventListener('click',function(){
        window.location.href='/';
    })
})

function activarBoton(botonSeleccionado) {
    // Desactivar ambos botones
    document.getElementById('botonIngreso').classList.remove('activado');
    document.getElementById('botonGasto').classList.remove('activado');

    // Activar el botón seleccionado
    document.getElementById(`boton${botonSeleccionado}`).classList.add('activado');

    // Actualizar la acción del formulario
    var formulario = document.getElementById('formularioMovimiento');
    formulario.action = `/submit_${botonSeleccionado}`;

    botonActivado = true;
}

function validarFormulario(event) {
    if (!botonActivado) {
        alert("Debes seleccionar un tipo de movimiento (Ingreso/Gasto) antes de enviar el formulario.");
        event.preventDefault(); // Evitar el envío del formulario
    }
}