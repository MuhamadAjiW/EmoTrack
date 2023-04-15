from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import *

class mainSignals(QObject):
    switch = pyqtSignal(object)
    
class UIWindow(object):
    def __init__(self):
        super(UIWindow).__init__()
        self.signals = mainSignals()

    def setupUi(self, Form, abspath) -> None:
        """Displays Window"""
        pass

class customSVGImage(QLabel):
    def __init__(self, resource: str, parent=None):
        super(customSVGImage, self).__init__(parent)
        self.renderer = QSvgRenderer(resource)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.renderer.render(painter)
    
class customSVGButton(QAbstractButton):
    def __init__(self, resource: str, resourceHL: str, parent=None):
        super(customSVGButton, self).__init__(parent)
        self.normalImage = resource
        self.highlightImage = resourceHL
        self.renderer = QSvgRenderer(self.normalImage)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.renderer.render(painter)

    def changeGeometry(self, x, y, width, height):
        self.setGeometry(QRect(x, y, width, height))
        self.update()

    def enterEvent(self, a0: QEvent) -> None:
        self.renderer = QSvgRenderer(self.highlightImage)
        return super().enterEvent(a0)
    
    def leaveEvent(self, a0: QEvent) -> None:
        self.renderer = QSvgRenderer(self.normalImage)
        return super().leaveEvent(a0)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.move(QPoint(self.x() - 2, self.y() + 2))
        return super().mousePressEvent(e)
    
    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        self.move(QPoint(self.x() + 2, self.y() - 2))
        return super().mouseReleaseEvent(e)