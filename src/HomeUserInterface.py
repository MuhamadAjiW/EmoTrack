from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from custom import *
from os import path
import sys

class overlaySignals(QObject):
    close = pyqtSignal()

class customOverlay(QWidget):
    def __init__(self, abspath, parent=None):
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


class homeForm(UIWindow):
    def setupUi(self, Form, abspath):
        self.parent = Form
        self.abspath = abspath

        Form.setObjectName("Home")
        Form.resize(1280, 786)

        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.OpeningPanel = QFrame(Form)
        self.OpeningPanel.setStyleSheet("QPushButton {\n"
"    background: rgb(240, 240, 240);\n"
"    border: 2px solid rgb(130, 130, 130);\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(215, 215, 215);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}")
        self.OpeningPanel.setObjectName("OpeningPanel")

        self.OpeningQuotes = QLabel(self.OpeningPanel)
        self.OpeningQuotes.setGeometry(QRect(30, 128, 240, 40))

        self.NameLabel = QLabel(self.OpeningPanel)
        self.NameLabel.setGeometry(QRect(30, 64, 240, 35))
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)

        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)

        self.OpeningQuotes.setFont(font)
        self.OpeningQuotes.setObjectName("OpeningQuotes")

        self.QuitButton = QPushButton(self.OpeningPanel)
        self.QuitButton.setGeometry(QRect(30, 650, 190, 40))
        self.QuitButton.setFont(font)
        self.QuitButton.setAutoFillBackground(False)
        self.QuitButton.setStyleSheet("text-align: left;\n"
                                      "padding: 5px;\n")
        self.QuitButton.setCheckable(False)
        self.QuitButton.setChecked(False)
        self.QuitButton.setAutoDefault(False)
        self.QuitButton.setDefault(False)
        self.QuitButton.setFlat(False)
        self.QuitButton.setObjectName("QuitButton")
        self.QuitButton.text
        self.QuitButton.clicked.connect(sys.exit)

        self.MoodButton = customSVGButton(path.join(abspath, "Resource/moodIcon.svg"), path.join(abspath, "Resource/moodIconH.svg"), self.OpeningPanel)
        self.MoodButton.setGeometry(QRect(30, 600, 40, 40))
        self.MoodButton.setObjectName("MoodButton")
        self.MoodButton
        self.MoodButton.clicked.connect(lambda: self._onswitch("Mood"))

        self.JournalButton = customSVGButton(path.join(abspath, "Resource/journalIcon.svg"), path.join(abspath, "Resource/journalIconH.svg"), self.OpeningPanel)
        self.JournalButton.setGeometry(QRect(80, 600, 40, 40))
        self.JournalButton.setObjectName("JournalButton")
        self.JournalButton.clicked.connect(lambda: self._onswitch("Journal"))

        self.SleepButton = customSVGButton(path.join(abspath, "Resource/sleepIcon.svg"), path.join(abspath, "Resource/sleepIconH.svg"), self.OpeningPanel)
        self.SleepButton.setGeometry(QRect(130, 600, 40, 40))
        self.SleepButton.setObjectName("SleepButton")
        self.SleepButton.clicked.connect(lambda: self._onswitch("Sleep"))
        
        self.QuotesButton = customSVGButton(path.join(abspath, "Resource/quoteIcon.svg"), path.join(abspath, "Resource/quoteIconH.svg"), self.OpeningPanel)
        self.QuotesButton.setGeometry(QRect(180, 600, 40, 40))
        self.QuotesButton.setObjectName("QuotesButton")
        self.QuotesButton.clicked.connect(lambda: self._onswitch("Quotes"))

        self.ChangeName = customSVGButton(path.join(abspath, "Resource/nameIcon.svg"), path.join(abspath, "Resource/nameIconH.svg"), self.OpeningPanel)
        self.ChangeName.setGeometry(QRect(250, 70, 30, 30))
        self.ChangeName.setObjectName("ChangeName")
        self.ChangeName.clicked.connect(self._onpopup)

        self.horizontalLayout.addWidget(self.OpeningPanel)

        self.ImagePanel = QFrame(Form)
        self.ImagePanel.setFrameShape(QFrame.StyledPanel)
        self.ImagePanel.setLineWidth(6)
        self.ImagePanel.setObjectName("ImagePanel")
        self.OpeningImage = customSVGImage(path.join(abspath, "Resource/opening.svg"), self.ImagePanel)
        self.OpeningImage.setGeometry(QRect(1, 1, 959, 790))
        self.OpeningImage.setObjectName("OpeningImage")

        self.horizontalLayout.addWidget(self.ImagePanel)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Home"))
        self.OpeningQuotes.setText(_translate("Form", "Di dalam kesulitan pasti ada\n"
"kemudahan"))
        self.NameLabel.setText(_translate("Form", "Hai Sayang"))
        self.QuitButton.setText(_translate("Form", "Keluar"))

    def _onswitch(self, dest):
        self.signals.switch.emit(dest)

    def _onpopup(self):
        self.popup = customOverlay(self.abspath, self.parent)
        self.popup.move(0, 0)
        self.popup.resize(self.parent.width(), self.parent.height())
        self.popup.signals.close.connect(self._closepopup)
        self.popup.show()

    def _closepopup(self):
        self.popup.close()


if __name__ == "__main__":
    abspath = path.dirname(path.abspath(__file__))
    app = QApplication(sys.argv)
    
    _id = QFontDatabase.addApplicationFont(path.join(abspath, "Resource/Helvetica/Helvetica.ttf"))    

    Widget = QWidget()
    ui = homeForm()
    ui.setupUi(Widget, abspath)

    Widget.show()
    sys.exit(app.exec_())
