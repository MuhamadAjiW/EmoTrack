from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import *

class customImage(QLabel):
    def __init__(self, pixmap, parent=None):
        super(customImage, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()
    
class customTextButton(QAbstractButton):
    def __init__(self, text: str, parent=None):
        super(customTextButton, self).__init__(parent)
        self.border = QFrame(self)
        self.border.setFrameShape(QFrame.StyledPanel)
        self.border.setStyleSheet(
                                "border-width: 2;"
                                "border-style: solid;"
                                )
        
        self.label = QLabel(text, self.border)
        self.label.setGeometry(QRect(5, 5, self.geometry().width() + 80, self.geometry().height()))
        self.label.setStyleSheet(
                                "border-width: 0;"
                                "border-style: solid;"
                                )
        self.label.setContentsMargins(5, 0, 0, 0)

        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.label.setFont(font)

    def setText(self, text: str) -> None:
        self.label.setText(text)
        return super().setText(text)

    def paintEvent(self, event):
        return

    def changeGeometry(self, x, y, width, height):
        self.setGeometry(QRect(x, y, width, height))
        self.update()

    def enterEvent(self, a0: QEvent) -> None:
        self.border.setStyleSheet(
                                "background-color: rgb(198, 227, 242);"
                                "border-width: 2;"
                                "border-style: solid;"
                                )
        return super().enterEvent(a0)
    
    def leaveEvent(self, a0: QEvent) -> None:
        self.border.setStyleSheet(
                        "background-color: transparent;"
                        "border-width: 2;"
                        "border-style: solid;"
                        )
        return super().leaveEvent(a0)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.move(QPoint(self.x() - 2, self.y() + 2))
        return super().mousePressEvent(e)
    
    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        self.move(QPoint(self.x() + 2, self.y() - 2))
        return super().mouseReleaseEvent(e)
    
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