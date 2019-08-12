import sys
from interface import Ui_MainWindow
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(Ui_MainWindow):

    # Define a signal called "trigger"
    trigger_rename_label_database = pyqtSignal()

    def __init__(self, form):
        # This configures the interface
        self.setupUi(form)
        self.pampadamm()
    
    # Connect and emit the signal
    def trigger_rename_label_database(self):
        # Connect the trigger
        self.trigger_rename_label_database.connect(self.handle_trigger_rename_label_database)
        # Emit the signal
        self.trigger_rename_label_database.emit()

    # Associate button pressing with signal emission
    def pampadamm(self):
        self.button_database.clicked.connect(self.handle_trigger_rename_label_database)
        return None
        
    # Handle the trigger
    def handle_trigger_rename_label_database(self):
        self.label_database.setText('Hi, dude )')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())