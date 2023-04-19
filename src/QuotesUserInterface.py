from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from custom import *
from os import path
from QuoteController import QuoteController
import sys

class QuoteOverlay(CustomOverlay):
    def __init__(self, codeIdx, controller, parent=None):
        super(QuoteOverlay, self).__init__(parent)
        self.controller = controller
        self.codeIdx = codeIdx
    
        self.block = QFrame(self)
        self.block.setFrameShape(QFrame.StyledPanel)
        self.block.setStyleSheet(
                                "background-color: rgb(255, 255, 255);"
                                "border-width: 2;"
                                "border-style: solid;"
                                )
        self.block.move(300, 200)
        self.block.resize(600, 300)

        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)

        self.quoteLabel = QLabel("Tambah/Edit Kutipan ", self.block)
        self.quoteLabel.setStyleSheet("border-width: 0;")
        self.quoteLabel.move(10,15)
        self.quoteLabel.setContentsMargins(5, 0, 0, 0)
        self.quoteLabel.setFont(font)
        
        self.quoteInput = QTextEdit(self.block)
        self.quoteInput.setGeometry(10,45, 580, 200)
        self.quoteInput.setContentsMargins(5, 0, 0, 0)
        self.quoteInput.setFont(font)

        if (codeIdx != 0):
            rows = self.controller.daftarQuotes
            self.quoteInput.setText(rows[codeIdx - 1].quote)

        self.deleteButton = CustomSVGButton(path.join(self.resources, "trashIcon.svg"), path.join(self.resources, "trashIconH.svg"), self.block)
        self.deleteButton.setGeometry(QRect(485, 254, 23, 23))
        self.deleteButton.setObjectName("DeleteButton")
        self.deleteButton.clicked.connect(self._ondelete)

        self.closeButton = CustomSVGButton(path.join(self.resources, "cancelIcon.svg"), path.join(self.resources, "cancelIconH.svg"), self.block)
        self.closeButton.setGeometry(QRect(525, 254, 23, 23))
        self.closeButton.setObjectName("CloseButton")
        self.closeButton.clicked.connect(self._onclose)

        self.confirmButton = CustomSVGButton(path.join(self.resources, "confirmIcon.svg"), path.join(self.resources, "confirmIconH.svg"), self.block)
        self.confirmButton.setGeometry(QRect(565, 254, 23, 23))
        self.confirmButton.setObjectName("ConfirmButton")
        self.confirmButton.clicked.connect(self._onconfirm)
    
    def _onconfirm(self):
        self.signals.confirm.emit(self.codeIdx)

    def _ondelete(self):
        self.signals.delete.emit(self.codeIdx)

