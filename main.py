import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
import os
import sys


server = 'https://static-maps.yandex.ru/1.x/?'
par = {"ll": '40.692065,55.615141',
       'spn': '0.001,0.001',
       'l': 'map',
       'size': '400,400'}


class Map(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('Yandex maps')
        self.maplabel = QLabel(self)
        self.maplabel.setGeometry(0, 0, self.width(), self.height())
        self.maplabel.setPixmap(self.get_map())

    def get_map(self):
        response = requests.get(server, params=par)
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        return QPixmap(self.map_file).scaled(self.maplabel.width(), self.maplabel.height())

#    def keyPressEvent(self, event):
#        if event.

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Map()
    win.show()
    sys.exit(app.exec())