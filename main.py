import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QImage
import os
import sys


server = 'https://static-maps.yandex.ru/1.x/?'
par = {"ll": '0,0',
       'spn': '80,80',
       'l': 'sat',
       'size': '400,400'}


class Map(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Yandex maps')
        self.maplabel = QLabel(self)
        self.maplabel.setGeometry(0, 0, 600, 600)
        self.maplabel.setPixmap(self.get_map())

    def get_map(self):
        response = requests.get(server, params=par)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        return QPixmap(map_file).scaled(600, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Map()
    win.show()
    sys.exit(app.exec())