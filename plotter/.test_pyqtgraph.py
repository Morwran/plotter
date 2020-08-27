#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from PyQt4 import QtCore, QtGui, QtSvg, uic
from PyQt4.QtWebKit import QGraphicsWebView
import pyqtgraph as pg
import datetime,sys,copy
from PyQt4.QtCore import QSize, Qt
from PyQt4.QtGui import QTableWidgetItem, QGridLayout 

import numpy as np
import binascii, re,time

from collections import deque, namedtuple 

#from threading import Thread

from rpi_serial import RpiSerial

stop_thrd1 = False
dump_size = 640
Amax = 16
Pmax = 0
Pmin = -16
kt=1500./(65534.*33.)

class mythread(QtCore.QThread):

	def __init__(self,parent,num):
		QtCore.QThread.__init__(self,parent)

		
		self.num=num
		#self.fn=fn()
		
		
	def __del__(self):
		self.wait()	

	def run(self):
		global stop_thrd1
		
		if self.num=='read uart':
			
			
			while 1:
				#if stop_thrd1:
				#	break
				#else:	
				self.emit(QtCore.SIGNAL("update()"))
				time.sleep(0.4)




class MyForm(QtGui.QMainWindow,RpiSerial):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui = uic.loadUi("mainwindow.ui",self)
		port="/dev/ttyUSB1"
		baudrate=115200
		stopbits=1
		parity="N"
		bytesizes=8
		RpiSerial.__init__(self,port,baudrate,stopbits,parity,bytesizes)
		self.close()
		self.open()
		self.clearFIFO()

		self.ui.action_load_dump.triggered.connect(self.load_dump)
		self.ui.action_close.triggered.connect(self.closeEvent)
		self.ui.action_rst.triggered.connect(self.rst)


		#графики
			#лайауты для графиков
		self.lo_plt1_ch1 = self.ui.p_ch1_lo1
		self.lo_plt2_ch1 = self.ui.p_ch1_lo2

		#self.lo_plt1_ch2 = self.ui.p_ch2_lo1
		#self.lo_plt2_ch2 = self.ui.p_ch2_lo2

		pg.setConfigOptions(antialias=True) 


		#self.plt1_ch1 = self.init_plot('time')
		#self.lo_plt1_ch1.addWidget(self.plt1_ch1)
#
		#self.plt1_ch2 = self.init_plot('time')
		#self.lo_plt1_ch2.addWidget(self.plt1_ch2)
#
		#self.plt2_ch1 = self.init_plot('freq')
		#self.lo_plt2_ch1.addWidget(self.plt2_ch1)
#
		#self.plt2_ch2 = self.init_plot('freq')
		#self.lo_plt2_ch2.addWidget(self.plt2_ch2)
