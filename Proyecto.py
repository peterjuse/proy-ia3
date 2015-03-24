#!/usr/bin/python

from pbmformat import PBMImage

"""
TODO:
	- leer/escribir archivos pbm (listo)
	- modelar la red
	- procesar los pbm para que sirvan de entrada a la RN
	- crear red neuronal
	- disenhar interfaz
	- implementar funcionalidades de la interfaz
	- convertir entrada manual en pbm
"""

def main():
	print "prueba de archivos pbm!"
	print "--carga desde archivo--"
	test = PBMImage()
	test.loadFromFile("./archivos pbm/J.pbm")
	test.display()
	print "----"
	print "--guardar a archivo--"
	test.saveToFile("save.pbm")
	print "----\n FIN"



if __name__ == '__main__':
	main()
	exit()