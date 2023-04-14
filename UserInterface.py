from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from custom import *
from os import path

class overlaySignals(QObject):
    close = pyqtSignal()

class customOverlay(QWidget):
    def __init__(self, parent=None):
        super(customOverlay, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.fillColor = QColor(30, 30, 30, 120)

        self.block = QFrame(self)
        self.block.setFrameShape(QFrame.StyledPanel)
        self.block.setStyleSheet(
                                "background-color: rgb(255, 255, 255);"
                                "border-width: 2;"
                                "border-style: solid;"
                                )
        self.block.move(300, 300)
        self.block.resize(600, 120)

        self.renameLabel = QLabel("Masukkan nama pengguna: ", self.block)
        self.renameLabel.setStyleSheet("border-width: 0;")
        self.renameLabel.move(5,15)
        self.renameLabel.setContentsMargins(5, 0, 0, 0)

        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.renameLabel.setFont(font)

        self.nameInput = QLineEdit(self.block)
        self.nameInput.setGeometry(5,45, 580, 30)
        self.nameInput.setContentsMargins(5, 0, 0, 0)
        self.nameInput.setFont(font)

        self.closeButton = customSVGButton(path.join(abspath, "Resource/cancelIcon.svg"), path.join(abspath, "Resource/cancelIconH.svg"), self.block)
        self.closeButton.setGeometry(QRect(523, 84, 23, 23))
        self.closeButton.setObjectName("CloseButton")

        self.confirmButton = customSVGButton(path.join(abspath, "Resource/confirmIcon.svg"), path.join(abspath, "Resource/confirmIconH.svg"), self.block)
        self.confirmButton.setGeometry(QRect(563, 84, 23, 23))
        self.confirmButton.setObjectName("ConfirmButton")

        self.closeButton.clicked.connect(self._onclose)
        #TODO: self.confirmButton.clicked.connect(self._onclose)

        self.signals = overlaySignals()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(self.fillColor)
        qp.drawRect(0, 0, self.width(), self.height())
        qp.end()

    def _onclose(self):
        self.signals.close.emit()


class Ui_HomeWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_HomeWindow, self).__init__(parent)

    def setupUi(self, HomeWindow, abspath):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.setEnabled(True)
        HomeWindow.resize(1280, 786)
        HomeWindow.setMinimumSize(QSize(1280, 786))
        HomeWindow.setMaximumSize(QSize(1280, 786))

        self.centralwidget = QFrame(HomeWindow)
        self.centralwidget.setMinimumSize(QSize(1280, 786))
        self.centralwidget.setMaximumSize(QSize(1280, 786))
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QRect(-1, 0, 1281, 791))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.OpeningPanel = QFrame(self.horizontalLayoutWidget)
        self.OpeningPanel.setStyleSheet('background-color: rgb(255,255,255)')
        self.OpeningPanel.setFrameShape(QFrame.StyledPanel)
        self.OpeningPanel.setLineWidth(6)
        self.OpeningPanel.setObjectName("OpeningPanel")

        self.OpeningQuotes = QLabel(self.OpeningPanel)
        self.OpeningQuotes.setGeometry(QRect(30, 128, 240, 40))

        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)

        self.OpeningQuotes.setFont(font)
        self.OpeningQuotes.setObjectName("OpeningQuotes")

        self.NameLabel = QLabel(self.OpeningPanel)
        self.NameLabel.setGeometry(QRect(30, 64, 240, 35))

        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)

        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")

        self.QuitButton = customTextButton("Keluar", self.OpeningPanel)
        self.QuitButton.setGeometry(QRect(30, 650, 190, 40))
        self.QuitButton.setObjectName("QuitButton")
        self.QuitButton.clicked.connect(sys.exit)

        self.MoodButton = customSVGButton(path.join(abspath, "Resource/moodIcon.svg"), path.join(abspath, "Resource/moodIconH.svg"), self.OpeningPanel)
        self.MoodButton.setGeometry(QRect(30, 590, 40, 40))
        self.MoodButton.setObjectName("MoodButton")
        #TODO: self.MoodButton.clicked.connect()

        self.JournalButton = customSVGButton(path.join(abspath, "Resource/journalIcon.svg"), path.join(abspath, "Resource/journalIconH.svg"), self.OpeningPanel)
        self.JournalButton.setGeometry(QRect(80, 590, 40, 40))
        self.JournalButton.setObjectName("JournalButton")
        #TODO: self.MoodButton.clicked.connect()

        self.SleepButton = customSVGButton(path.join(abspath, "Resource/sleepIcon.svg"), path.join(abspath, "Resource/sleepIconH.svg"), self.OpeningPanel)
        self.SleepButton.setGeometry(QRect(130, 590, 40, 40))
        self.SleepButton.setObjectName("SleepButton")
        #TODO: self.SleepButton.clicked.connect()
        
        self.QuotesButton = customSVGButton(path.join(abspath, "Resource/quoteIcon.svg"), path.join(abspath, "Resource/quoteIconH.svg"), self.OpeningPanel)
        self.QuotesButton.setGeometry(QRect(180, 590, 40, 40))
        self.QuotesButton.setObjectName("QuotesButton")
        #TODO: self.QuotesButton.clicked.connect()

        self.ChangeName = customSVGButton(path.join(abspath, "Resource/nameIcon.svg"), path.join(abspath, "Resource/nameIconH.svg"), self.OpeningPanel)
        self.ChangeName.setGeometry(QRect(250, 70, 30, 30))
        self.ChangeName.setObjectName("ChangeName")
        self.ChangeName.clicked.connect(self._onpopup)

        self.horizontalLayout.addWidget(self.OpeningPanel)

        self.ImagePanel = QFrame(self.horizontalLayoutWidget)
        self.ImagePanel.setFrameShape(QFrame.StyledPanel)
        self.ImagePanel.setLineWidth(6)
        self.ImagePanel.setObjectName("ImagePanel")
        self.OpeningImage = customImage(QPixmap(path.join(abspath, "Resource/opening.png")), self.ImagePanel)
        self.OpeningImage.setGeometry(QRect(1, 1, 959, 790))
        self.OpeningImage.setObjectName("OpeningImage")

        self.horizontalLayout.addWidget(self.ImagePanel)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        HomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeWindow)
        QMetaObject.connectSlotsByName(HomeWindow)


    def retranslateUi(self, HomeWindow):
        _translate = QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "Home"))
        self.OpeningQuotes.setText(_translate("HomeWindow", "Di dalam kesulitan pasti ada\n"
"kemudahan"))
        self.NameLabel.setText(_translate("HomeWindow", "Hai Sayang"))


    def _onpopup(self):
        self.popup = customOverlay(self.centralwidget)
        self.popup.move(0, 0)
        self.popup.resize(1280, 786)
        self.popup.signals.close.connect(self._closepopup)
        self.popup.show()

    def _closepopup(self):
        self.popup.close()


if __name__ == "__main__":
    import sys
    abspath = path.dirname(path.abspath(__file__))
    app = QApplication(sys.argv)
    
    _id = QFontDatabase.addApplicationFont(path.join(abspath, "Resource/Helvetica/Helvetica.ttf"))    

    HomeWindow = QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow, abspath)

    HomeWindow.show()
    sys.exit(app.exec_())
