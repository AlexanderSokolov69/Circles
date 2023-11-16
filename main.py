import sys
from random import randint, choice


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication

from Ui import Ui_Form


class Circles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Круги')
        self.pushButton.clicked.connect(self.create_circle)
        self.circles = []
    
    def create_circle(self):
        r = randint(40, 300)
        x = randint(0, self.width()) - r // 2
        y = randint(0, self.height()) - r // 2
        self.circles.append((x, y, r))
        self.update()
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()
    
    def draw(self, qp):
        qp.setPen(QPen(QColor('yellow'), 4, Qt.SolidLine))
        for el in self.circles:
            qp.drawArc(el[0], el[1], el[2], el[2], 0, 360 * 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Circles()
    form.show()
    sys.exit(app.exec())
    
