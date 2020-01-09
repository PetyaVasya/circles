import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


def random_color():
    return (randint(0, 256) for _ in range(3))


def random_size(max_size):
    return randint(5, max(5, max_size))


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.circles)
        self.last = []

    def circles(self):
        self.last = [(randint(0, self.width()), randint(0, self.height())) for _ in range(10)]
        self.repaint()

    def paintEvent(self, *__args):
        if self.last:
            qp = QPainter(self)
            # qp.setBrush(QColor(*random_color()))
            qp.setBrush(QColor(255, 255, 0))
            for i in range(10):
                height = random_size(min(
                    self.height(),
                    self.width(),
                    self.height() - self.last[i][0],
                    self.width() - self.last[i][1],
                ))
                qp.drawEllipse(self.last[i][0], self.last[i][1], height, height)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
