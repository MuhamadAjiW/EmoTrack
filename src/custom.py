from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import *
from os import path

class OverlaySignals(QObject):
    close = pyqtSignal()
    confirm = pyqtSignal(object)
    delete = pyqtSignal(object)

class MainSignals(QObject):
    switch = pyqtSignal(object)
    
class UIWindow(object):
    def __init__(self):
        super(UIWindow).__init__()
        self.signals = MainSignals()

    def _onswitch(self, dest):
        self.signals.switch.emit(dest)

    def setupUi(self, Form) -> None:
        """Displays Window"""
        pass

class CustomOverlay(QWidget):
    def __init__(self, parent=None):
        super(CustomOverlay, self).__init__(parent)
        self.signals = OverlaySignals()
        self.resources = path.join(path.dirname(path.abspath(__file__)), 'Resource')

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.fillColor = QColor(30, 30, 30, 120)
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(self.fillColor)
        qp.drawRect(0, 0, self.width(), self.height())
        qp.end()

    def _onclose(self):
        self.signals.close.emit()

class CustomSVGImage(QLabel):
    def __init__(self, resource: str, parent=None):
        super(CustomSVGImage, self).__init__(parent)
        self.renderer = QSvgRenderer(resource)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.renderer.render(painter)
    
class CustomSVGButton(QAbstractButton):
    def __init__(self, resource: str, resourceHL: str, parent=None):
        super(CustomSVGButton, self).__init__(parent)
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