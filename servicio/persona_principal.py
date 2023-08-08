from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow

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

        correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        validator = QRegularExpressionValidator(correo_exp, self)
        self.ui.txt_email.setValidator(validator)

    def grabar(self):
        tipo_persona = self.ui.cb_tipo_persona.currentText()
        if self.ui.txt_nombre.text() == '' or self.ui.txt_apellido.text() == ''\
            or len (self.ui.txt_cedula.text()) < 10 or self.ui.txt_email.text() == '':
            print(' Completar datos')
        else:
         persona = None
         if tipo_persona == 'Docente':
            persona = Docente()
            persona.nombre = self.ui.txt_nombre.text()
            persona.apellido = self.ui.txt_apellido.text()
            persona.cedula = self.ui.txt_cedula.text()
            persona.email = self.ui.txt_email.text()
         else:
            persona = Estudiante()
            persona.nombre = self.ui.txt_nombre.text()
            persona.apellido = self.ui.txt_apellido.text()
            persona.cedula = self.ui.txt_cedula.text()
            persona.email = self.ui.txt_email.text()
            #try:
            #EstudianteDao.insertar_estudiante(persona)
            #except Exception as e:




                #insertar
        #archivo = None
        #try:
         #   archivo = open('../servicio/archivo.txt', mode='a')
          #  archivo.write(persona.__str__())
           # archivo.write('\n')
        #except Exception as e:
            #print('No se pudo grabar.')
        #finally:
         #   if archivo:
          #      archivo.close()
        #if respuesta['exito']:
        self.ui.txt_nombre.setText('')
        self.ui.txt_apellido.setText('')
        self.ui.txt_cedula.setText('')
        self.ui.txt_email.setText('')
        self.ui.stb_estado.showMessage('Grabado con éxito.', 2000)
        #else:
        	#QmessageBox.critical(self,'Error',respuesta['mensaje'])
    def consultar(self):
        consulta_cedula = self.ui.txt_consulta_cedula.text()
        self._persona = PersonaPrincipal()
        self._persona = PersonaPrincipal(cedula=consulta_cedula)
        tupla_persona = EstudianteDao.seleccionar_persona_por_cedula(self._persona)
        self._persona.id = tupla_persona[0]
        self._persona.nombre = tupla_persona[1]
        self._persona.apellido = tupla_persona[2]
        self._persona.cedula = tupla_persona[3]
        self._persona.email = tupla_persona[4]
        self.llenar_formulario()
        print(self._persona)
