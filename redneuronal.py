#	Archivo de la red neuronal, procedimientos, entrenamiento y procesamiento
#	de todo lo necesario para evaluar las imagenes.

from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets.classification import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from numpy import argmax


def cargarpbm(path):
	f=open(path)
	nombre_imagen=f.readline()
	dimension_imagen=f.readline()
	linea = f.read().replace('\n',' ')
	mat=[]
	for i in linea:
		if i<>' ':
			mat.append(int(i))
	return mat


def rn():
	
	#	Creacion de la red neuronal
	print 'creando red neuronal'
	red_neruronal = buildNetwork(10000,320,10,hiddenclass=TanhLayer)
	print 'Red neuronal creada!'

	#	Creacion del conjunto de datos
	print "Creando conjunto de datos de entramiento"
	#ds = ClassificationDataSet(10000,target=10,nb_classes=10,class_labels=['uno','dos','tres','cuarto','cinco','seis','siete','ocho','nueve','diez'])
	ds = ClassificationDataSet(10000,target=10)
	print 'Conjunto de datos creado'

	#	Agrego las muestras y entreno las neuronas
	print 'Cargar los datos de entramiento'
	ds.addSample(cargarpbm('entrenamiento/0/cero1.pbm'),(0,))
	ds.addSample(cargarpbm('entrenamiento/0/cero2.pbm'),(0,))
	ds.addSample(cargarpbm('entrenamiento/1/uno1.pbm'),(1,))
	ds.addSample(cargarpbm('entrenamiento/1/uno2.pbm'),(1,))
	ds.addSample(cargarpbm('entrenamiento/1/uno3.pbm'),(1,))
	ds.addSample(cargarpbm('entrenamiento/2/dos1.pbm'),(2,))
	ds.addSample(cargarpbm('entrenamiento/2/dos2.pbm'),(2,))
	ds.addSample(cargarpbm('entrenamiento/2/dos3.pbm'),(2,))
	ds.addSample(cargarpbm('entrenamiento/3/tres1.pbm'),(3,))
	ds.addSample(cargarpbm('entrenamiento/3/tres2.pbm'),(3,))
	ds.addSample(cargarpbm('entrenamiento/3/tres3.pbm'),(3,))
	ds.addSample(cargarpbm('entrenamiento/4/cuatro1.pbm'),(4,))
	ds.addSample(cargarpbm('entrenamiento/4/cuatro2.pbm'),(4,))
	ds.addSample(cargarpbm('entrenamiento/4/cuatro3.pbm'),(4,))
	ds.addSample(cargarpbm('entrenamiento/5/cinco1.pbm'),(5,))
	ds.addSample(cargarpbm('entrenamiento/5/cinco2.pbm'),(5,))
	ds.addSample(cargarpbm('entrenamiento/5/cinco3.pbm'),(5,))
	ds.addSample(cargarpbm('entrenamiento/6/seis1.pbm'),(6,))
	ds.addSample(cargarpbm('entrenamiento/6/seis2.pbm'),(6,))
	ds.addSample(cargarpbm('entrenamiento/6/seis3.pbm'),(6,))
	ds.addSample(cargarpbm('entrenamiento/7/siete1.pbm'),(7,))
	ds.addSample(cargarpbm('entrenamiento/7/siete2.pbm'),(7,))
	ds.addSample(cargarpbm('entrenamiento/7/siete3.pbm'),(7,))
	ds.addSample(cargarpbm('entrenamiento/8/ocho1.pbm'),(8,))
	ds.addSample(cargarpbm('entrenamiento/8/ocho2.pbm'),(8,))
	ds.addSample(cargarpbm('entrenamiento/8/ocho3.pbm'),(8,))
	ds.addSample(cargarpbm('entrenamiento/9/nueve1.pbm'),(9,))
	ds.addSample(cargarpbm('entrenamiento/9/nueve2.pbm'),(9,))
	ds.addSample(cargarpbm('entrenamiento/9/nueve3.pbm'),(9,))
	print 'Muestras de entramiento supervisado agregadas'


	print 'Entrenamiento de red neuronal'
	entrenamiento = BackpropTrainer(red_neruronal,ds)
	error = 10
	itera = 0
	while error > 0.001: 
	    error = entrenamiento.train()
	    itera += 1
	    print "Iteracion: {0} - Error: {1}".format(itera, error)
	print 'Entrenamiento de red neuronal completado!'
	#entrenamiento.train()
	resultado=argmax(red_neruronal.activate(cargarpbm('res.pbm')))
	print "\nResultado ", resultado

rn()