#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#exec env LD_LIBRARY_PATH=/some/path/to/lib /path/to/specific/python -x "$0" "$@"
#exec env LD_LIBRARY_PATH=/home/kvb/prj/qcustomplot-python /usr/bin/env -x "$0" "$@"



from PyQt4 import QtCore, QtGui, QtSvg, uic
from PyQt4.QtWebKit import QGraphicsWebView

import datetime,sys,os,shutil,copy, scipy
from PyQt4.QtCore import QSize, Qt
from PyQt4.QtGui import QTableWidgetItem, QGridLayout, QColor, QWidget 

import numpy as np
import binascii, re,time

from collections import deque, namedtuple 

#from threading import Thread

from rpi_serial import RpiSerial

if len (sys.argv) > 1:
	sys.path.insert(0, str(sys.argv[1]))
else:
	sys.path.insert(0, "/home/kvb/prj/qcustomplot-python/")

import qcustomplot as qcp

stop_thrd1 = False
dump_size = 162 #640
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
		#global stop_thrd1
		
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
		self.msg={'serial':'ok'}
		self.access_rights = 0o777
		

		self.uart_settings_list=[self.ui.port_edit,\
									self.ui.baud_edit,\
									self.ui.parity_comb,\
									self.ui.stp_bts_comb,\
									self.ui.byte_comb]	
		self.init_uart()							

		#print "uart_settings_list",	self.uart_settings_list						

		self.save_uart=	self.ui.save_uart
		self.save_uart.clicked.connect(self.save_settings_uart)

		self.ui.action_load_dump.triggered.connect(self.load_dump)
		self.ui.action_close.triggered.connect(self.closeEvent)
		self.ui.action_rst.triggered.connect(self.rst)
		self.ui.action_clean_uart.triggered.connect(self.clean_uart)
		self.ui.action_clean_all.triggered.connect(self.clean_all)
		self.ui.action_clean1_2_all.triggered.connect(self.clean1_2_all)
		self.ui.action_clean1_2_today.triggered.connect(self.clean1_2_today)
		self.ui.action_clean1_all.triggered.connect(self.clean1_all)
		self.ui.action_clean1_today.triggered.connect(self.clean1_today)
		self.ui.action_clean2_all.triggered.connect(self.clean2_all)
		self.ui.action_clean2_today.triggered.connect(self.clean2_today)


		self.edit_x1 = self.ui.edit_x1
		self.edit_y1 = self.ui.edit_y1

		self.edit_x2 = self.ui.edit_x2
		self.edit_y2 = self.ui.edit_y2

		self.cont_cb = self.ui.cont_cb
		self.wr_all = self.ui.wr_all
		self.wr_1 = self.ui.wr_1
		self.wr_2 = self.ui.wr_2
		self.wr_all.toggled.connect(self.click_write_all)
		self.wr_1.toggled.connect(self.click_write_1)
		self.wr_2.toggled.connect(self.click_write_2)

		self.lcd_f0_1 = self.ui.lcd_f0_1
		self.lcd_p1 = self.ui.lcd_p_1

		self.lcd_f0_2 = self.ui.lcd_f0_2
		self.lcd_p2 = self.ui.lcd_p_2

		self.fstart_comb1 = self.ui.fstart_comb1
		self.fstart_comb1.currentIndexChanged.connect(self.fstart1_changed)

		self.fstart_comb2 = self.ui.fstart_comb2
		self.fstart_comb2.currentIndexChanged.connect(self.fstart2_changed)

		

		self.fend_comb1 = self.ui.fend_comb1
		self.fend_comb1.currentIndexChanged.connect(self.fend1_changed)
		self.fend_comb2 = self.ui.fend_comb2
		self.fend_comb2.currentIndexChanged.connect(self.fend2_changed)

		flist=(map(lambda x: (x*8.0/dump_size), range(0,dump_size/2,1)))
		for f_indx in flist:
			self.fstart_comb1.addItem(str(f_indx))
			self.fend_comb1.addItem(str(f_indx))
			self.fstart_comb2.addItem(str(f_indx))
			self.fend_comb2.addItem(str(f_indx))	

		self.d_from_1=0
		self.d_to_1=len(flist)		

		self.d_from_2=0
		self.d_to_2=len(flist)		

		#self.cont_cb.stateChanged.connect(self.click_cont_cb)


		self.start_tr = re.compile('tr start')
		self.stop_tr = re.compile('tr end')
		self.start_flg=False

		self.center()

		self.plt1_ch1 = self.ui.p_ch1_lo1
		self.plt1_ch1 = self.init_graph(self.plt1_ch1,'time',Qt.red,0,dump_size,-Amax,Amax)

		#connect(self.plt1_ch1, SIGNAL(mouseMove()), this, SLOT(mouseMove(QMouseEvent*)));
		self.plt1_ch1.installEventFilter(self)

		#QtCore.QObject.connect(self.plt1_ch1, QtCore.SIGNAL('mouseMove(QMouseEvent)'), self.m_event)

		self.plt2_ch1 = self.ui.p_ch1_lo2
		self.plt2_ch1 = self.init_graph(self.plt2_ch1,'freq',Qt.blue,0,dump_size,Pmin,0)
		self.plt2_ch1.installEventFilter(self)

		self.plt1_ch2 = self.ui.p_ch2_lo1
		self.plt1_ch2 = self.init_graph(self.plt1_ch2,'time',Qt.red,0,dump_size,-Amax,Amax)
		self.plt1_ch2.installEventFilter(self)
		self.plt2_ch2 = self.ui.p_ch2_lo2
		self.plt2_ch2 = self.init_graph(self.plt2_ch2,'freq',Qt.blue,0,dump_size,Pmin,0)
		self.plt2_ch2.installEventFilter(self)

		self.t1=mythread(self,'read uart')
		if self.msg['serial']!='err':
			
			QtCore.QObject.connect(self.t1, QtCore.SIGNAL("update()"),self.th_read)
		#stop_thrd1=True
			self.t1.start()

	def is_dir_exist(self,dir_path):
		now = datetime.datetime.now()
		if(os.path.exists(dir_path)):
			
			if(os.path.exists(dir_path+now.strftime("%d-%m-%Y"))):
				if(os.path.exists(dir_path+now.strftime("%d-%m-%Y")+'/ampl')):
					pass
				else:
					self.creat_dir(dir_path+now.strftime("%d-%m-%Y")+'/ampl')
				if(os.path.exists(dir_path+now.strftime("%d-%m-%Y")+'/freq')):
					pass
				else:
					self.creat_dir(dir_path+now.strftime("%d-%m-%Y")+'/freq')		

			else:
				self.creat_dir(dir_path+now.strftime("%d-%m-%Y")+'/ampl')
				self.creat_dir(dir_path+now.strftime("%d-%m-%Y")+'/freq')
		else:
			self.creat_dir(dir_path+now.strftime("%d-%m-%Y")+'/ampl')
			self.creat_dir(dir_path+now.strftime("%d-%m-%Y")+'/freq')		

	def creat_dir(self,dir_path):
		try:
			os.makedirs(dir_path,self.access_rights)
		except OSError as er:
			print ("Создать директорию %s не удалось" % dir_path)		
			print er

	def creat_path(self,num):
		
		if num=='all':
			if(os.path.exists('measure')):
				self.is_dir_exist('measure/ch1/')
				self.is_dir_exist('measure/ch2/')
			else:
				now = datetime.datetime.now()
				dir_path11='measure/ch1/'+now.strftime("%d-%m-%Y")+'/ampl'
				dir_path12='measure/ch1/'+now.strftime("%d-%m-%Y")+'/freq'
				dir_path21='measure/ch2/'+now.strftime("%d-%m-%Y")+'/ampl'
				dir_path22='measure/ch2/'+now.strftime("%d-%m-%Y")+'/freq'
				self.creat_dir(dir_path11)
				self.creat_dir(dir_path12)	
				self.creat_dir(dir_path21)
				self.creat_dir(dir_path22)

		if num=='ch1':
			if(os.path.exists('measure')):
				self.is_dir_exist('measure/ch1/')
			else:
				now = datetime.datetime.now()
				dir_path1='measure/ch1/'+now.strftime("%d-%m-%Y")+'/ampl'
				dir_path2='measure/ch1/'+now.strftime("%d-%m-%Y")+'/freq'
				self.creat_dir(dir_path1)
				self.creat_dir(dir_path2)	

		if num=='ch2':
			if(os.path.exists('measure')):
				self.is_dir_exist('measure/ch2/')
			else:
				now = datetime.datetime.now()
				dir_path1='measure/ch2/'+now.strftime("%d-%m-%Y")+'/ampl'
				dir_path2='measure/ch2/'+now.strftime("%d-%m-%Y")+'/freq'
				self.creat_dir(dir_path1)
				self.creat_dir(dir_path2)	
				

	def click_write_all(self,state):

		#if state == QtCore.Qt.Checked:
		if self.wr_all.isChecked():
			self.wr_1.setChecked(True)
			self.wr_2.setChecked(True)
			#print"chk"
		else:
			self.wr_1.setChecked(False)
			self.wr_2.setChecked(False)
			#print"not chk"	

	def click_write_1(self,state):

		#if state == QtCore.Qt.Checked:
		if self.wr_1.isChecked():
			self.creat_path('ch1')
			#print"chk1"
		else:
			print"not chk1"				

	def click_write_2(self,state):

		#if state == QtCore.Qt.Checked:
		if self.wr_2.isChecked():
			self.creat_path('ch2')
			#print"chk2"
		else:
			print"not chk2"	

	def init_tabs_uart(self,port,baudrate):
		for st in self.uart_settings_list:
			if st==self.ui.port_edit:
				st.setText('%s' % (port))
			elif st==self.ui.baud_edit:
				st.setText('%s' % (str(baudrate)))

			elif st==self.ui.parity_comb:
				st.addItem("N")
				st.addItem("O")
				st.addItem("E")
			elif st==self.ui.stp_bts_comb:
				st.addItem("1")
				st.addItem("2")

			elif st==self.ui.byte_comb:
				st.addItem("8")
				st.addItem("9")

													
				

	def init_uart(self):
		file_path=".settings"
		port="/dev/ttyUSB0"
		baudrate=115200
		stopbits=1
		parity="N"
		bytesizes=8
		settings_list=[]
		if(os.path.isfile(file_path)):
			try:
				settings_file = open('.settings')
			except IOError as e:
				print(u'не удалось открыть файл')
			else:
				settings = settings_file.readline()
				settings_list.append(settings[:-2])
				while settings:
					#print (settings)
					settings = settings_file.readline()
					settings_list.append(settings[:-2])

				settings_file.close()
				#port,baudrate,stopbits,parity,bytesizes
				RpiSerial.__init__(self,settings_list[0],settings_list[1],\
					(stopbits if settings_list[3]=='' else int(settings_list[3])),\
					(parity if settings_list[2]=='' else settings_list[2]),\
					(bytesizes if settings_list[4]=='' else int(settings_list[4])))
				#print"settings_list",settings_list	
				self.init_tabs_uart(settings_list[0],settings_list[1])
		else:
			RpiSerial.__init__(self,port,baudrate,stopbits,parity,bytesizes)	
			self.init_tabs_uart(port,baudrate)			

		
		
		try:
			self.close()
			self.open()
			self.clearFIFO()
		except:
			QtGui.QMessageBox.warning(QWidget(), "Warning", u"вставь COM-PORT")
			self.msg['serial']='err'			

	def uart_settings_get(self):
		st_list=[]
		eol='\r\n'
		for st in self.uart_settings_list:
			if st==self.ui.port_edit or st==self.ui.baud_edit:
				st_list.append(str(st.toPlainText())+eol)
				#print"edit"
			else:
				st_list.append(str(st.currentText())+eol)
				#print"cb"
		return st_list			

	def save_dump_file(self,name,data1,data2):
		eol='\r\n'
		if(not os.path.isfile(name)):
			try:
				new_file = open(name, 'w')
			except IOError as e:
				print(u'не удалось открыть файл')
				print e
			else:
				with new_file:	
					#wr_data=[d1+' '+str(data2[idx])+eol for idx,d1 in enumerate(str(data1))]
					wr_data=[str(d1)+' '+str(data2[idx])+eol for idx,d1 in enumerate(data1)]
					new_file.writelines(wr_data)
					new_file.close()				

	def save_settings_uart(self):
		try:
			settings_file = open('.settings', 'w')
		except IOError as e:
			print(u'не удалось открыть файл')
		else:
			with settings_file:
				#print"st list",self.uart_settings_get
				list1=self.uart_settings_get()
				#print"st list",list1
				settings_file.writelines(list1)
				settings_file.close()
				QtGui.QMessageBox.information(QWidget(), u"Инфо", u"Сохранено")
						

	def eventFilter(self, source, event):

		if event.type() == QtCore.QEvent.MouseMove:	
			if event.buttons() == QtCore.Qt.NoButton:
				pos = event.pos()
				if(source==self.plt1_ch1):
					self.edit_x1.setText('%.3f' % (self.plt1_ch1.xAxis.pixelToCoord(pos.x())))
					self.edit_y1.setText('%.4f' % (self.plt1_ch1.yAxis.pixelToCoord(pos.y())))
				elif(source==self.plt2_ch1):
					self.edit_x1.setText('%.3f' % (self.plt2_ch1.xAxis.pixelToCoord(pos.x())))
					self.edit_y1.setText('%.4f' % (self.plt2_ch1.yAxis.pixelToCoord(pos.y())))	
				elif(source==self.plt1_ch2):
					self.edit_x2.setText('%.3f' % (self.plt1_ch2.xAxis.pixelToCoord(pos.x())))
					self.edit_y2.setText('%.4f' % (self.plt1_ch2.yAxis.pixelToCoord(pos.y())))							
				elif(source==self.plt2_ch2):
					self.edit_x2.setText('%.3f' % (self.plt2_ch2.xAxis.pixelToCoord(pos.x())))
					self.edit_y2.setText('%.4f' % (self.plt2_ch2.yAxis.pixelToCoord(pos.y())))	
			
		elif event.type() == QtCore.QEvent.MouseButtonPress and event.button() & QtCore.Qt.RightButton:			
			pos = event.pos()
			menu = QtGui.QMenu()
			menu.addAction(u'сохранить как jpg', lambda:self.save_jpg(source))
			menu.addAction(u'сохранить как png', lambda:self.save_png(source))
			menu.addAction(u'сохранить как bmp', lambda:self.save_bmp(source))
		
			menu.exec_(QtGui.QCursor.pos())
			
		#return QtGui.QMainWindow.eventFilter(self, source, event)	
		return QtGui.QWidget.eventFilter(self, source, event)

	def msg_save_image(self,path):
		QtGui.QMessageBox.information(QWidget(), u"Инфо", u"Сохранено в: "+path)
		

	def save_img(self,name,objects,tp):
		
		try:
			if tp=='jpg':
				objects.saveJpg(name+'.jpg')
			elif tp=='png':
				objects.savePng(name+'.png')	
			elif tp=='bmp':	
				objects.saveBmp(name+'.bmp')
		except OSError as e:
			print e	
		else:
			self.msg_save_image(name+'.'+tp)	

	def save_img_proc(self,objects,tp):
		now=datetime.datetime.now()
		if(objects==self.plt1_ch1 or objects==self.plt2_ch1):
			if(os.path.exists('graph/ch1/')):
				if(objects==self.plt1_ch1):
					self.save_img('graph/ch1/ampl_'+now.strftime("%d-%m-%y-%H-%M-%S"),objects,tp)
				elif(objects==self.plt2_ch1):
					self.save_img('graph/ch1/freq_'+now.strftime("%d-%m-%y-%H-%M-%S"),objects,tp)	
			else:
				self.creat_dir('graph/ch1/')
				if(objects==self.plt1_ch1):
					
					self.save_img('graph/ch1/ampl_'+now.strftime("%d-%m-%y-%H-%M-%S"),objects,tp)
				elif(objects==self.plt2_ch1):
					self.save_img('graph/ch1/freq_'+now.strftime("%d-%m-%y-%H-%M-%S"),objects,tp)	

		if(objects==self.plt1_ch2 or objects==self.plt2_ch2):
			if(os.path.exists('graph/ch2/')):
				if(objects==self.plt1_ch2):
					self.save_img('graph/ch2/ampl_'+now.strftime("%d-%m-%y-%H-%M-%S"),objects,tp)
				elif(objects==self.plt2_ch2):
					self.save_img('graph/ch2/freq_'+now.strftime("%d-%m-%y-%H-%M-%S"),objects,tp)	
			else:
				self.creat_dir('graph/ch2/')
				if(objects==self.plt1_ch2):
					
					self.save_img('graph/ch2/ampl_'+now.strftime("%d-%m-%y-%H-%M-%S"),objects,tp)
				elif(objects==self.plt2_ch2):
					self.save_img('graph/ch2/freq_'+now.strftime("%d-%m-%y-%H-%M-%S"),objects,tp)			


	def save_jpg(self, objects):
		self.save_img_proc(objects,'jpg')

	def save_png(self, objects):	
		self.save_img_proc(objects,'png')

	def save_bmp(self, objects):	
		self.save_img_proc(objects,'bmp')

	def fstart1_changed(self,i):
		self.d_from_1 = i

		if self.fstart_comb1.count()>1 and self.fend_comb1.count()>1 and self.d_to_1>self.d_from_1:
			if not self.cont_cb.isChecked():
				try:
					self.plt2_ch1=self.replot_graph(self.plt2_ch1,self.xf1[self.d_from_1:self.d_to_1],self.yf1[self.d_from_1:self.d_to_1])
	
				except:
					QtGui.QMessageBox.information(QWidget(), "Warning", u"Дамп не загружен. Загрузите дамп")
					#print"data not loaded"	
					
	def fend1_changed(self,i):
		self.d_to_1 = i

				
		if self.fstart_comb1.count()>1 and self.fend_comb1.count()>1 and self.d_to_1>self.d_from_1:	
			if not self.cont_cb.isChecked():
				try:
					self.plt2_ch1=self.replot_graph(self.plt2_ch1,self.xf1[self.d_from_1:self.d_to_1],self.yf1[self.d_from_1:self.d_to_1])
				except:
					QtGui.QMessageBox.information(QWidget(), "Warning", u"Дамп не загружен. Загрузите дамп")
					#print"data not loaded"


	def fstart2_changed(self,i):
		self.d_from_2 = i

		if self.fstart_comb2.count()>1 and self.fend_comb2.count()>1 and self.d_to_2>self.d_from_2:
			if not self.cont_cb.isChecked():
				try:
					self.plt2_ch2=self.replot_graph(self.plt2_ch2,self.xf2[self.d_from_2:self.d_to_2],self.yf2[self.d_from_2:self.d_to_2])
	
				except:
					QtGui.QMessageBox.information(QWidget(), "Warning", u"Дамп не загружен. Загрузите дамп")
					#print"data not loaded"	
					
	def fend2_changed(self,i):
		self.d_to_2 = i

				
		if self.fstart_comb2.count()>1 and self.fend_comb2.count()>1 and self.d_to_2>self.d_from_2:	
			if not self.cont_cb.isChecked():
				try:
					self.plt2_ch2=self.replot_graph(self.plt2_ch2,self.xf2[self.d_from_2:self.d_to_2],self.yf2[self.d_from_2:self.d_to_2])
				except:
					QtGui.QMessageBox.information(QWidget(), "Warning", u"Дамп не загружен. Загрузите дамп")

	def init_graph(self,plt,tp,color,xmin,xmax,ymin,ymax):
			
		plt.clearGraphs();
		plt.addGraph()
		#x_data = range(1000)
		#y_data = [np.sin(x*2*np.pi/1000) for x in x_data]		
		#plt.graph(0).setData(x_data, y_data)
		#plt.graph(0).setPen(QColor(Qt.red))
		plt.graph(0).setPen(QColor(color))

		#Подписываем оси Ox и Oy
		if tp=='time':
			plt.xAxis.setLabel("t,c")
			plt.yAxis.setLabel("I,A")
		elif tp=='freq':
			plt.xAxis.setLabel("f,kHz")
			plt.yAxis.setLabel("P,dBm")	

		plt.xAxis.setRange(xmin,xmax)
		plt.yAxis.setRange(ymin,ymax)
		plt.replot()

		return plt

	def replot_graph(self,plt,x_data,y_data):	
		plt.graph(0).setData(x_data, y_data)
		plt.xAxis.setRange(np.min(x_data),np.max(x_data))
		plt.yAxis.setRange(np.min(y_data),np.max(y_data))
		plt.replot()

		return plt


	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)  
		#QtGui.QWidget.updateGeometry(screen) 

	def closeEvent(self, event):
		# Переопределить colseEvent
		#global stop_thrd1
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
				#stop_thrd1=True

				#self.t1.wait()
				if type(event)==bool:
					app.quit()
				else:	
					event.accept()

			else:
				if type(event)!=bool:
					event.ignore()
	def delete_dir(self,path):
		if(os.path.exists(path)):
			try:
				shutil.rmtree(path)
			except OSError as e:
				print ("Error: %s - %s." % (e.filename, e.strerror))
	
	def delete_file(self,path):
		if os.path.isfile(path):
			try:
				os.remove(path)
			except OSError as e:
				print ("Error: %s - %s." % (e.filename, e.strerror))
				

	def clean_uart(self):
		reply = QtGui.QMessageBox.question\
			(self, u'Информация',
				u"Вы уверены, что хотите удалить все настройки ЮАРТ?",
				 QtGui.QMessageBox.Yes,
				 QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			self.delete_file(".settings")

	def clean2_all(self):
		reply = QtGui.QMessageBox.question\
		(self, u'Информация',
			u"Вы уверены, что хотите удалить все данные канала 2?",
			 QtGui.QMessageBox.Yes,
			 QtGui.QMessageBox.No)	

		if reply == QtGui.QMessageBox.Yes:	
			self.delete_dir('measure/ch2/')		
			self.wr_2.setChecked(False)
	
	def clean2_today(self):
		reply = QtGui.QMessageBox.question\
		(self, u'Информация',
			u"Вы уверены, что хотите удалить данные за сегодня c канала 2?",
			 QtGui.QMessageBox.Yes,
			 QtGui.QMessageBox.No)	

		if reply == QtGui.QMessageBox.Yes:	
			now = datetime.datetime.now()
			self.delete_dir('measure/ch2/'+now.strftime("%d-%m-%Y"))	
			self.wr_2.setChecked(False)
	
	def clean1_all(self):
		reply = QtGui.QMessageBox.question\
		(self, u'Информация',
			u"Вы уверены, что хотите удалить все данные канала 1?",
			 QtGui.QMessageBox.Yes,
			 QtGui.QMessageBox.No)	

		if reply == QtGui.QMessageBox.Yes:	
			self.delete_dir('measure/ch1/')
			self.wr_1.setChecked(False)		
	
	def clean1_today(self):
		reply = QtGui.QMessageBox.question\
		(self, u'Информация',
			u"Вы уверены, что хотите удалить данные за сегодня c канала 1?",
			 QtGui.QMessageBox.Yes,
			 QtGui.QMessageBox.No)	

		if reply == QtGui.QMessageBox.Yes:	
			now = datetime.datetime.now()
			self.delete_dir('measure/ch1/'+now.strftime("%d-%m-%Y"))
			self.wr_1.setChecked(False)		 			

	def clean1_2_today(self):
		reply = QtGui.QMessageBox.question\
		(self, u'Информация',
			u"Вы уверены, что хотите удалить данные за сегодня со всех каналов?",
			 QtGui.QMessageBox.Yes,
			 QtGui.QMessageBox.No)	

		if reply == QtGui.QMessageBox.Yes:	
			now = datetime.datetime.now()
			
			self.delete_dir('measure/ch1/'+now.strftime("%d-%m-%Y"))
			self.delete_dir('measure/ch2/'+now.strftime("%d-%m-%Y"))	
			self.wr_1.setChecked(False)
			self.wr_2.setChecked(False)	
			self.wr_all.setChecked(False)

	def clean1_2_all(self):
		reply = QtGui.QMessageBox.question\
		(self, u'Информация',
			u"Вы уверены, что хотите удалить все данные со всех каналов?",
			 QtGui.QMessageBox.Yes,
			 QtGui.QMessageBox.No)	

		if reply == QtGui.QMessageBox.Yes:	
			self.delete_dir('measure/ch1/')
			self.delete_dir('measure/ch2/')
			self.wr_1.setChecked(False)
			self.wr_2.setChecked(False)	
			self.wr_all.setChecked(False)

	def clean_all(self):
		reply = QtGui.QMessageBox.question\
			(self, u'Информация',
				u"Вы уверены, что хотите провести полную очистку?",
				 QtGui.QMessageBox.Yes,
				 QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			self.delete_file(".settings")
			self.delete_dir('measure')
			self.delete_dir('graph')
			self.wr_1.setChecked(False)
			self.wr_2.setChecked(False)	
			self.wr_all.setChecked(False)
					


	def load_dump(self):
		#global stop_thrd1
		self.cmd="msr start f1m1"
		print"loading dump..."	
		#stop_thrd1=True
		#self.t1.start()
		self.write_byte(self.cmd)

	def rst(self):
		self.cmd="rst f1m1"
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
				
				#print "s_start.group",s_start.group()
				#print "self.read_str",self.read_str
				self.start_flg=True

			if(s_stop):

				self.start_flg=False
				stop_thrd1=True

				#print "s_stop.group()",s_stop.group()
				##print "self.read_str",self.read_str
				#print "len buff",len(self.read_buff)
				#print "len str",len(self.read_buff[0])
				print self.read_buff

				split_buff=[self.read_buff[0][x:x+4] for x in range (4, len(self.read_buff[0])-4, 4)]
				print split_buff
				self.ch1_list=[]
				self.ch2_list=[]
				for indx,ch in enumerate(split_buff):
					if not indx%2:
						self.ch2_list.append(float(np.int16(int((ch[2]+ch[3]+ch[0]+ch[1]),base=16)))*kt)
						
					else:
						self.ch1_list.append(float(np.int16(int((ch[2]+ch[3]+ch[0]+ch[1]),base=16)))*kt)
						
						
						

				print "len ch1",len(self.ch1_list)
				print "len ch2",len(self.ch2_list)

				print "ch1",self.ch1_list
				print "ch2",self.ch2_list

				#self.plt1_ch1.clearGraphs();
				#self.plt1_ch1.addGraph()
				if(len(self.ch1_list)==dump_size):
					#x_ch1 = range(0,len(self.ch1_list))
					x_ch1 = map(lambda x: x*(0.02/167), range(0,len(self.ch1_list)))
					#y_ch1 = self.ch1_list	
	
					self.plt1_ch1=self.replot_graph(self.plt1_ch1,x_ch1,self.ch1_list)	
					self.plt1_ch2=self.replot_graph(self.plt1_ch2,x_ch1,self.ch2_list)
	
	
					self.Pmax1,self.f01,self.xf1,self.yf1=self.FFT(self.ch1_list)

					if self.fstart_comb1.count()>1 and self.fend_comb1.count()>1 and self.d_to_1>self.d_from_1:
						self.plt2_ch1=self.replot_graph(self.plt2_ch1,self.xf1[self.d_from_1:self.d_to_1],self.yf1[self.d_from_1:self.d_to_1])

					self.lcd_f0_1.display(self.f01)
					self.lcd_f0_1.repaint()

					self.lcd_p1.display(self.Pmax1)
					self.lcd_p1.repaint()
	
	
	
					self.Pmax2,self.f02,self.xf2,self.yf2=self.FFT(self.ch2_list)

					if self.fstart_comb2.count()>1 and self.fend_comb2.count()>1 and self.d_to_2>self.d_from_2:
						self.plt2_ch2=self.replot_graph(self.plt2_ch2,self.xf2[self.d_from_2:self.d_to_2],self.yf2[self.d_from_2:self.d_to_2])

					self.lcd_f0_2.display(self.f02)
					self.lcd_f0_2.repaint()

					self.lcd_p2.display(self.Pmax2)
					self.lcd_p2.repaint()

					if(self.wr_1.isChecked()):
						now=datetime.datetime.now()

						datapath1_ampl='measure/ch1/'+now.strftime("%d-%m-%Y")+'/ampl/'
						datapath1_freq='measure/ch1/'+now.strftime("%d-%m-%Y")+'/freq/'

						name_ampl=datapath1_ampl+'ch1_ampl_'+now.strftime("%d-%m-%y-%H-%M-%S")
						name_freq=datapath1_freq+'ch1_freq_'+now.strftime("%d-%m-%y-%H-%M-%S")
						
						self.save_dump_file(name_ampl,self.ch1_list,x_ch1)
						self.save_dump_file(name_freq,self.yf1,self.xf1)

					if(self.wr_2.isChecked()):
						now=datetime.datetime.now()

						datapath2_ampl='measure/ch2/'+now.strftime("%d-%m-%Y")+'/ampl/'
						datapath2_freq='measure/ch2/'+now.strftime("%d-%m-%Y")+'/freq/'

						name_ampl=datapath2_ampl+'ch2_ampl_'+now.strftime("%d-%m-%y-%H-%M-%S")
						name_freq=datapath2_freq+'ch2_freq_'+now.strftime("%d-%m-%y-%H-%M-%S")
						
						self.save_dump_file(name_ampl,self.ch2_list,x_ch1)
						self.save_dump_file(name_freq,self.yf2,self.xf2)
				#self.a1.appendleft(sample[0])
				#datatoplot = self.a1.pop()



				#self.t1.quit()
				if self.cont_cb.isChecked():
					self.write_byte("msr start f1m1")
				else:	
					self.write_byte("msr stop f1m1")

			if(not self.start_flg):
				print self.read_str

			if(self.start_flg and not s_start):	
				self.read_buff.append(binascii.hexlify(self.read_str))	

	def FFT(self,signal):

		# signal.append(sigval * 0.000122)

		#signal = []	 #список для реального сигнала
		sig = []		#реальный сигнал
		fft_w_m = []		#fft list without max element	

		freqs = map(lambda x: (x*8.0/len(signal)), range(0,len(signal)/2,1))


		aver = reduce(lambda x, y: x + y, signal) / len(signal)

		#aver = np.mean(freqs)

		sig.extend(signal)

		signal[:] = [x - aver for x in signal]

		window = np.hamming(len(signal))
		signal = np.array(signal)
		signal = np.multiply(signal, window)

		FFT = abs(scipy.fft(signal)) / ((len(signal) / 2.0) * 0.54)

		fft = 20.0 * scipy.log10(FFT)

		first = np.max(fft[:len(signal)/2])

		#first_idx = first.argmax()
		#freq_f0 = first.argmax()

		first_idx = self.idx(fft[:len(signal)/2], first)

		#freq_f0   = self.idx(fft[:len(signal)/2], first)
		freq_f0=freqs[first_idx]*1000
		Pmax=fft[first_idx]

		print"first {},first_idx {}, freq_f0 {}".format(first,first_idx,freq_f0)

		xf,yf = freqs,fft[:len(fft)//2]
		return Pmax,freq_f0,xf,list(yf)

#index of item in scipy array
	def idx(self,array, item):
		return np.where(array == item)[0][0]

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	MyForm().show()

	sys.exit(app.exec_()) 


		