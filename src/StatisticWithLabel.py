from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class StatisticWithLabel(QHBoxLayout):
    def __init__(self, parent=None, labelText="label", barValue=10, barMax=11):
        super(StatisticWithLabel, self).__init__(parent)
        self.setObjectName("Statistik" + labelText)
        self.setStretch(1, 5)
        
        self.label = QLabel(labelText, parent)
        self.label.setMinimumHeight(50)
        self.label.setMinimumWidth(100)

        self.bar = QProgressBar(parent)
        self.bar.setMaximum(barMax)
        self.bar.setValue(barValue)
        self.refreshBar

        self.bar.setMinimumHeight(30)
        self.bar.setContentsMargins(0, 10, 0, 10)

        self.addWidget(self.label)
        self.addWidget(self.bar)

    def refreshBar(self):
        self.bar.setFormat('{0}/{1}'.format(self.bar.value(), self.bar.maximum()))
        

        


        
        

        
    
    