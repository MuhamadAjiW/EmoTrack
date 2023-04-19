from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MoodController import MoodController
from custom import *
from os import path
import sys

import datetime

class MoodForm(UIWindow):
    def setupUi(self, Form):
        self.controller = MoodController()

        Form.setObjectName("Mood Menu")
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
        
        self.MoodTitle = QLabel(self.OpeningPanel)
        self.MoodTitle.setGeometry(QRect(30, 64, 240, 35))
        self.MoodSubtitle = QLabel(self.OpeningPanel)
        self.MoodSubtitle.setGeometry(QRect(30, 128, 240, 40))

        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)

        self.MoodTitle.setFont(font)
        self.MoodTitle.setObjectName("MoodTitle")
        self.MoodTitle.setAlignment(Qt.AlignLeft|Qt.AlignTop)

        font.setPointSize(13)

        self.MoodSubtitle.setFont(font)
        self.MoodSubtitle.setWordWrap(True)
        self.MoodSubtitle.setObjectName("MoodSubtitle")
        self.MoodSubtitle.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        
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

        font.setPointSize(10)
        font.setBold(True)
        self.button1 = QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":)"), font=font)
        self.button1.setGeometry(QRect(30, 230, 41, 41))
        self.button1.setObjectName("button1")
        self.button6 = QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":3"), font=font)
        self.button6.setGeometry(QRect(90, 290, 41, 41))
        self.button6.setObjectName("button6")
        self.button4 = QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":v"), font=font)
        self.button4.setGeometry(QRect(210, 230, 41, 41))
        self.button4.setObjectName("button4")
        self.button5 = QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":D"), font=font)
        self.button5.setGeometry(QRect(30, 290, 41, 41))
        self.button5.setObjectName("button5")
        self.button2 = QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":("), font=font)
        self.button2.setGeometry(QRect(90, 230, 41, 41))
        self.button2.setObjectName("button2")
        self.button3 = QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":O"), font=font)
        self.button3.setGeometry(QRect(150, 230, 41, 41))
        self.button3.setObjectName("button3")
        self.button7 = QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":|"), font=font)
        self.button7.setGeometry(QRect(150, 290, 41, 41))
        self.button7.setObjectName("button7")
        self.button8 = QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":\\"), font=font)
        self.button8.setGeometry(QRect(210, 290, 41, 41))
        self.button8.setObjectName("button8")



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
        self.currentFrameDown = QFrame(self.content)
        self.currentFrameDown.setGeometry(QRect(780, 10, 121, 121))
        self.currentFrameDown.setFont(font)
        self.currentFrameDown.setFrameShape(QFrame.Box)
        self.currentFrameDown.setFrameShadow(QFrame.Raised)
        self.currentFrameDown.setObjectName("frame")
        self.currentFrameDown.setStyleSheet(
            "QFrame#frame {\n"
            "    background: rgb(255, 255, 255);\n"
            "    border: 1px solid rgb(130, 130, 130);\n"
            "    border-radius: 0px;\n"
            "}\n"
        )

        self.currentFrameTop = QFrame(self.currentFrameDown)
        self.currentFrameTop.setGeometry(QRect(-40, 0, 191, 31))
        self.currentFrameTop.setFrameShape(QFrame.Box)
        self.currentFrameTop.setFrameShadow(QFrame.Raised)
        self.currentFrameTop.setObjectName("frame_2")

        font.setPointSize(10)
        font.setBold(True)

        self.labelTanggal = QLabel(self.currentFrameTop)
        self.labelTanggal.move(70, 10)
        self.labelTanggal.setFont(font)
        self.labelTanggal.setAlignment(Qt.AlignCenter)
        self.labelTanggal.setObjectName("label_tanggal")
        

        self.labelMoodSekarang = QLabel(self.currentFrameDown)
        self.labelMoodSekarang.setGeometry(QRect(0, 30, 121, 91))

        font.setPointSize(22)
        font.setBold(False)

        self.labelMoodSekarang.setFont(font)
        self.labelMoodSekarang.setAlignment(Qt.AlignCenter)
        self.labelMoodSekarang.setObjectName("label_mood_sekarang")



        font.setPointSize(14)

        self.labelFrekuensi = QLabel(self.content)
        self.labelFrekuensi.setGeometry(QRect(60, 90, 671, 41))
        self.labelFrekuensi.setFont(font)
        self.labelFrekuensi.setObjectName("label_frekuensi")
        
        self.label_mood_1 = QLabel(self.content)
        self.label_mood_1.setGeometry(QRect(60, 150, 41, 41))
        self.label_mood_1.setFrameShape(QFrame.Box)
        self.label_mood_1.setAlignment(Qt.AlignCenter)
        self.label_mood_1.setObjectName("label_mood_1")
        self.label_mood_1.setStyleSheet(
            "background: rgb(255, 255, 255);\n"
        )
        self.progress_bar_1 = QProgressBar(self.content)
        self.progress_bar_1.setGeometry(QRect(120, 150, 601, 41))
        self.progress_bar_1.setProperty("value", 0)
        self.progress_bar_1.setObjectName("progress_bar_1")
        self.label_mood_2 = QLabel(self.content)
        self.label_mood_2.setGeometry(QRect(60, 210, 41, 41))
        self.label_mood_2.setFrameShape(QFrame.Box)
        self.label_mood_2.setAlignment(Qt.AlignCenter)
        self.label_mood_2.setObjectName("label_mood_2")
        self.label_mood_2.setStyleSheet(
            "background: rgb(255, 255, 255);\n"
        )
        self.progress_bar_2 = QProgressBar(self.content)
        self.progress_bar_2.setGeometry(QRect(120, 210, 601, 41))
        self.progress_bar_2.setProperty("value", 0)
        self.progress_bar_2.setObjectName("progress_bar_2")
        self.label_mood_3 = QLabel(self.content)
        self.label_mood_3.setGeometry(QRect(60, 270, 41, 41))
        self.label_mood_3.setFrameShape(QFrame.Box)
        self.label_mood_3.setAlignment(Qt.AlignCenter)
        self.label_mood_3.setObjectName("label_mood_3")
        self.label_mood_3.setStyleSheet(
            "background: rgb(255, 255, 255);\n"
        )
        self.progress_bar_3 = QProgressBar(self.content)
        self.progress_bar_3.setGeometry(QRect(120, 270, 601, 41))
        self.progress_bar_3.setProperty("value", 0)
        self.progress_bar_3.setObjectName("progress_bar_3")
        self.label_mood_4 = QLabel(self.content)
        self.label_mood_4.setGeometry(QRect(60, 330, 41, 41))
        self.label_mood_4.setFrameShape(QFrame.Box)
        self.label_mood_4.setAlignment(Qt.AlignCenter)
        self.label_mood_4.setObjectName("label_mood_4")
        self.label_mood_4.setStyleSheet(
            "background: rgb(255, 255, 255);\n"
        )
        self.progress_bar_4 = QProgressBar(self.content)
        self.progress_bar_4.setGeometry(QRect(120, 330, 601, 41))
        self.progress_bar_4.setProperty("value", 0)
        self.progress_bar_4.setObjectName("progress_bar_4")
        self.label_mood_5 = QLabel(self.content)
        self.label_mood_5.setGeometry(QRect(60, 390, 41, 41))
        self.label_mood_5.setFrameShape(QFrame.Box)
        self.label_mood_5.setAlignment(Qt.AlignCenter)
        self.label_mood_5.setObjectName("label_mood_5")
        self.label_mood_5.setStyleSheet(
            "background: rgb(255, 255, 255);\n"
        )
        self.progress_bar_5 = QProgressBar(self.content)
        self.progress_bar_5.setGeometry(QRect(120, 390, 601, 41))
        self.progress_bar_5.setProperty("value", 0)
        self.progress_bar_5.setObjectName("progress_bar_5")
        self.label_mood_6 = QLabel(self.content)
        self.label_mood_6.setGeometry(QRect(60, 450, 41, 41))
        self.label_mood_6.setFrameShape(QFrame.Box)
        self.label_mood_6.setAlignment(Qt.AlignCenter)
        self.label_mood_6.setObjectName("label_mood_6")
        self.label_mood_6.setStyleSheet(
            "background: rgb(255, 255, 255);\n"
        )
        self.progress_bar_6 = QProgressBar(self.content)
        self.progress_bar_6.setGeometry(QRect(120, 450, 601, 41))
        self.progress_bar_6.setProperty("value", 0)
        self.progress_bar_6.setObjectName("progress_bar_6")
        self.label_mood_7 = QLabel(self.content)
        self.label_mood_7.setGeometry(QRect(60, 510, 41, 41))
        self.label_mood_7.setFrameShape(QFrame.Box)
        self.label_mood_7.setAlignment(Qt.AlignCenter)
        self.label_mood_7.setObjectName("label_mood_7")
        self.label_mood_7.setStyleSheet(
            "background: rgb(255, 255, 255);\n"
        )
        self.progress_bar_7 = QProgressBar(self.content)
        self.progress_bar_7.setGeometry(QRect(120, 510, 601, 41))
        self.progress_bar_7.setProperty("value", 0)
        self.progress_bar_7.setObjectName("progress_bar_7")
        self.label_mood_8 = QLabel(self.content)
        self.label_mood_8.setGeometry(QRect(60, 570, 41, 41))
        self.label_mood_8.setFrameShape(QFrame.Box)
        self.label_mood_8.setAlignment(Qt.AlignCenter)
        self.label_mood_8.setObjectName("label_mood_8")
        self.label_mood_8.setStyleSheet(
            "background: rgb(255, 255, 255);\n"
        )
        self.progress_bar_8 = QProgressBar(self.content)
        self.progress_bar_8.setGeometry(QRect(120, 570, 601, 41))
        self.progress_bar_8.setProperty("value", 0)
        self.progress_bar_8.setObjectName("progress_bar_8")

        self.horizontalLayout.addWidget(self.OpeningPanel)
        self.horizontalLayout.addWidget(self.content)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(Form)
        self.updateView()
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ReturnButton.setText(_translate("Form", "Kembali"))
        self.MoodTitle.setText(_translate("Form", "Mood"))
        self.MoodSubtitle.setText(
            _translate("Form", "Bagaimana perasaanmu \nhari ini?"))
        self.button1.setText(_translate("Form", ":)"))
        self.button6.setText(_translate("Form", ":3"))
        self.button4.setText(_translate("Form", ":v"))
        self.button5.setText(_translate("Form", ":D"))
        self.button2.setText(_translate("Form", ":("))
        self.button3.setText(_translate("Form", ":O"))
        self.button7.setText(_translate("Form", ":|"))
        self.button8.setText(_translate("Form", ":\\"))
        self.labelTanggal.setText(_translate(
            "Form", datetime.datetime.now().strftime("%d/%m/%Y")))
        self.labelMoodSekarang.setText(_translate("Form", ""))
        self.labelFrekuensi.setText(_translate(
            "Form", "Frekuensi Mood 30 Hari Terakhir"))
        self.label_mood_1.setText(_translate("Form", ":)"))
        self.label_mood_2.setText(_translate("Form", ":("))
        self.label_mood_3.setText(_translate("Form", ":O"))
        self.label_mood_4.setText(_translate("Form", ":v"))
        self.label_mood_8.setText(_translate("Form", ":\\"))
        self.label_mood_7.setText(_translate("Form", ":|"))
        self.label_mood_5.setText(_translate("Form", ":D"))
        self.label_mood_6.setText(_translate("Form", ":3"))

    def onClick(self, mood):
        # Set current mood, insert to database, and update view
        self.labelMoodSekarang.setText(mood)
        self.controller.addMood(mood)
        self.updateView()

    def updateView(self):
        # Set current mood
        currentMood = self.controller.getCurrentMood()
        if currentMood is not None:
            self.labelMoodSekarang.setText(currentMood)

        # Set progress bar
        self.progress_bar_1.setValue(self.controller.getPercentage(':)'))
        self.progress_bar_2.setValue(self.controller.getPercentage(':('))
        self.progress_bar_3.setValue(self.controller.getPercentage(':O'))
        self.progress_bar_4.setValue(self.controller.getPercentage(':v'))
        self.progress_bar_5.setValue(self.controller.getPercentage(':D'))
        self.progress_bar_6.setValue(self.controller.getPercentage(':3'))
        self.progress_bar_7.setValue(self.controller.getPercentage(':|'))
        self.progress_bar_8.setValue(self.controller.getPercentage(':\\'))


if __name__ == "__main__":
    abspath = path.dirname(path.abspath(__file__))
    app = QApplication(sys.argv)
    _id = QFontDatabase.addApplicationFont(path.join(abspath, "Resource/Helvetica/Helvetica.ttf"))    

    Form = QWidget()
    ui = MoodForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
