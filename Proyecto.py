#!/usr/bin/python

import sys
from PySide import QtCore, QtGui

from drawarea import *

"""
TODO:
	- leer/escribir archivos pbm (listo)
	- modelar la red (listo)
	- procesar los pbm para que sirvan de entrada a la RN(listo)
	- crear red neuronal (listo)
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