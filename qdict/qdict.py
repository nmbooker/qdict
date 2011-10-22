#! /usr/bin/env python

import sys
from PyQt4.QtGui import *
from ui import mainwindow

def main():
    app = QApplication(sys.argv)
    main_window = mainwindow.MainWindow()
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()
