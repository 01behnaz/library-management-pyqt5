

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *
import pymysql


my_connection = pymysql.connect(
    host='localhost',
    user='root',
    password='your password',
    database='your database')
print("ok")

my_cursor = my_connection.cursor()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName('Dialog')
        Dialog.resize(591, 450)
        Dialog.setWindowIcon(QIcon('icons8-library-100.png'))
        self.myTabs = QtWidgets.QTabWidget(Dialog)
        self.myTabs.setGeometry(QtCore.QRect(0, 0, 592, 451))
        self.myTabs.setStyleSheet(
            'background-color: rgb(222, 212, 215);'
            "color: rgb(51, 51, 51);\n"
            "font: 8pt \"B Nazanin\";\n")
        self.myTabs.setObjectName('myTab')

        # CREATE TAB HOME
        self.tab_home = QtWidgets.QWidget()
        self.tab_home.setObjectName('tab_home')
        self.groupBox_del = QtWidgets.QGroupBox(self.tab_home)
        self.groupBox_del.setGeometry(QtCore.QRect(70, 10, 442, 101))
        self.groupBox_del.setStyleSheet("background-color: rgb(200, 183, 188);"
                                        "color: rgb(51, 51, 51);\n"
                                        "font: 9pt \"B Nazanin\";\n")
        self.groupBox_del.setObjectName('groupBox_del')
        self.groupBox_del.setTitle('Delete')
        self.label_del = QtWidgets.QLabel(self.groupBox_del)
        self.label_del.setGeometry(QtCore.QRect(
            110, 37, 47, 13))
        self.label_del.setObjectName('label_del')
        self.label_del.setText("Name ")
        self.label_del.setStyleSheet("color: rgb(51, 51, 51);\n"
                                     "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_del = QtWidgets.QLineEdit(self.groupBox_del)
        self.lineEdit_del.setGeometry(QtCore.QRect(160, 30, 148, 25))
        self.lineEdit_del.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "border-radius: 5px;\n"
            "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_del.setObjectName("lineEdit_del")
        self.btn_del = QtWidgets.QPushButton(
            self.groupBox_del, clicked=lambda: self.delete_Book())
        self.btn_del.setGeometry(QtCore.QRect(178, 62, 110, 31))
        self.btn_del.setStyleSheet("background-color: rgb(157, 129, 137);\n"
                                   "color: rgb(51, 51, 51);\n"
                                   "border-radius: 10px;\n"
                                   "font: 11pt \"B Nazanin\";\n")
        self.btn_del.setObjectName('btn_del')
        self.btn_del.setText('Delete')
        self.Book_List = QtWidgets.QGroupBox(self.tab_home)
        self.Book_List.setGeometry(QtCore.QRect(25, 120, 542, 281))
        self.Book_List.setStyleSheet('background-color: rgb(200, 183, 188);'
                                     "color: rgb(51, 51, 51);\n"
                                     "font: 9pt \"B Nazanin\";\n")
        self.Book_List.setObjectName('Book_List')
        self.Book_List.setTitle('Book')
        self.myTable = QtWidgets.QTableWidget(self.Book_List)
        self.myTable.setGeometry(QtCore.QRect(20, 30, 501, 191))
        self.myTable.setStyleSheet(
            'background-color: rgb(255, 255, 255);'
            "color: rgb(51, 51, 51);\n"
            "font: 10pt \"B Nazanin\";\n")
        self.myTable.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.myTable.setObjectName('myTablel')
        self.myTable.setColumnCount(5)
        self.myTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem("Name Book")
        self.myTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("Author Book")
        self.myTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem("Releas Data")
        self.myTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem("Description")
        self.myTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem("Group")
        self.myTable.setHorizontalHeaderItem(4, item)
        self.btn_show_data = QtWidgets.QPushButton(
            self.Book_List, clicked=lambda: self.show_data())
        self.btn_show_data.setGeometry(QtCore.QRect(223, 238, 110, 31))
        self.btn_show_data.setStyleSheet(
            "background-color: rgb(157, 129, 137);\n"
            "color: rgb(51, 51, 51);\n"
            "border-radius: 10px;\n"
            "font: 11pt \"B Nazanin\";\n")
        self.btn_show_data.setObjectName('btn_show_data')
        self.btn_show_data.setText("Show Data")
        self.myTabs.addTab(self.tab_home, "Home")

        # CREATE TAB ADD
        self.tab_add = QtWidgets.QWidget()
        self.tab_add.setObjectName("tab_add")
        self.label_h = QtWidgets.QLabel(self.tab_add)
        self.label_h.setGeometry(QtCore.QRect(225, 30, 145, 35))
        self.label_h.setStyleSheet("background-color: rgb(200, 183, 188);"
                                   "color: rgb(51, 51, 51);\n"
                                   "font: 12pt \"B Nazanin\";\n")
        self.label_h.setObjectName('label_h')
        self.label_h.setText(" Add Your Book Info")
        self.lbl_Add_Name = QtWidgets.QLabel(self.tab_add)
        self.lbl_Add_Name.setGeometry(QtCore.QRect(10, 123, 101, 16))
        self.lbl_Add_Name.setStyleSheet("color: rgb(51, 51, 51);\n"
                                        "font: 10pt \"B Nazanin\";\n")
        self.lbl_Add_Name.setText('Enter Name Book ')
        self.lbl_Add_Name.setObjectName('lbl_Add_Name')
        self.lineEdit_Add_Name = QtWidgets.QLineEdit(self.tab_add)
        self.lineEdit_Add_Name.setGeometry(QtCore.QRect(115, 120, 141, 20))
        self.lineEdit_Add_Name.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "border-radius: 5px;\n"
            "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_Add_Name.setObjectName("lineEdit_Add_Name")
        self.lbl_Add_Author = QtWidgets.QLabel(self.tab_add)
        self.lbl_Add_Author.setGeometry(QtCore.QRect(10, 163, 101, 16))
        self.lbl_Add_Author.setStyleSheet("color: rgb(51, 51, 51);\n"
                                          "font: 10pt \"B Nazanin\";\n")
        self.lbl_Add_Author.setText('Enter Author Book')
        self.lbl_Add_Author.setObjectName('lbl_Add_Author')
        self.lineEdit_Add_Author = QtWidgets.QLineEdit(self.tab_add)
        self.lineEdit_Add_Author.setGeometry(QtCore.QRect(115, 160, 141, 20))
        self.lineEdit_Add_Author.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "border-radius: 5px;\n"
            "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_Add_Author.setObjectName("lineEdit_Add_Author")
        self.lbl_Add_Releas_Data = QtWidgets.QLabel(self.tab_add)
        self.lbl_Add_Releas_Data.setGeometry(QtCore.QRect(10, 203, 101, 20))
        self.lbl_Add_Releas_Data.setStyleSheet("color: rgb(51, 51, 51);\n"
                                               "font: 10pt \"B Nazanin\";\n")
        self.lbl_Add_Releas_Data.setText('Enter Releas Data')
        self.lbl_Add_Releas_Data.setObjectName('lbl_Add_Releas_Data')
        self.lineEdit_Releas_Data = QtWidgets.QLineEdit(self.tab_add)
        self.lineEdit_Releas_Data.setGeometry(QtCore.QRect(115, 200, 141, 20))
        self.lineEdit_Releas_Data.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "border-radius: 5px;\n"
            "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_Releas_Data.setObjectName("lineEdit_Releas_Data")
        self.lbl_group = QtWidgets.QLabel(self.tab_add)
        self.lbl_group.setGeometry(QtCore.QRect(340, 123, 81, 16))
        self.lbl_group.setStyleSheet("color: rgb(51, 51, 51);\n"
                                     "font: 11pt \"B Nazanin\";\n")
        self.lbl_group.setText('Group ')
        self.lbl_group.setObjectName('lbl_group')
        self.check_Iranian = QtWidgets.QCheckBox(self.tab_add)
        self.check_Iranian.setGeometry(QtCore.QRect(340, 145, 70, 17))
        self.check_Iranian.setStyleSheet("color: rgb(51, 51, 51);\n"
                                         "font: 10pt \"B Nazanin\";\n")
        self.check_Iranian.setText('Iranian')
        self.check_Iranian.setObjectName("check_Iranian")
        self.check_Forigen = QtWidgets.QCheckBox(self.tab_add)
        self.check_Forigen.setGeometry(QtCore.QRect(420, 145, 70, 17))
        self.check_Forigen.setStyleSheet("color: rgb(51, 51, 51);\n"
                                         "font: 10pt \"B Nazanin\";\n")
        self.check_Forigen.setText('Forigen')
        self.check_Forigen.setObjectName("check_Foriegn")
        self.lbl_Description = QtWidgets.QLabel(self.tab_add)
        self.lbl_Description.setGeometry(QtCore.QRect(340, 178, 107, 19))
        self.lbl_Description.setStyleSheet("color: rgb(51, 51, 51);\n"
                                           "font: 11pt \"B Nazanin\";\n")
        self.lbl_Description.setText('Description')
        self.lbl_Description.setObjectName('lbl_Description')
        self.lineEdit_Add_Description = QtWidgets.QLineEdit(self.tab_add)
        self.lineEdit_Add_Description.setGeometry(
            QtCore.QRect(340, 200, 150, 65))
        self.lineEdit_Add_Description.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "border-radius: 5px;\n"
            "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_Add_Description.setObjectName("lineEdit_Add_Description")
        self.btn_Add_Book = QtWidgets.QPushButton(
            self.tab_add, clicked=lambda: self.add_Book())
        self.btn_Add_Book.setGeometry(QtCore.QRect(220, 325, 140, 41))
        self.btn_Add_Book.setStyleSheet("background-color: rgb(157, 129, 137);\n"
                                        "color: rgb(51, 51, 51);\n"
                                        "border-radius: 10px;\n"
                                        "font: 11pt \"B Nazanin\";\n")
        self.btn_Add_Book.setObjectName("btn_Add_Book")
        self.btn_Add_Book.setText('Add Book')
        self.myTabs.addTab(self.tab_add, 'Add')

        # CREATE TAB Edit
        self.tab_edit = QtWidgets.QWidget()
        self.tab_edit.setObjectName('tab_edit')
        self.label_he = QtWidgets.QLabel(self.tab_edit)
        self.label_he.setGeometry(QtCore.QRect(225, 30, 104, 35))
        self.label_he.setStyleSheet("background-color: rgb(200, 183, 188);"
                                    "color: rgb(51, 51, 51);\n"
                                    "font: 12pt \"B Nazanin\";\n")
        self.label_he.setObjectName("label_he")
        self.label_he.setText('Edit Book Info')
        self.lbl_Name_for_Edite = QtWidgets.QLabel(self.tab_edit)
        self.lbl_Name_for_Edite.setGeometry(QtCore.QRect(10, 95, 142, 31))
        self.lbl_Name_for_Edite.setText("Enter Name Book For Edit ")
        self.lbl_Name_for_Edite.setStyleSheet("color: rgb(51, 51, 51);\n"
                                              "font: 10pt \"B Nazanin\";\n")
        self.lbl_Name_for_Edite.setObjectName("lbl_Name_for_Edite")
        self.lineEdit_Name_for_search = QtWidgets.QLineEdit(self.tab_edit)
        self.lineEdit_Name_for_search.setGeometry(
            QtCore.QRect(160, 96, 148, 25))
        self.lineEdit_Name_for_search.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "border-radius: 5px;\n"
            "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_Name_for_search.setObjectName("lineEdit_Name_for_search")
        self.btn_Edite_Search = QtWidgets.QPushButton(
            self.tab_edit, clicked=lambda: self.search_Book())
        self.btn_Edite_Search.setGeometry(QtCore.QRect(330, 93, 110, 31))
        self.btn_Edite_Search.setStyleSheet(
            "background-color: rgb(157, 129, 137);\n"
            "color: rgb(51, 51, 51);\n"
            "border-radius: 10px;\n"
            "font: 11pt \"B Nazanin\";\n")
        self.btn_Edite_Search.setObjectName("btn_Edite_Search")
        self.btn_Edite_Search.setText("Search Book")
        self.lbl_Add_Name_2 = QtWidgets.QLabel(self.tab_edit)
        self.lbl_Add_Name_2.setGeometry(QtCore.QRect(10, 160, 111, 16))
        self.lbl_Add_Name_2.setStyleSheet("color: rgb(51, 51, 51);\n"
                                          "font: 10pt \"B Nazanin\";\n")
        self.lbl_Add_Name_2.setText("Enter Name Book")
        self.lineEdit_Edite_Name = QtWidgets.QLineEdit(self.tab_edit)
        self.lineEdit_Edite_Name.setGeometry(QtCore.QRect(115, 155, 141, 20))
        self.lineEdit_Edite_Name.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "border-radius: 5px;\n"
            "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_Edite_Name.setObjectName("lineEdit_Edite_Name")
        self.lbl_Add_Author_2 = QtWidgets.QLabel(self.tab_edit)
        self.lbl_Add_Author_2.setGeometry(QtCore.QRect(10, 200, 101, 16))
        self.lbl_Add_Author_2.setStyleSheet("color: rgb(51, 51, 51);\n"
                                            "font: 10pt \"B Nazanin\";\n")
        self.lbl_Add_Author_2.setText("Enter Author Book")
        self.lbl_Add_Author_2.setObjectName("lbl_Add_Author_2")
        self.lineEdit_Edite_Author = QtWidgets.QLineEdit(self.tab_edit)
        self.lineEdit_Edite_Author.setGeometry(QtCore.QRect(115, 195, 141, 20))
        self.lineEdit_Edite_Author.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "border-radius: 5px;\n"
            "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_Edite_Author.setObjectName("lineEdit_Edite_Author")
        self.lbl_Add_Releas_Data_2 = QtWidgets.QLabel(self.tab_edit)
        self.lbl_Add_Releas_Data_2.setGeometry(QtCore.QRect(10, 240, 101, 20))
        self.lbl_Add_Releas_Data_2.setStyleSheet("color: rgb(51, 51, 51);\n"
                                                 "font: 10pt \"B Nazanin\";\n")
        self.lbl_Add_Releas_Data_2.setText("Enter Releas Data")
        self.lbl_Add_Releas_Data_2.setObjectName("lbl_Add_Releas_Data_2")
        self.lineEdit_Edite_Releas_Data = QtWidgets.QLineEdit(self.tab_edit)
        self.lineEdit_Edite_Releas_Data.setGeometry(
            QtCore.QRect(115, 237, 141, 20))
        self.lineEdit_Edite_Releas_Data.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "border-radius: 5px;\n"
            "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_Edite_Releas_Data.setObjectName(
            "lineEdit_Edite_Releas_Data")
        self.lbl_group_2 = QtWidgets.QLabel(self.tab_edit)
        self.lbl_group_2.setGeometry(QtCore.QRect(340, 155, 81, 16))
        self.lbl_group_2.setStyleSheet("color: rgb(51, 51, 51);\n"
                                       "font: 11pt \"B Nazanin\";\n")
        self.lbl_group_2.setText('Group')
        self.lbl_group_2.setObjectName("lbl_group_2")
        self.check_Edite_Iranian = QtWidgets.QCheckBox(self.tab_edit)
        self.check_Edite_Iranian.setGeometry(QtCore.QRect(340, 177, 70, 17))
        self.check_Edite_Iranian.setStyleSheet("color: rgb(51, 51, 51);\n"
                                               "font: 10pt \"B Nazanin\";\n")
        self.check_Edite_Iranian.setText('Iranian')
        self.check_Edite_Iranian.setObjectName("check_Edite_Iranian")
        self.check_Edite_Forigen = QtWidgets.QCheckBox(self.tab_edit)
        self.check_Edite_Forigen.setGeometry(QtCore.QRect(420, 177, 70, 17))
        self.check_Edite_Forigen.setStyleSheet("color: rgb(51, 51, 51);\n"
                                               "font: 10pt \"B Nazanin\";\n")
        self.check_Edite_Forigen.setText('Forigen')
        self.check_Edite_Forigen.setObjectName("check_Edite_Foriegn")
        self.check_Edite_Forigen.setObjectName("lbl_Add_Name_2")
        self.lbl_Description_2 = QtWidgets.QLabel(self.tab_edit)
        self.lbl_Description_2.setGeometry(QtCore.QRect(340, 210, 107, 19))
        self.lbl_Description_2.setStyleSheet("color: rgb(51, 51, 51);\n"
                                             "font: 11pt \"B Nazanin\";\n")
        self.lbl_Description_2.setText('Description')
        self.lbl_Description_2.setObjectName("lbl_Description_2")
        self.lineEdit_Edite_Description = QtWidgets.QLineEdit(self.tab_edit)
        self.lineEdit_Edite_Description.setGeometry(
            QtCore.QRect(340, 232, 150, 65))
        self.lineEdit_Edite_Description.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "border-radius: 5px;\n"
            "font: 10pt \"B Nazanin\";\n")
        self.lineEdit_Edite_Description.setObjectName(
            "lineEdit_Edite_Description")
        self.btn_Edite_Book = QtWidgets.QPushButton(
            self.tab_edit, clicked=lambda: self.edite_Book())
        self.btn_Edite_Book.setGeometry(QtCore.QRect(220, 325, 140, 41))
        self.btn_Edite_Book.setStyleSheet(
            "background-color: rgb(157, 129, 137);\n"
            "color: rgb(51, 51, 51);\n"
            "border-radius: 10px;\n"
            "font: 11pt \"B Nazanin\";\n")
        self.btn_Edite_Book.setObjectName("btn_Edite_Book")
        self.btn_Edite_Book.setText("Edit Book")
        self.myTabs.addTab(self.tab_edit, 'Edit')
        self.retranslateUi(Dialog)
        self.myTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # Func to add book

    def add_Book(self):
        my_connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="your password",
            database="your database"
        )
        my_cursor = my_connection.cursor()
        myTable = "INSERT INTO Book (Name, Author, releasData, my_Group, Description) VALUES (%s,%s,%s,%s,%s)"
        check = ""

        if self.check_Iranian.isChecked() == False and self.check_Forigen.isChecked() == False or self.lineEdit_Add_Name.text() == "" or self.lineEdit_Add_Author.text() == "" or self.lineEdit_Releas_Data.text() == "" or self.lineEdit_Add_Description.text() == "":
            check_message = QMessageBox()
            check_message.setWindowTitle('Message Box')
            check_message.setWindowIcon(QIcon('icons8-warning-100.png'))
            check_message.setText('You shoud fill all of feilds')
            check_message.exec_()
        else:
            if self.check_Iranian.isChecked():
                check = 'Iranian'
            elif self.check_Forigen.isChecked():
                check = 'Foriegn'

            value = (self.lineEdit_Add_Name.text(), self.lineEdit_Add_Author.text(), int(
                self.lineEdit_Releas_Data.text()), check, self.lineEdit_Add_Description.text())
            my_cursor.execute(myTable, value)
            my_connection.commit()
            my_connection.close()

    # func for data
    def show_data(self):
        my_connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="your database",
            database="your database"
        )
        my_cursor = my_connection.cursor()
        my_cursor.execute('SELECT * FROM Book')
        records = my_cursor.fetchall()
        self.myTable.setRowCount(len(records))
        row = 0

        for record in records:
            self.myTable.setItem(row, 0, QtWidgets.QTableWidgetItem(record[0]))
            self.myTable.setItem(row, 1, QtWidgets.QTableWidgetItem(record[1]))
            self.myTable.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(record[2])))
            self.myTable.setItem(row, 3, QtWidgets.QTableWidgetItem(record[3]))
            self.myTable.setItem(row, 4, QtWidgets.QTableWidgetItem(record[4]))
            row += 1
        my_connection.commit()

    # func for delete book
    def delete_Book(self):
        my_connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="your password",
            database="your database"
        )
        my_cursor = my_connection.cursor()
        name_Delete = self.lineEdit_del.text()
        if name_Delete == "":
            check_message = QMessageBox()
            check_message.setWindowTitle('Message Box')
            check_message.setWindowIcon(QIcon('icons8-warning-100.png'))
            check_message.setText('Write the name of the book')
            check_message.exec_()
        else:
            myTable = 'DELETE FROM Book WHERE Name=%s'
            my_cursor.execute(myTable, [(name_Delete)])
            my_connection.commit()
            my_connection.close()

    # func for search book
    def search_Book(self):
        my_connection = pymysql.connect(
            host="localhost",
            user='root',
            password='your password',
            database='your database'
        )
        my_cursor = my_connection.cursor()
        try:
            myTable = "SELECT * FROM book WHERE Name=%s"
            value = self.lineEdit_Name_for_search.text()
            my_cursor.execute(myTable, [(value)])
            data = my_cursor.fetchone()
            self.lineEdit_Edite_Name.setText(data[0])
            self.lineEdit_Edite_Author.setText(data[1])
            self.lineEdit_Edite_Releas_Data.setText(str(data[2]))
            self.lineEdit_Edite_Description.setText(data[3])
        except TypeError:
            info_msg = QMessageBox()
            info_msg.setWindowTitle('Information Message Box')
            info_msg.setWindowIcon(QIcon('icons8-warning-100.png'))
            info_msg.setText('There is no book with this name')
            info_msg.exec_()

    # func for edite
    def edite_Book(self):
        my_connection = pymysql.connect(
            host="localhost",
            user='root',
            password='your password',
            database='your database'
        )
        my_cursor = my_connection.cursor()
        check = ""

        if self.check_Edite_Iranian.isChecked():
            check = 'Iranian'
        elif self.check_Edite_Forigen.isChecked():
            check = 'Forigen'

        my_cursor.execute("""UPDATE book SET Name=%s,Author=%s,releasData=%s,Description=%s,my_Group=%s WHERE Name=%s
        """, (self.lineEdit_Edite_Name.text(),
              self.lineEdit_Edite_Author.text(),
              int(self.lineEdit_Edite_Releas_Data.text()),
              self.lineEdit_Edite_Description.text(),
              check,
              self.lineEdit_Name_for_search.text()
              ))
        my_connection.commit()
        my_connection.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "My Library"))
        self.Book_List.setTitle(_translate("Dialog", "Book"))
        item = self.myTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name Book"))
        item = self.myTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Author Book"))
        item = self.myTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Releas Data"))
        item = self.myTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Description"))
        item = self.myTable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Group"))
        self.btn_show_data.setText(_translate("Dialog", "show Data"))
        self.groupBox_del.setTitle(_translate("Dialog", "Delete"))
        self.label_del.setText(_translate("Dialog", "Name "))
        self.btn_del.setText(_translate("Dialog", "Delete"))
        self.myTabs.setTabText(self.myTabs.indexOf(
            self.tab_home), _translate("Dialog", "Home"))
        self.lbl_Add_Name.setText(_translate("Dialog", "Enter Name Book "))
        self.lbl_Add_Author.setText(
            _translate("Dialog", "Enter Author Book  "))
        self.lbl_Add_Releas_Data.setText(
            _translate("Dialog", "Enter Releas Data "))
        self.lbl_group.setText(_translate("Dialog", "Group "))
        self.lbl_Description.setText(
            _translate("Dialog", "Enter Description "))
        self.check_Iranian.setText(_translate("Dialog", "Iranian"))
        self.check_Forigen.setText(_translate(
            "Dialog", "Foriegn"))
        self.label_h.setText(_translate(
            "Dialog", " Add Your Book Info "))
        self.btn_Add_Book.setText(_translate("Dialog", "Add Book"))
        self.myTabs.setTabText(self.myTabs.indexOf(
            self.tab_add), _translate("Dialog", "Add"))
        self.label_he.setText(_translate(
            "Dialog", " Edit Book Info  "))
        self.lbl_Add_Author_2.setText(
            _translate("Dialog", "Enter Author Book "))
        self.lbl_Description_2.setText(
            _translate("Dialog", "Enter Description "))
        self.check_Edite_Forigen.setText(_translate("Dialog", "Foriegn"))
        self.lbl_Add_Name_2.setText(_translate("Dialog", "Enter Name Book "))
        self.check_Edite_Iranian.setText(_translate("Dialog", "Iranian"))
        self.lbl_Add_Releas_Data_2.setText(
            _translate("Dialog", "Enter Releas Data "))
        self.lbl_group_2.setText(_translate("Dialog", "Group "))
        self.btn_Edite_Book.setText(_translate("Dialog", "Edit Book"))
        self.lbl_Name_for_Edite.setText(_translate(
            "Dialog", "Enter Name Book for Edit "))
        self.btn_Edite_Search.setText(_translate("Dialog", "Search Book"))
        self.myTabs.setTabText(self.myTabs.indexOf(
            self.tab_edit), _translate("Dialog", "Edit "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
