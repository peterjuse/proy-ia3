#	Archivo de la red neuronal, procedimientos, entrenamiento y procesamiento
#	de todo lo necesario para evaluar las imagenes.

from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets.classification import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from numpy import argmax
import cv2

class neuralNet(object):
	"""Representacion de la red neuronal como objeto"""
	def __init__(self):
		super(neuralNet, self).__init__()
		#	Creacion de la red neuronal
		print 'creando red neuronal'
		self.red = buildNetwork(30000,320,1,hiddenclass=TanhLayer)
		print 'Red neuronal creada!'

		#	Creacion del conjunto de datos
		print "Creando conjunto de datos de entramiento"
		self.ds = ClassificationDataSet(30000,target=1,nb_classes=10,class_labels=['uno','dos','tres','cuarto','cinco','seis','siete','ocho','nueve','diez'])
		print 'Conjunto de datos creado'

		#	Agrego las muestras y entreno las neuronas
		print 'Cargar los datos de entramiento'
		self.ds.addSample(self.cargarpbm('entrenamiento/0/cero1.pbm'),(0,))
		self.ds.addSample(self.cargarpbm('entrenamiento/0/cero2.pbm'),(0,))
		self.ds.addSample(self.cargarpbm('entrenamiento/1/uno1.pbm'),(1,))
		self.ds.addSample(self.cargarpbm('entrenamiento/1/uno2.pbm'),(1,))
		self.ds.addSample(self.cargarpbm('entrenamiento/1/uno3.pbm'),(1,))
		self.ds.addSample(self.cargarpbm('entrenamiento/2/dos1.pbm'),(2,))
		self.ds.addSample(self.cargarpbm('entrenamiento/2/dos2.pbm'),(2,))
		self.ds.addSample(self.cargarpbm('entrenamiento/2/dos3.pbm'),(2,))
		self.ds.addSample(self.cargarpbm('entrenamiento/3/tres1.pbm'),(3,))
		self.ds.addSample(self.cargarpbm('entrenamiento/3/tres2.pbm'),(3,))
		self.ds.addSample(self.cargarpbm('entrenamiento/3/tres3.pbm'),(3,))
		self.ds.addSample(self.cargarpbm('entrenamiento/4/cuatro1.pbm'),(4,))
		self.ds.addSample(self.cargarpbm('entrenamiento/4/cuatro2.pbm'),(4,))
		self.ds.addSample(self.cargarpbm('entrenamiento/4/cuatro3.pbm'),(4,))
		self.ds.addSample(self.cargarpbm('entrenamiento/5/cinco1.pbm'),(5,))
		self.ds.addSample(self.cargarpbm('entrenamiento/5/cinco2.pbm'),(5,))
		self.ds.addSample(self.cargarpbm('entrenamiento/5/cinco3.pbm'),(5,))
		self.ds.addSample(self.cargarpbm('entrenamiento/6/seis1.pbm'),(6,))
		self.ds.addSample(self.cargarpbm('entrenamiento/6/seis2.pbm'),(6,))
		self.ds.addSample(self.cargarpbm('entrenamiento/6/seis3.pbm'),(6,))
		self.ds.addSample(self.cargarpbm('entrenamiento/7/siete1.pbm'),(7,))
		self.ds.addSample(self.cargarpbm('entrenamiento/7/siete2.pbm'),(7,))
		self.ds.addSample(self.cargarpbm('entrenamiento/7/siete3.pbm'),(7,))
		self.ds.addSample(self.cargarpbm('entrenamiento/8/ocho1.pbm'),(8,))
		self.ds.addSample(self.cargarpbm('entrenamiento/8/ocho2.pbm'),(8,))
		self.ds.addSample(self.cargarpbm('entrenamiento/8/ocho3.pbm'),(8,))
		self.ds.addSample(self.cargarpbm('entrenamiento/9/nueve1.pbm'),(9,))
		self.ds.addSample(self.cargarpbm('entrenamiento/9/nueve2.pbm'),(9,))
		self.ds.addSample(self.cargarpbm('entrenamiento/9/nueve3.pbm'),(9,))
		print 'Muestras de entramiento supervisado agregadas'

	def entrenar(self,maxErr=0.1):
		print 'Entrenamiento de red neuronal'
		self.entrenamiento = BackpropTrainer(self.red,self.ds)
		error = 10
		itera = 0
		while error > maxErr: 
		    error = self.entrenamiento.trainUntilConvergence()
		    itera += 1
		    print "Iteracion: {0} - Error: {1}".format(itera, error)
		print 'Entrenamiento de red neuronal completado!'
		return self

	def flatten(self,x):
		result = []
		for el in x:
			if hasattr(el, "__iter__") and not isinstance(el, basestring):
				result.extend(self.flatten(el))
			else:
				result.append(el)
		return result

	def cargarpbm(self,path):
		im = cv2.imread(path)
		return self.flatten(im)


	def activar(self,path):
		resultado=argmax(self.red.activate(self.cargarpbm(path)))
		print "\nResultado ", resultado
