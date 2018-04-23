# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import googlemaps
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

from src import Valuation


class App(QtWidgets.QWidget):
    gmaps = None
    valuation = None
    latitude = None
    longitude = None

    def __init__(self):
        super().__init__()
        self.gmaps = googlemaps.Client(
            key='AIzaSyAWPy2RuBxzziKOgEDLXa2LrXakMIHlBpY')
        self.valuation = Valuation.Valuation()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Główne okno")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 491, 81))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget. \
            setGeometry(QtCore.QRect(20, 130, 381, 161))
        self.horizontalLayoutWidget. \
            setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_postalCode = QtWidgets.QLineEdit(
            self.horizontalLayoutWidget)
        self.lineEdit_postalCode.setObjectName("lineEdit_postalCode")
        self.verticalLayout.addWidget(self.lineEdit_postalCode)
        self.lineEdit_city = \
            QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.verticalLayout.addWidget(self.lineEdit_city)
        self.lineEdit_street = \
            QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.verticalLayout.addWidget(self.lineEdit_street)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pushButton_calculate_geographical = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButton_calculate_geographical. \
            setGeometry(QtCore.QRect(20, 300, 381, 21))
        self.pushButton_calculate_geographical. \
            setObjectName("pushButton_calculate_geographical")
        self.pushButton_calculate_geographical. \
            clicked.connect(self.buttonCalculateGeographical_onClick)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 100, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(20, 390, 381, 161))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_squareMeters = QtWidgets.QLineEdit(
            self.horizontalLayoutWidget_2)
        self.lineEdit_squareMeters.setObjectName("lineEdit_squareMeters")
        self.verticalLayout_6.addWidget(self.lineEdit_squareMeters)
        self.lineEdit_productionYear = QtWidgets.QLineEdit(
            self.horizontalLayoutWidget_2)
        self.lineEdit_productionYear.setObjectName("lineEdit_productionYear")
        self.verticalLayout_6.addWidget(self.lineEdit_productionYear)
        self.comboBox_market = QtWidgets.QComboBox(
            self.horizontalLayoutWidget_2)
        self.comboBox_market.setObjectName("comboBox_market")
        self.comboBox_market.addItems(["wtórny", "pierwotny"])
        self.verticalLayout_6.addWidget(self.comboBox_market)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3. \
            setGeometry(QtCore.QRect(410, 130, 381, 331))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBox_balcony = QtWidgets. \
            QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_balcony.setObjectName("checkBox_balcony")
        self.verticalLayout_8.addWidget(self.checkBox_balcony)
        self.checkBox_usableRoom = QtWidgets. \
            QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_usableRoom.setObjectName("checkBox_usableRoom")
        self.verticalLayout_8.addWidget(self.checkBox_usableRoom)
        self.checkBox_garage = QtWidgets.QCheckBox(
            self.horizontalLayoutWidget_3)
        self.checkBox_garage.setObjectName("checkBox_garage")
        self.verticalLayout_8.addWidget(self.checkBox_garage)
        self.checkBox_cellar = QtWidgets. \
            QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_cellar.setObjectName("checkBox_cellar")
        self.verticalLayout_8.addWidget(self.checkBox_cellar)
        self.checkBox_patio = QtWidgets. \
            QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_patio.setObjectName("checkBox_patio")
        self.verticalLayout_8.addWidget(self.checkBox_patio)
        self.checkBox_elevator = QtWidgets.QCheckBox(
            self.horizontalLayoutWidget_3)
        self.checkBox_elevator.setObjectName("checkBox_elevator")
        self.verticalLayout_8.addWidget(self.checkBox_elevator)
        self.checkBox_twoFloors = QtWidgets.QCheckBox(
            self.horizontalLayoutWidget_3)
        self.checkBox_twoFloors.setObjectName("checkBox_twoFloors")
        self.verticalLayout_8.addWidget(self.checkBox_twoFloors)
        self.checkBox_airConditioning = QtWidgets.QCheckBox(
            self.horizontalLayoutWidget_3)
        self.checkBox_airConditioning.setObjectName("checkBox_airConditioning")
        self.verticalLayout_8.addWidget(self.checkBox_airConditioning)
        self.checkBox_garden = QtWidgets.QCheckBox(
            self.horizontalLayoutWidget_3)
        self.checkBox_garden.setObjectName("checkBox_garden")
        self.verticalLayout_8.addWidget(self.checkBox_garden)
        self.checkBox_furnished = QtWidgets.QCheckBox(
            self.horizontalLayoutWidget_3)
        self.checkBox_furnished.setObjectName("checkBox_furnished")
        self.verticalLayout_8.addWidget(self.checkBox_furnished)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(100, 360, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(450, 510, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(550, 510, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(810, 300, 351, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_calculatePrice = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButton_calculatePrice.setGeometry(
            QtCore.QRect(410, 470, 371, 25))
        self.pushButton_calculatePrice.setObjectName(
            "pushButton_calculatePrice")
        self.pushButton_calculatePrice.clicked.connect(
            self.buttonCalculatePrice_onClick)
        self.pushButton_calculatePrice.setDisabled(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Wycena nieruchomości"))
        self.label_3.setText(_translate("MainWindow", "Kod pocztowy:"))
        self.label_4.setText(_translate("MainWindow", "Miasto:"))
        self.label_2.setText(_translate("MainWindow", "Ulica:"))
        self.pushButton_calculate_geographical.setText(
            _translate("MainWindow", "oblicz polożenie geograficzne"))
        self.label_5.setText(
            _translate("MainWindow", "Lokalizacja mieszkania"))
        self.label_6.setText(_translate("MainWindow", "metry kwadrat."))
        self.label_9.setText(_translate("MainWindow", "rok budowy"))
        self.label_7.setText(_translate("MainWindow", "Market"))
        self.checkBox_balcony.setText(_translate("MainWindow", "balkon"))
        self.checkBox_usableRoom.setText(
            _translate("MainWindow", "pom.użytkowe"))
        self.checkBox_garage.setText(_translate("MainWindow", "garaż"))
        self.checkBox_cellar.setText(_translate("MainWindow", "piwnica"))
        self.checkBox_patio.setText(_translate("MainWindow", "taras"))
        self.checkBox_elevator.setText(_translate("MainWindow", "winda"))
        self.checkBox_twoFloors.setText(
            _translate("MainWindow", "dwupoziomowe"))
        self.checkBox_airConditioning.setText(
            _translate("MainWindow", "klimatyzacja"))
        self.checkBox_garden.setText(_translate("MainWindow", "ogród"))
        self.checkBox_furnished.setText(_translate("MainWindow", "umeblowane"))
        self.label_12.setText(_translate("MainWindow", "Parametry mieszkania"))
        self.label_13.setText(_translate("MainWindow", "Cena:"))
        self.label_14.setText(_translate("MainWindow", "---"))
        self.label_8.setText(
            _translate("MainWindow", "Informacje dodatkowe o mieszkaniu"))
        self.pushButton_calculatePrice.setText(
            _translate("MainWindow", "oblicz cenę mieszkania"))

    def find_city(self, geocode_result):
        addressType = None
        print(geocode_result['address_components'][0])
        for i in range(0, len(geocode_result['address_components'])):
            for x in geocode_result['address_components'][i]:
                if (x == "long_name"):
                    locality = geocode_result[
                        'address_components'][i]['long_name']
                    if self.valuation.list_Of_available_cities.__contains__(locality):
                        self.lineEdit_city.setText(locality)
                        self.pushButton_calculatePrice.setDisabled(False)

    @pyqtSlot()
    def buttonCalculateGeographical_onClick(self):
        print(self.lineEdit_postalCode.text())

        geocode_result = self.gmaps.geocode(
            'Poland ' + self.lineEdit_postalCode.text())[0]
        self.latitude = geocode_result['geometry']['location']['lat']
        self.longitude = geocode_result['geometry']['location']['lng']
        self.find_city(geocode_result)

    @pyqtSlot()
    def buttonCalculatePrice_onClick(self):
        price = self.valuation.estimate_cost_of_the_flat(
            self.latitude, self.longitude,
            float(
                self.lineEdit_squareMeters.text(
                )),
            self.lineEdit_city.text(
            ),
            int(self.lineEdit_productionYear.text(
            )),
            self.checkBox_furnished.isChecked(
            ),
            self.checkBox_balcony.isChecked(
            ),
            self.checkBox_usableRoom, self.checkBox_garage.isChecked(
            ),
            self.checkBox_cellar.isChecked(
            ),
            self.checkBox_garage.isChecked(
            ),
            self.checkBox_patio.isChecked(
            ),
            self.checkBox_elevator.isChecked(
            ),
            self.checkBox_twoFloors.isChecked(
            ),
            self.checkBox_airConditioning.isChecked(
            ),
            self.comboBox_market.currentText(
            )
        )
        self.label_14.setText(str(price))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