#
		#self.pltCurve1_ch1 = self.plt1_ch1.plot(pen='g',symbolSize=1)
		#self.pltCurve2_ch1 = self.plt1_ch1.plot(pen='r',symbolSize=4)
		#
		#self.pltCurve1_ch2 = self.plt1_ch2.plot(pen='g',symbolSize=1)
		#self.pltCurve2_ch2 = self.plt1_ch2.plot(pen='r',symbolSize=4)

		#self.plt1_ch = self.init_plot('time')
		self.plt1_ch = pg.PlotWidget(
			title=u"Временная область",
			labels={'bottom': 'отсчеты','left': 'амплитуда'}
			#axisItems={'left': TimeAxisItem(orientation='left')}
		)
		self.plt1_ch.setXRange(0, dump_size)
		self.plt1_ch.setYRange(-Amax, Amax)
		self.plt1_ch.showGrid(x=True, y=True)
		self.plt1_ch.addLegend()

		self.plt1_ch.setBackground('w')	
		self.lo_plt1_ch1.addWidget(self.plt1_ch)
		#self.lo_plt1_ch2.addWidget(self.plt1_ch[1])

		#self.plt2_ch = self.init_plt_list('freq')
		#self.lo_plt2_ch1.addWidget(self.plt2_ch[0])
		#self.lo_plt2_ch2.addWidget(self.plt2_ch[1])

		self.pltCurve1_ch1 = self.plt1_ch.plot(pen='g',symbolSize=1)
		#self.pltCurve2_ch1 = self.plt2_ch[0].plot(pen='r',symbolSize=4)
		
		#self.pltCurve1_ch2 = self.plt1_ch[1].plot(pen='g',symbolSize=1)
		#self.pltCurve2_ch2 = self.plt2_ch[1].plot(pen='r',symbolSize=4)

		self.pltData1_ch1 = {'x': [], 'y': []}				

		self.start_tr = re.compile('tr start')
		self.stop_tr = re.compile('tr end')
		self.start_flg=False

		self.center()
		#self.start()
		self.t1=mythread(self,'read uart')
		QtCore.QObject.connect(self.t1, QtCore.SIGNAL("update()"),self.th_read)
		#stop_thrd1=True
		self.t1.start()

		self.pltData1_ch1['x']=range(0,dump_size)
		#self.pltData1_ch1['y']=np.random.uniform(-Amax,Amax,160)
		#self.pltData1_ch1['y']=[0 for x in range(0,dump_size)]

		#self.pltCurve1_ch1.setData(self.pltData1_ch1['x'], self.pltData1_ch1['y'])
		


	def init_plot(self,tp):
		if tp=='time':
			self.plt = pg.PlotWidget(
				title=u"Временная область",
				labels={'bottom': 'отсчеты','left': 'амплитуда'}
				#axisItems={'left': TimeAxisItem(orientation='left')}
			)
			self.plt.setXRange(0, dump_size)
			self.plt.setYRange(-Amax, Amax)
		elif tp=='freq':
			self.plt = pg.PlotWidget(
				title=u"Частотная область",
				labels={'bottom': 'отсчеты','left': 'мощность'}
				#axisItems={'left': TimeAxisItem(orientation='left')}
			)
			self.plt.setXRange(0, dump_size)
			self.plt.setYRange(Pmin, Pmax)

		self.plt.showGrid(x=True, y=True)
		self.plt.addLegend()
		#plt.enableMouse()
		self.plt.setBackground('w')	
		return self.plt	

	def init_plt_list(self,tp):
		self.plt_list=[]
		for i in range(0,2):
			if tp=='time':
				self.plt = pg.PlotWidget(
					title=u"Временная область",
					labels={'bottom': 'отсчеты','left': 'амплитуда'}
					#axisItems={'left': TimeAxisItem(orientation='left')}
				)
				self.plt.setXRange(0, dump_size)
				self.plt.setYRange(-Amax, Amax)
			elif tp=='freq':
				self.plt = pg.PlotWidget(
					title=u"Частотная область",
					labels={'bottom': 'отсчеты','left': 'мощность'}
					#axisItems={'left': TimeAxisItem(orientation='left')}
				)
				self.plt.setXRange(0, dump_size)
				self.plt.setYRange(Pmin, Pmax)
	
			self.plt.showGrid(x=True, y=True)
			self.plt.addLegend()
			#plt.enableMouse()
			self.plt.setBackground('w')	

			self.plt_list.append(self.plt)

		return self.plt_list			

	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)  
		#QtGui.QWidget.updateGeometry(screen) 

	def closeEvent(self, event):
		# Переопределить colseEvent
		global stop_thrd1
		#print "event",type(event)
		if type(event)==bool:
			evnt=not event
			print "ok"
		else:
			evnt=event.spontaneous()
		if evnt:
			reply = QtGui.QMessageBox.question\
			(self, u'Информация',
				u"Вы уверены, что хотите уйти?",
				 QtGui.QMessageBox.Yes,
				 QtGui.QMessageBox.No)
			if reply == QtGui.QMessageBox.Yes:
				#print("Пока pushButton")
				self.t1.quit()
				stop_thrd1=True

				#self.t1.wait()
				if type(event)==bool:
					app.quit()
				else:	
					event.accept()

			else:
				if type(event)!=bool:
					event.ignore()

	def load_dump(self):
		global stop_thrd1
		self.cmd="msr start m2"
		print"loading dump..."	
		stop_thrd1=True
		self.t1.start()
		self.write_byte(self.cmd)

	def rst(self):
		self.cmd="rst m2"
		print"reseting modul..."	
		self.write_byte(self.cmd)	


	#def start(self):
	#	self.t1 = Thread(target=self.th_read, args=())
	#	#self.t2 = Thread(target=self.th_write, args=())
	#	self.t1.start()
	#	#self.t2.start()
	#	self.t1.join()
	#	#self.t2.join()	

	def th_read(self):
		#while 1:
		t=time.time()
		self.collect()
		#print"time:",time.time()-t

	def collect(self):
		global stop_thrd1
		self.read_str = self.read()	
		if(len(self.read_str.split())!=0):

			s_start=re.search(self.start_tr,self.read_str)
			s_stop=re.search(self.stop_tr,self.read_str)

			if(s_start):
				self.read_buff=[]
				self.pltData1_ch1['y']=[]
				#print "s_start.group",s_start.group()
				#print "self.read_str",self.read_str
				self.start_flg=True

			if(s_stop):
				self.start_flg=False
				stop_thrd1=False

				#print "s_stop.group()",s_stop.group()
				##print "self.read_str",self.read_str
				#print "len buff",len(self.read_buff)
				#print "len str",len(self.read_buff[0])
				split_buff=[self.read_buff[0][x:x+4] for x in range (4, len(self.read_buff[0])-4, 4)]
				self.ch1_list=[]
				self.ch2_list=[]
				for indx,ch in enumerate(split_buff):
					if not indx%2:
						self.ch2_list.append(float(np.int16(int((ch[2]+ch[3]+ch[0]+ch[1]),base=16)))*kt)
						
					else:
						self.ch1_list.append(float(np.int16(int((ch[2]+ch[3]+ch[0]+ch[1]),base=16)))*kt)
						self.pltData1_ch1['y'].append(float(np.int16(int((ch[2]+ch[3]+ch[0]+ch[1]),base=16)))*kt)
						#self.pltData1_ch1['x'].append(indx)
						

				print "ch1",len(self.pltData1_ch1['y'])
				print "ch2",len(self.pltData1_ch1['x'])

				

				self.pltCurve1_ch1.setData(self.pltData1_ch1['x'][:160], self.pltData1_ch1['y'][:160])
				#self.pltData1_ch1['x']=range(0,len(self.ch1_list))
				#self.pltData1_ch1['y']=self.ch1_list

				#self.pltCurve1_ch1.setData(self.pltData1_ch1['x'], self.pltData1_ch1['y'])
				#self.pltCurve1_ch2.setData(range(0,len(self.ch1_list)), self.ch2_list)

				#print "self.read_buff",self.read_buff	
				#self.t1.quit()
				self.write_byte("msr stop m2")

			if(not self.start_flg):
				print self.read_str

			if(self.start_flg and not s_start):	
				self.read_buff.append(binascii.hexlify(self.read_str))	
		self.pltCurve1_ch1.setData(self.pltData1_ch1['x'][:160], self.pltData1_ch1['y'][:160])		

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	MyForm().show()

	sys.exit(app.exec_()) 	
		