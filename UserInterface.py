from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from custom import *
from HomeUserInterface import *
from JurnalUserInterface import *
from os import path

class UserInterface(QMainWindow):
    def __init__(self, abspath, startView: UIWindow, views: dict, parent=None):
        super(UserInterface, self).__init__(parent)
        self.setObjectName("UI Controller")
        self.resize(1280, 786)

        self.displays = views
        self.abspath = abspath
        self.view = QFrame(self)
        self.currentUI = startView

        startView.signals.switch.connect(self.test)
        startView.setupUi(self.view, self.abspath)
        self.setCentralWidget(self.view)

    def switchWindow(self, window: UIWindow):
        del self.view
        self.view = QFrame(self)
        window.setupUi(self.view, self.abspath)
        self.currentUI = self.view
        self.setCentralWidget(self.view)

    def test(self, code):
        print(code)
        self.switchWindow(self.displays[code])

if __name__ == "__main__":
    abspath = path.dirname(path.abspath(__file__))
    app = QApplication(sys.argv)
    
    _id = QFontDatabase.addApplicationFont(path.join(abspath, "Resource/Helvetica/Helvetica.ttf"))    
    
    HomeUi = homeForm()
    MoodUi = Ui_Form()
    JournalUi = Ui_Form()
    SleepUi = Ui_Form()
    QuotesUi = Ui_Form()
    UiDict ={
        "Home": HomeUi,
        "Mood": JournalUi,
        "Journal": JournalUi,
        "Sleep": JournalUi,
        "Quotes": JournalUi,
    }
    mainWindow = UserInterface(abspath, HomeUi, UiDict)

    mainWindow.show()
    sys.exit(app.exec_())

