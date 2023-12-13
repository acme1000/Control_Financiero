from flask import Blueprint, render_template
from flask import request
from .models import db, Movimiento
from datetime import datetime, timedelta

main = Blueprint('main',__name__)


# RUTA MENU PRINCIPAL ====================
@main.route('/') 
def index():
    return render_template('index.html')


# RUTAS PARA AÑADIR MOVIMIENTO ====================
@main.route('/anadir')
def anadir():
    return render_template('anadir.html')

@main.route('/submit_Ingreso', methods=['POST'])
def submit_Ingreso():
    tipo = 'Ingreso'
    nombre = request.form.get('nombre')
    monto = float(request.form.get('monto'))
    descr = request.form.get('descr')
    fecha_str = request.form.get('fecha')
    fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()  # Convierte la cadena de fecha a un objeto de fecha
    nuevo_mov = Movimiento(tipo=tipo,
                           nombre=nombre,
                           monto=monto,
                           fecha=fecha,
                           descr=descr)
    db.session.add(nuevo_mov)
    db.session.commit()

    return render_template('exito.html')

@main.route('/submit_Gasto', methods=['POST'])
def submit_Gasto():
    tipo = 'Gasto'
    nombre = request.form.get('nombre')
    monto = float(request.form.get('monto'))
    if monto > 0: 
        monto *= -1
    descr = request.form.get('descr')
    fecha_str = request.form.get('fecha')
    fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()  # Convierte la cadena de fecha a un objeto de fecha
    nuevo_mov = Movimiento(tipo=tipo,
                           nombre=nombre,
                           monto=monto,
                           fecha=fecha,
                           descr=descr)
    db.session.add(nuevo_mov)
    db.session.commit()

    return render_template('exito.html')


# RUTA PARA VER MOVIMIENTOS ====================
@main.route('/ver_movimientos')
def ver_movimientos():
    #movimientos = Movimiento.query.all()
    # Ordena los movimientos por fecha, de más reciente a más antiguo
    movimientos = Movimiento.query.order_by(Movimiento.fecha.desc()).all()

    return render_template('ver_movimientos.html', movimientos=movimientos)


# RUTAS PARA EDITAR Y ELIMINAR ====================
@main.route('/editar')
def editar():
    movimientos = Movimiento.query.all()
    return render_template('editar.html', movimientos=movimientos)

@main.route('/editar/<int:id_movimiento>')
def editar_movimiento(id_movimiento):
    movimiento = Movimiento.query.get_or_404(id_movimiento)
    return render_template('editar_movimiento.html', movimiento=movimiento)

@main.route('/actualizar_movimiento/<int:id_movimiento>', methods=['POST'])
def actualizar_movimiento(id_movimiento):
    movimiento = Movimiento.query.get_or_404(id_movimiento)
    movimiento.nombre = request.form['nombre']
    movimiento.monto = float(request.form['monto'])
    movimiento.descr = request.form['descr']
    fecha_str = request.form['fecha']
    movimiento.fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
    
    db.session.commit()
    return render_template('exito.html')

@main.route('/eliminar_movimiento/<int:id_movimiento>', methods=['POST'])
def eliminar_movimiento(id_movimiento):
    movimiento = Movimiento.query.get_or_404(id_movimiento)
    db.session.delete(movimiento)
    db.session.commit()
    return render_template('exito.html')


# RUTAS PARA BALANCE ====================
@main.route('/balance')
def balance():
    total = round(db.session.query(db.func.sum(Movimiento.monto)).scalar(), 2)

    return render_template('balance.html', total=total)

# RUTA PARA PRÓXIMAMENTE ====================
@main.route('/soon')
def soon():
    return render_template('soon.html')
