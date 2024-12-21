from app.configuraciones.extensiones import db

class RegistroEnfermeria(db.Model):
    __tablename__ = 'registro_enfermeria'

    id_registro_enfermeria = db.Column(db.Integer, primary_key=True)
    procedimiento_enfermeria = db.Column(db.String(200), nullable=True)
    observaciones_enfermeria = db.Column(db.Text, nullable=True)
    fecha_registro = db.Column(db.Date, nullable=True)
    hora_registro = db.Column(db.Time, nullable=True)
    id_enfermera_cargo = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_consulta_registro = db.Column(db.Integer, db.ForeignKey('consultas.id_consulta'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id_paciente'), nullable=False)

    def __init__(self, procedimiento, observaciones, fecha, hora, enfermera, consulta, paciente):
        self.procedimiento_enfermeria = procedimiento
        self.observaciones_enfermeria = observaciones
        self.fecha_registro = fecha
        self.hora_registro = hora
        self.id_enfermera_cargo = enfermera
        self.id_consulta_registro = consulta
        self.id_paciente = paciente

