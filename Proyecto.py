#!/usr/bin/python

import sys
from PySide import QtCore, QtGui

from drawarea import *

#import redneuronal

"""
TODO:
	- leer/escribir archivos pbm (listo)
	- modelar la red
	- procesar los pbm para que sirvan de entrada a la RN
	- crear red neuronal
	- disenhar interfaz ("listo" realmente preferi que la interfaz se limite al area donde se permitira escribir el/los numero(s) )
	- implementar funcionalidades de la interfaz (listo - excepto las de la RN ya estan todas asociadas a teclas)
	- convertir entrada manual en pbm (listo!)
"""

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()
	sys.exit()