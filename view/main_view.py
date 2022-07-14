# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_version.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from controller.table_widget_contoller import set_column_names
from controller.start_button_controller import run_sniffing_in_thread
from controller.stop_button_controller import stop_sniffing_thread
from controller.show_info_button_controller import show_info_according_to_selected_row
from controller.clear_table_widget_button_controller import clear_table_widget
from controller.apply_button_controller import search_in_table_widget
from controller.clear_text_edit_button_controller import clear_text_edit
from controller.clear_list_widget_button_controller import clear_list_widget
from controller.sniffing import save_info
from controller.save_as_action_controller import save_as_pcap_files
from controller.save_action_controller import save_pcap_file


class Ui_MainWindow(object):
    NUMBER_OF_TABLE_WIDGET_COLUMN = 5
    COLUMN_NAMES = ['No.', 'IP Version', 'Source', 'Destination', 'Protocol']

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 836)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 430, 1001, 261))
        self.listWidget.setObjectName("listWidget")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(70, 720, 93, 28))
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(180, 720, 93, 28))
        self.stop_btn.setObjectName("stop_btn")
        self.show_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_btn.setGeometry(QtCore.QRect(290, 720, 93, 28))
        self.show_btn.setObjectName('show_btn')
        self.clear_table_widget_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_table_widget_btn.setGeometry(QtCore.QRect(400, 720, 93, 28))
        self.clear_table_widget_btn.setObjectName('clear_table_widget_btn')

        self.apply_btn = QtWidgets.QPushButton(self.centralwidget)
        self.apply_btn.setGeometry(QtCore.QRect(690, 20, 93, 28))
        self.apply_btn.setObjectName("apply_btn")

        self.clear_list_widget_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_list_widget_btn.setGeometry(QtCore.QRect(510, 720, 93, 28))
        self.clear_list_widget_btn.setObjectName("clear_list_widget_btn")

        self.clear_text_edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_text_edit_btn.setGeometry(QtCore.QRect(800, 20, 93, 28))
        self.clear_text_edit_btn.setObjectName("clear_text_edit_btn")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(430, 20, 231, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("Filter...")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 70, 1001, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        # --------------------------------------label
        self.status_label = QLabel(self.centralwidget)
        self.status_label.move(70, 760)
        self.status_label.setText('Stopped')
        self.status_label.setStyleSheet('color: red')
        # create shortcut
        self.actionsave.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_S))

        # buttons action
        self.start_btn.clicked.connect(self.start_btn_action)
        self.stop_btn.clicked.connect(self.stop_btn_action)
        self.show_btn.clicked.connect(self.show_btn_action)
        self.clear_table_widget_btn.clicked.connect(self.clear_table_widget_btn_action)
        self.apply_btn.clicked.connect(self.apply_btn_action)
        self.clear_text_edit_btn.clicked.connect(self.clear_text_edit_btn_action)
        self.clear_list_widget_btn.clicked.connect(self.clear_list_widget_btn_action)
        # menubar actions
        self.actionSave_As.triggered.connect(self.save_as_action)
        self.actionsave.triggered.connect(self.save_action)

        self.file_name = None
        # make this program responsive
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit.setMaximumSize(QtCore.QSize(231, 30))
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 6)
        self.gridLayout.addWidget(self.listWidget, 4, 0, 1, 6)
        self.gridLayout.addWidget(self.textEdit, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.apply_btn, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.clear_text_edit_btn, 0, 5, 1, 1)
        self.gridLayout.addWidget(self.start_btn, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.stop_btn, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.show_btn, 5, 2, 1, 1)
        self.gridLayout.addWidget(self.clear_table_widget_btn, 5, 3, 1, 1)
        self.gridLayout.addWidget(self.clear_list_widget_btn, 5, 4, 1, 1)
        self.gridLayout.addWidget(self.status_label, 6, 0, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # table widget settings
        self.tableWidget.setColumnCount(self.NUMBER_OF_TABLE_WIDGET_COLUMN)

        set_column_names(self.tableWidget, self.COLUMN_NAMES)

    def start_btn_action(self):
        run_sniffing_in_thread(self.status_label, self.tableWidget)

    def stop_btn_action(self):
        stop_sniffing_thread(self.status_label)

    def show_btn_action(self):
        show_info_according_to_selected_row(self.tableWidget.currentRow(), self.listWidget)

    def clear_table_widget_btn_action(self):
        clear_table_widget(self.tableWidget)

    def apply_btn_action(self):
        search_in_table_widget(self.tableWidget, self.textEdit, self.COLUMN_NAMES)

    def clear_text_edit_btn_action(self):
        clear_text_edit(self.tableWidget, self.textEdit)

    def clear_list_widget_btn_action(self):
        clear_list_widget(self.listWidget)

    def save_action(self):
        self.file_name = save_pcap_file(self.file_name)

    def save_as_action(self):
        self.file_name = save_as_pcap_files()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.show_btn.setText(_translate("MainWindow", "Show More Info"))
        self.show_btn.adjustSize()
        self.clear_table_widget_btn.setText(_translate("MainWindow", "Clear Table"))
        self.clear_list_widget_btn.setText(_translate("MainWindow", "Clear Info"))
        self.apply_btn.setText(_translate("MainWindow", "Apply"))
        self.clear_text_edit_btn.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionopen.setText(_translate("MainWindow", "Open"))
        self.actionsave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
