#	Archivo de la red neuronal, procedimientos, entrenamiento y procesamiento
#	de todo lo necesario para evaluar las imagenes.

from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets.classification import ClassificationDataSet

#	Creacion de la red neuronal
red_neruronal = buildNetwork(10000,320,10,hiddenclass=TanhLayer)
#	Creacion del conjunto de datos
ds = ClassificationDataSet(2,nb_classes=10,class_labels=['uno','dos','tres','cuarto','cinco','seis','siete','ocho','nueve','diez'])
#falta el entrenamiento y falta tambien la salida