class QuotesForm(UIWindow):
    def addquote(self, quote="Kutipan Kosong"):
        _translate = QCoreApplication.translate
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)

        exec("self.entry%d = QPushButton(self.content)" % self.entries)
        exec("self.entry%d.setObjectName('entry%d')" % (self.entries, self.entries))
        exec("self.list.insertWidget(1, self.entry%d)" % self.entries)

        enter = quote.find('\n')
        if enter == -1:
            if len(quote) < 100:
                exec("self.entry%d.setText(_translate('Form', '     %s'))" % (self.entries, quote.replace("'", "\\'").replace('"', '\\"')))
            else:
                exec("self.entry%d.setText(_translate('Form', '     %s'))" % (self.entries, quote.replace("'", "\\'").replace('"', '\\"')[:100] + '...'))
        else:
            if enter < 100:
                exec("self.entry%d.setText(_translate('Form', '     %s'))" % (self.entries, quote.replace("'", "\\'").replace('"', '\\"')[:enter] + '...'))
            else:
                exec("self.entry%d.setText(_translate('Form', '     %s'))" % (self.entries, quote.replace("'", "\\'").replace('"', '\\"')[:100] + '...'))

        exec("self.entry%d.clicked.connect(lambda: self._onpopup(%d))" % (self.entries, self.entries), locals())
        exec("self.entry%d.setFont(font)" % self.entries)

        self.entries += 1
        self.scrollAreaHeight = min(726, self.entries * 70)
        self.scrollArea.setGeometry(QRect(30, 30, 890, self.scrollAreaHeight))

    def setupUi(self, Form):
        self.controller = QuoteController()

        self.parent = Form
        self.entries = 1

        Form.setObjectName("FormQuote")
        Form.resize(1280, 786)

        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.OpeningPanel = QFrame(Form)
        self.OpeningPanel.setObjectName("OpeningPanel")
        self.OpeningPanel.setStyleSheet(
"QFrame#OpeningPanel {\n"
"    background: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    border-radius: 0px;\n"
"}"
"QPushButton {\n"
"    background: rgb(255, 255, 255);\n"
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
        

        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        
        self.QuoteTitle = QLabel(self.OpeningPanel)
        self.QuoteTitle.setGeometry(QRect(30, 64, 240, 35))
        self.QuoteTitle.setFont(font)
        self.QuoteTitle.setObjectName("QuoteTitle")
        self.QuoteTitle.setAlignment(Qt.AlignLeft|Qt.AlignTop)

        font.setPointSize(13)

        self.QuoteSubtitle = QLabel(self.OpeningPanel)
        self.QuoteSubtitle.setGeometry(QRect(30, 128, 240, 40))
        self.QuoteSubtitle.setFont(font)
        self.QuoteSubtitle.setWordWrap(True)
        self.QuoteSubtitle.setObjectName("QuoteSubtitle")
        self.QuoteSubtitle.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        
        self.ReturnButton = QPushButton(self.OpeningPanel)
        self.ReturnButton.setGeometry(QRect(30, 650, 190, 40))
        self.ReturnButton.setFont(font)
        self.ReturnButton.setAutoFillBackground(False)
        self.ReturnButton.setStyleSheet("text-align: left;\n"
                                      "padding: 5px;\n")
        self.ReturnButton.setCheckable(False)
        self.ReturnButton.setChecked(False)
        self.ReturnButton.setAutoDefault(False)
        self.ReturnButton.setDefault(False)
        self.ReturnButton.setFlat(False)
        self.ReturnButton.setObjectName("ReturnButton")
        self.ReturnButton.clicked.connect(lambda: self._onswitch("Home"))
        
        self.content = QFrame()
        self.content.setContentsMargins(40, 64, 20, -1)
        self.content.setObjectName("content")
        self.content.setStyleSheet(
"QFrame#content {\n"
"    background: rgb(200, 200, 200);\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    border-radius: 0px;\n"
"}\n"
"QPushButton {\n"
"    background: rgb(255, 255, 255);\n"
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
        
        self.scrollArea = QScrollArea(self.content)
        self.scrollAreaHeight = 70
        self.scrollArea.setGeometry(QRect(30, 30, 890, self.scrollAreaHeight))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet(
"QWidget {\n"
"    background: rgb(200, 200, 200);\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    background: rgb(255, 255, 255);\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(130, 130, 130);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    background: rgb(255, 255, 255);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    background: rgb(255, 255, 255);\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
"}"

"QPushButton {\n"
"    background: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    padding-left: 10px;\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"    min-height: 50px;\n"
"    text-align: left;\n"
"\n"
"    margin-left: 20px;\n"
"    margin-right: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(215, 215, 215);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}\n"
"")
        self.listWrapper = QWidget()
        self.listWrapper.setGeometry(QRect(0, 0, 960, 786))
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWrapper.sizePolicy().hasHeightForWidth())

        self.listWrapper.setSizePolicy(sizePolicy)

        self.list = QVBoxLayout(self.listWrapper)
        self.list.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.list.setObjectName("list")

        self.addButton = QPushButton(self.content)
        self.addButton.setObjectName("pushButton")
        self.addButton.setFont(font)
        self.addButton.clicked.connect(lambda: self._onpopup(0))

        self.list.addWidget(self.addButton)

        self.scrollArea.setWidget(self.listWrapper)

        self.horizontalLayout.addWidget(self.OpeningPanel)
        self.horizontalLayout.addWidget(self.content)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(Form)
        self.readDB()
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.QuoteSubtitle.setText(_translate("Form", "Kata - kata bijak apa yang\ndapat menginspirasi anda"))
        self.QuoteTitle.setText(_translate("Form", "Kutipan"))
        self.ReturnButton.setText(_translate("Form", "Kembali"))
        self.addButton.setText(_translate("Form", "     +          Tambah Kutipan Baru"))
        
    def _onswitch(self, dest):
        self.signals.switch.emit(dest)

    def _onpopup(self, codeIdx):
        self.popup = QuoteOverlay(codeIdx, self.controller, self.parent)
        self.popup.move(0, 0)
        self.popup.resize(self.parent.width(), self.parent.height())
        self.popup.signals.close.connect(self._closepopup)
        self.popup.signals.confirm.connect(self._onconfirm)
        self.popup.signals.delete.connect(self._ondelete)
        self.popup.codeIdx = codeIdx
        self.popup.show()

    def _closepopup(self):
        self.popup.close()

    def _onconfirm(self, codeIdx):
        if(codeIdx == 0):
            self.controller.addQuote(self.popup.quoteInput.toPlainText())
            for i in range(1, self.entries):
                exec("self.entry%d.deleteLater()" % i)
            
            self.readDB()

            self.scrollAreaHeight = min(726, self.entries * 70)
            self.scrollArea.setGeometry(QRect(30, 30, 890, self.scrollAreaHeight))

        else:
            if self.controller.daftarQuotes[codeIdx-1].builtin == True:
                msg = QMessageBox()
                msg.setWindowTitle("Terjadi kesalahan!")
                msg.setText(str("Quotes ini tidak dapat diubah karena merupakan bawaan aplikasi"))
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
            else:
                self.controller.editQuote(codeIdx-1, self.popup.quoteInput.toPlainText())

                _translate = QCoreApplication.translate
                quote = self.popup.quoteInput.toPlainText()
                enter = quote.find('\n')
                if enter == -1:
                    if len(quote) < 100:
                        exec("self.entry%d.setText(_translate('Form', '     %s'))" % (self.entries, quote.replace("'", "\\'").replace('"', '\\"')))
                    else:
                        exec("self.entry%d.setText(_translate('Form', '     %s'))" % (self.entries, quote.replace("'", "\\'").replace('"', '\\"')[:100] + '...'))
                else:
                    if enter < 100:
                        exec("self.entry%d.setText(_translate('Form', '     %s'))" % (self.entries, quote.replace("'", "\\'").replace('"', '\\"')[:enter] + '...'))
                    else:
                        exec("self.entry%d.setText(_translate('Form', '     %s'))" % (self.entries, quote.replace("'", "\\'").replace('"', '\\"')[:100] + '...'))   

        self._closepopup()

    def _ondelete(self, codeIdx):
        if(codeIdx != 0 and self.controller.daftarQuotes[codeIdx-1].builtin == False ):
            self.controller.deleteQuote(codeIdx-1)

            for i in range(1, self.entries):
                exec("self.entry%d.deleteLater()" % i)
            
            self.readDB()

            self.scrollAreaHeight = min(726, self.entries * 70)
            self.scrollArea.setGeometry(QRect(30, 30, 890, self.scrollAreaHeight))
        elif self.controller.daftarQuotes[codeIdx-1].builtin == True:
            msg = QMessageBox()
            msg.setWindowTitle("Terjadi kesalahan!")
            msg.setText(str("Quotes ini tidak dapat dihapus karena merupakan bawaan aplikasi"))
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

        self._closepopup()
        

    def readDB(self):
        self.entries = 1
        for row in self.controller.daftarQuotes:
            self.addquote(row.quote)


if __name__ == "__main__":
    abspath = path.join(path.dirname(path.abspath(__file__)), '../img')
    app = QApplication(sys.argv)
    _id = QFontDatabase.addApplicationFont(path.join(abspath, "Helvetica/Helvetica.ttf"))    

    Widget = QWidget()
    ui = QuotesForm()
    ui.setupUi(Widget)

    Widget.show()
    sys.exit(app.exec_())