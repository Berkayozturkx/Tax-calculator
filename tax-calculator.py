#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Vergi Hesaplayıcı")
        grid = QGridLayout()
        grid.addWidget(QLabel("Fiyat Giriniz:"),2,0)
        grid.addWidget(QLabel("Oran:"),3,0)
        
        #LineEdit
        self.fiyat = QLineEdit()
        grid.addWidget(self.fiyat,2,1,1,3)
        
        #RadioButtons
        self.oranlar = QButtonGroup()
        self.oran1 = QRadioButton("%18")
        self.oran2 = QRadioButton("%08")
        self.oran3 = QRadioButton("%01")
        self.oranlar.addButton(self.oran1)
        self.oranlar.addButton(self.oran2)
        self.oranlar.addButton(self.oran3)
        
        grid.addWidget(self.oran1,3,1)
        grid.addWidget(self.oran2,4,1)
        grid.addWidget(self.oran3,5,1)
        
        #Labels
        self.kdv = QLabel("")
        self.kdvliFiyat = QLabel("")
        self.yaziAlani = QLabel("")
        
        grid.addWidget(self.kdv,8,1)
        grid.addWidget(self.kdvliFiyat,9,1)
        grid.addWidget(self.yaziAlani,10,1)
        
        
        #PushButton
        self.buton = QPushButton("Hesapla")
        self.buton.clicked.connect(lambda: self.hesapla(self.yaziAlani,self.kdv,self.kdvliFiyat,self.oran1.isChecked(),self.oran2.isChecked(),self.oran3.isChecked()))
        grid.addWidget(self.buton,6,1,1,3)
        
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(grid)
        h_box.addStretch()
        
        
        self.setGeometry(300,300,300,150)
        self.setLayout(h_box)
        self.show()
        
    def hesapla(self,yaziAlani,kdv,kdvliFiyat,oran1,oran2,oran3):
        fiyat = 0
        try: fiyat = int(self.fiyat.text())
        except: pass
        
        if (fiyat > 0):
            if(oran1):
                oran = 0.18
                kdv = fiyat*oran
                kdvliFiyat = kdv + fiyat
                self.kdv.setText("Kdv: {}".format(kdv))
                self.kdvliFiyat.setText("Kdv dahil fiyat: {}".format(kdvliFiyat))
                self.yaziAlani.setText("")
            elif(oran2):
                oran = 0.08
                kdv = fiyat*oran
                kdvliFiyat = kdv + fiyat
                self.kdv.setText("Kdv: {}".format(kdv))
                self.kdvliFiyat.setText("Kdv dahil fiyat: {}".format(kdvliFiyat))
                self.yaziAlani.setText("")
            else:
                oran = 0.01
                kdv = fiyat*oran
                kdvliFiyat = kdv + fiyat
                self.kdv.setText("Kdv: {}".format(kdv))
                self.kdvliFiyat.setText("Kdv dahil fiyat: {}".format(kdvliFiyat))
                self.yaziAlani.setText("")
        elif (fiyat <= 0):
            self.kdv.setText("")
            self.kdvliFiyat.setText("")
            self.yaziAlani.setText("Lütfen pozitif bir sayı giriniz")
        else:
            self.yaziAlani.setText("Hatalı giriş yaptınız.")
        
uygulama = QApplication(sys.argv)
pencere = MainWindow()
sys.exit(uygulama.exec_())


# In[ ]:




