from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from custom import *
from HomeUserInterface import *
from JurnalUserInterface import *
from MoodUserInterface import *
from QuotesUserInterface import *
from SleepUserInterface import *
from os import path

class UserInterface(QMainWindow):
    def __init__(self, startView: UIWindow, views: dict, parent=None):
        super(UserInterface, self).__init__(parent)
        self.setObjectName("UI Controller")
        self.resize(1280, 786)

        self.displays = views
        self.view = QFrame(self)
        self.currentUI = startView

        for display in self.displays.values():
            display.signals.switch.connect(self.switchWindow)

        startView.setupUi(self.view)
        self.setCentralWidget(self.view)

    def switchWindow(self, code):
        window = self.displays[code]
        del self.view
        self.view = QFrame(self)
        window.setupUi(self.view)
        self.currentUI = self.view
        self.setCentralWidget(self.view)

if __name__ == "__main__":
    abspath = path.dirname(path.abspath(__file__))
    app = QApplication(sys.argv)
    
    _id = QFontDatabase.addApplicationFont(path.join(abspath, "Resource/Helvetica/Helvetica.ttf"))    
    
    HomeUi = HomeForm()
    MoodUi = MoodForm()
    JournalUi = JurnalForm()
    SleepUi = SleepForm()
    QuotesUi = QuotesForm()
    UiDict ={
        "Home": HomeUi,
        "Mood": MoodUi,
        "Journal": JournalUi,
        "Sleep": SleepUi,
        "Quotes": QuotesUi,
    }
    mainWindow = UserInterface(HomeUi, UiDict)

    mainWindow.show()
    sys.exit(app.exec_())

