
from PyQt5 import QtWidgets
from interfaz import Ui_Dialog  # importa tu archivo generado desde test.ui

class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Crear QLineEdit manualmente si no estaba en el .ui
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(130, 180, 161, 31)
        self.lineEdit.setPlaceholderText("Ingrese su nombre")

        # Conectar botón
        self.ui.pushButton.clicked.connect(self.set_nombre)

    def set_nombre(self):
        nombre = self.lineEdit.text()
        self.ui.label.setText(f"Mi nombre es: {nombre}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = MyApp()
    ventana.show()
    sys.exit(app.exec_())