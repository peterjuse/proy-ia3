"""
Mi version de ScribbleArea
"""

from PySide import QtCore, QtGui
from pbmformat import PBMImage
from redneuronal import neuralNet
import sys

class ScribbleArea(QtGui.QWidget):
	def __init__(self, parent=None):
		super(ScribbleArea, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_StaticContents)
		self.modified = False
		self.scribbling = False
		self.myPenWidth = 1
		self.myPenColor = QtCore.Qt.black
		self.image = QtGui.QImage()
		self.lastPoint = QtCore.QPoint()

	def saveImage(self):
		visibleImage = self.image
		data = []
		cb,cn = 0, 0
		for x in range(visibleImage.width()):
			fila = []
			for y in range(visibleImage.height()):
				pix = visibleImage.pixel(y,x)
				if QtGui.qRed(pix) == 255:
					fila += [0]
				elif QtGui.qRed(pix) == 0:
					fila += [1]
			data += [fila]
		tempImg = PBMImage()
		tempImg.load("P1","",visibleImage.width(),visibleImage.height(),data)
		tempImg.saveToFile("res.pbm")
		print"imagen guardada!"

	def clearImage(self):
		self.image.fill(QtGui.qRgb(255, 255, 255))
		self.modified = True
		self.update()

	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			self.lastPoint = event.pos()
			self.scribbling = True

	def mouseMoveEvent(self, event):
		if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
			self.drawLineTo(event.pos())

	def mouseReleaseEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton and self.scribbling:
			self.drawLineTo(event.pos())
			self.scribbling = False
		if event.button() == QtCore.Qt.RightButton:
			self.clearImage()

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.drawImage(QtCore.QPoint(0, 0), self.image)

	def resizeEvent(self, event):
		if self.width() > self.image.width() or self.height() > self.image.height():
			newWidth = max(self.width(), self.image.width())
			newHeight = max(self.height(), self.image.height())
			self.resizeImage(self.image, QtCore.QSize(newWidth, newHeight))
			self.update()

		super(ScribbleArea, self).resizeEvent(event)

	def drawLineTo(self, endPoint):
		painter = QtGui.QPainter(self.image)
		painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
				QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
		painter.drawLine(self.lastPoint, endPoint)
		self.modified = True

		rad = self.myPenWidth / 2 + 2
		self.update(QtCore.QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
		self.lastPoint = QtCore.QPoint(endPoint)

	def resizeImage(self, image, newSize):
		if image.size() == newSize:
			return
		newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
		newImage.fill(QtGui.qRgb(255, 255, 255))
		painter = QtGui.QPainter(newImage)
		painter.drawImage(QtCore.QPoint(0, 0), image)
		self.image = newImage

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.scribbleArea = ScribbleArea()
		self.setCentralWidget(self.scribbleArea)
		self.setWindowTitle("Entrada")
		self.setFixedSize(100, 100)
		self.red = neuralNet()
		self.red.entrenar()

	def closeEvent(self, event):
		#event.accept()
		self.hide()
		event.ignore()
		sys.exit()

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Escape:
			self.close()
			sys.exit()
		elif e.key() == QtCore.Qt.Key_S:
			self.scribbleArea.saveImage()
			self.red.activar("res.pbm")




if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
