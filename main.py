import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication

from random import randint

yellow = QColor(255, 255, 0)


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def draw_circles(self, qp):
        qp.setBrush(yellow)
        D = randint(10, 100)
        qp.drawEllipse(randint(0, self.width()), randint(0, self.height()), D, D)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Form()
    ex.show()

    sys.exepthook = except_hook
    sys.exit(app.exec())
