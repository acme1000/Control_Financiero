document.addEventListener('DOMContentLoaded',function(){
    document.getElementById('botonInicio').addEventListener('click',function(){
        window.location.href='/';
    })
})

document.querySelectorAll('.botonEditar').forEach(function(boton) {
    boton.addEventListener('click', function() {
        var idMovimiento = boton.getAttribute('data-id');
        window.location.href = '/editar/' + idMovimiento;
    });
});