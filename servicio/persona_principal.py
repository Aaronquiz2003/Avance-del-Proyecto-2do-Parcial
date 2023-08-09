
from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from Datos.estudiante_dao import EstudianteDao
from UI.vtn_principal import Ui_vtn_principal
from dominio.docente import Docente
from dominio.estudiante import Estudiante

class PersonaPrincipal(QMainWindow):
    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('Bienvenido', 2000)
        self.ui.vtn_grabar.clicked.connect(self.grabar)
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())
        self.ui.btn_buscar_cedula.clicked.connect(self.buscar_x_cedula)
        #self.ui.btn_estatura.clicked.connect(self.calculos_estatura)

        correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        validator = QRegularExpressionValidator(correo_exp, self)
        self.ui.txt_email.setValidator(validator)


    def grabar(self):
        tipo_persona = self.ui.cb_tipo_persona.currentText()
        if self.ui.txt_nombre.text() == '' or self.ui.txt_apellido.text() == ''\
            or len(self.ui.txt_cedula.text()) < 10 or self.ui.txt_email.text() == '':
            QMessageBox.critical(self, 'Error', 'Por favor, complete todos los campos.')
        else:
            persona = None
            if tipo_persona == 'Docente':
                persona = Docente()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()
                persona.carrera = self.ui.txt_carrera.text()
                respuesta = None
                respuesta = EstudianteDao.insertar_estudiante(persona)
                persona.estatura = self.ui.sp_estatura.text()
            else:
                persona = Estudiante()

            persona.nombre = self.ui.txt_nombre.text()
            persona.apellido = self.ui.txt_apellido.text()
            persona.cedula = self.ui.txt_cedula.text()
            persona.email = self.ui.txt_email.text()
            persona.carrera = self.ui.txt_carrera.text()
            #persona.estatura= self.ui.txt
            respuesta=None
            respuesta= EstudianteDao.insertar_estudiante(persona)
           # persona.estatura = self.ui.sp_estatura.text()
            try:
                EstudianteDao.insertar_estudiante(persona)  # Asumiendo que EstudianteDao.insertar_estudiante está definido en tu código.
                self.ui.txt_nombre.setText('')
                self.ui.txt_apellido.setText('')
                self.ui.txt_cedula.setText('')
                self.ui.txt_email.setText('')
                self.ui.txt_carrera.setText('')
                # persona.estatura = self.ui.sp_estatura.text()
                self.ui.stb_estado.showMessage('Grabado con éxito.', 2000)
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'No se pudo grabar: {str(e)}')

    def buscar_x_cedula(self):
        cedula = self.ui.txt_cedula.text()
        e = Estudiante(cedula=cedula)
        e = EstudianteDao.seleccionar_por_cedula(e)
        print(e)
        self.ui.txt_nombre.setText(e.nombre)
        self.ui.txt_apellido.setText(e.apellido)
        self.ui.txt_email.setText(e.email)
        self.ui.txt_carrera.setText(e.carrera)
        self.ui.cb_tipo_persona.setCurrentText('Estudiante')


