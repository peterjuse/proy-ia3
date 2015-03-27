#!/usr/bin/python

#Nota: con esta ultima version deje de escribir comentarios en los archivos generados (no nos hace falta de todos modos)

from pprint import pprint

class PBMImage(object):
	"""Imagen PBM"""
	def __init__(self):
		super(PBMImage, self).__init__()
		self.magic_number = ""
		self.comment = ""
		self.width, self.height = [0, 0]
		self.data = []

	def load(self, magic_number, comment, width, height, data):
		self.magic_number = magic_number
		self.comment = comment
		self.width = width
		self.height = height
		self.data = data

	def loadFromFile(self, filename):
		with open(filename) as f:
			magic_number = f.readline()[:-1]
			comment = []
			temp = f.readline()
			while temp[0] == '#':
				comment.append(temp[:-1])
				temp = f.readline()
			width, height = temp.split()
			dataMatrix = f.readlines()
			data = []
			for linea in dataMatrix:
				linea = linea.split()
				linea = map(int, linea)
				data += [linea]
		self.load(magic_number, comment, width, height, data)
		return True

	def display(self):
		print "Magic Number:"+self.magic_number+"|"
		print "Comment:"
		pprint(self.comment)
		print "Width:"+self.width+"|"
		print "Height:"+self.height+"|"
		print "Data:"
		pprint(self.data)
		
	def saveToFile(self, filename):
		with open(filename, 'w') as f:
			f.write(self.magic_number+'\n')
			#for c in self.comment:
			#	f.write( c +'\n')
			f.write(str(self.width)+' '+str(self.height)+"\n")
			for fila in self.data:
				f.write(" ".join(map(str, fila))+"\n")
		return True

if __name__ == '__main__':
	print "Este archivo no debe ejecutarse directamente sino utilizado desde Proyecto.py"
	exit()