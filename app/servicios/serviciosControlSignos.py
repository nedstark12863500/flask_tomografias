from app.configuraciones.extensiones import db
from app.modelos.controlSignos import ControlSignos
from app.serializadores.serializadorControlSignos import SerializadorControlSignos

class ServiciosControlSignos():
    def obtener_todos():
        controles_signos = ControlSignos.query.all()
        respuesta = SerializadorControlSignos.serializar(controles_signos)
        if respuesta:
            return respuesta
        else:
            return None
    
    def obtener_id(id):
        control_signo = ControlSignos.query.get(id)
        respuesta = SerializadorControlSignos.serializar_unico(control_signo)
        if respuesta:
            return respuesta
        else:
            return None
    
    def obtener_hoja(id_hoja):
        control_signo = ControlSignos.query.filter_by(id_hoja_signos=id_hoja)
        respuesta = SerializadorControlSignos.serializar(control_signo)
        if respuesta:
            return respuesta
        else:
            return None
    
    def crear(fecha, hora, presion_sistolica, presion_diastolica, respiracion, saturacion, diuresis, catarsis, hoja_control):
        nuevo_control = ControlSignos(fecha, hora, presion_sistolica, presion_diastolica, respiracion, saturacion, diuresis, catarsis, hoja_control)
        db.session.add(nuevo_control)
        db.session.commit()
        respuesta = SerializadorControlSignos.serializar_unico(nuevo_control)
        if respuesta:
            return respuesta
        else:
            return None
    
    def actualizar(id, fecha=None, hora=None, presion_sistolica=None, presion_diastolica=None, respiracion=None, saturacion=None, diuresis=None, catarsis=None, hoja_control=None):
        print("ingreso a los servicios de actualizacion del control de signos")

        editar_control = ControlSignos.query.get(id)
        print(editar_control)
        if editar_control:
            if fecha:
                editar_control.fecha_control = fecha
            if hora:
                editar_control.hora_control = hora
            if presion_sistolica:
                editar_control.presion_sistolica_control = presion_sistolica
            if presion_diastolica:
                editar_control.presion_diastolica_control = presion_diastolica
            if respiracion:
                editar_control.respiracion_control = respiracion
            if saturacion:
                editar_control.saturacion_control = saturacion
            if diuresis:
                editar_control.diuresis_control = diuresis
            if catarsis:
                editar_control.catarsis_control = catarsis
            if hoja_control:
                editar_control.id_hoja_signos = hoja_control
            db.session.commit()
            respuesta = SerializadorControlSignos.serializar_unico(editar_control)
            if respuesta:
                return respuesta
            else:
                return None
        else:
            return None
