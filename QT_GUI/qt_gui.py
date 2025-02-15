# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 1100)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.Display = QtWidgets.QVBoxLayout()
        self.Display.setObjectName("Display")
        self.img_preview = QtWidgets.QGraphicsView(Form)
        self.img_preview.setObjectName("img_preview")
        self.Display.addWidget(self.img_preview)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_line_spacing_sigma = QtWidgets.QLabel(Form)
        self.label_line_spacing_sigma.setObjectName("label_line_spacing_sigma")
        self.horizontalLayout_13.addWidget(self.label_line_spacing_sigma)
        self.label_font_size_sigma = QtWidgets.QLabel(Form)
        self.label_font_size_sigma.setObjectName("label_font_size_sigma")
        self.horizontalLayout_13.addWidget(self.label_font_size_sigma)
        self.label_word_spacing_sigma = QtWidgets.QLabel(Form)
        self.label_word_spacing_sigma.setObjectName("label_word_spacing_sigma")
        self.horizontalLayout_13.addWidget(self.label_word_spacing_sigma)
        self.label_perturb_x_sigma = QtWidgets.QLabel(Form)
        self.label_perturb_x_sigma.setObjectName("label_perturb_x_sigma")
        self.horizontalLayout_13.addWidget(self.label_perturb_x_sigma)
        self.label_perturb_y_sigma = QtWidgets.QLabel(Form)
        self.label_perturb_y_sigma.setObjectName("label_perturb_y_sigma")
        self.horizontalLayout_13.addWidget(self.label_perturb_y_sigma)
        self.label_perturb_theta_sigma = QtWidgets.QLabel(Form)
        self.label_perturb_theta_sigma.setObjectName("label_perturb_theta_sigma")
        self.horizontalLayout_13.addWidget(self.label_perturb_theta_sigma)
        self.Display.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lineEdit_line_spacing_sigma = QtWidgets.QLineEdit(Form)
        self.lineEdit_line_spacing_sigma.setObjectName("lineEdit_line_spacing_sigma")
        self.horizontalLayout_12.addWidget(self.lineEdit_line_spacing_sigma)
        self.lineEdit_font_size_sigma = QtWidgets.QLineEdit(Form)
        self.lineEdit_font_size_sigma.setObjectName("lineEdit_font_size_sigma")
        self.horizontalLayout_12.addWidget(self.lineEdit_font_size_sigma)
        self.lineEdit_word_spacing_sigma = QtWidgets.QLineEdit(Form)
        self.lineEdit_word_spacing_sigma.setObjectName("lineEdit_word_spacing_sigma")
        self.horizontalLayout_12.addWidget(self.lineEdit_word_spacing_sigma)
        self.lineEdit_perturb_x_sigma = QtWidgets.QLineEdit(Form)
        self.lineEdit_perturb_x_sigma.setObjectName("lineEdit_perturb_x_sigma")
        self.horizontalLayout_12.addWidget(self.lineEdit_perturb_x_sigma)
        self.lineEdit_perturb_y_sigma = QtWidgets.QLineEdit(Form)
        self.lineEdit_perturb_y_sigma.setObjectName("lineEdit_perturb_y_sigma")
        self.horizontalLayout_12.addWidget(self.lineEdit_perturb_y_sigma)
        self.lineEdit_perturb_theta_sigma = QtWidgets.QLineEdit(Form)
        self.lineEdit_perturb_theta_sigma.setObjectName("lineEdit_perturb_theta_sigma")
        self.horizontalLayout_12.addWidget(self.lineEdit_perturb_theta_sigma)
        self.Display.addLayout(self.horizontalLayout_12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.page_label = QtWidgets.QLabel(Form)
        self.page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.page_label.setObjectName("page_label")
        self.horizontalLayout.addWidget(self.page_label)
        self.page_number = QtWidgets.QComboBox(Form)
        self.page_number.setObjectName("page_number")
        self.horizontalLayout.addWidget(self.page_number)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        self.Display.addLayout(self.horizontalLayout)
        self.horizontalLayout_14.addLayout(self.Display)
        self.Info = QtWidgets.QVBoxLayout()
        self.Info.setObjectName("Info")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_width = QtWidgets.QLabel(Form)
        self.label_width.setObjectName("label_width")
        self.horizontalLayout_2.addWidget(self.label_width)
        self.label_height = QtWidgets.QLabel(Form)
        self.label_height.setObjectName("label_height")
        self.horizontalLayout_2.addWidget(self.label_height)
        self.Info.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_width = QtWidgets.QLineEdit(Form)
        self.lineEdit_width.setObjectName("lineEdit_width")
        self.horizontalLayout_3.addWidget(self.lineEdit_width)
        self.resolution_x = QtWidgets.QLabel(Form)
        self.resolution_x.setObjectName("resolution_x")
        self.horizontalLayout_3.addWidget(self.resolution_x)
        self.lineEdit_height = QtWidgets.QLineEdit(Form)
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.horizontalLayout_3.addWidget(self.lineEdit_height)
        self.Info.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ttf_selector = QtWidgets.QComboBox(Form)
        self.ttf_selector.setObjectName("ttf_selector")
        self.horizontalLayout_4.addWidget(self.ttf_selector)
        self.Info.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_font_size = QtWidgets.QLabel(Form)
        self.label_font_size.setObjectName("label_font_size")
        self.horizontalLayout_5.addWidget(self.label_font_size)
        self.label_line_spacing = QtWidgets.QLabel(Form)
        self.label_line_spacing.setObjectName("label_line_spacing")
        self.horizontalLayout_5.addWidget(self.label_line_spacing)
        self.label_char_distance = QtWidgets.QLabel(Form)
        self.label_char_distance.setObjectName("label_char_distance")
        self.horizontalLayout_5.addWidget(self.label_char_distance)
        self.Info.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_font_size = QtWidgets.QLineEdit(Form)
        self.lineEdit_font_size.setObjectName("lineEdit_font_size")
        self.horizontalLayout_6.addWidget(self.lineEdit_font_size)
        self.lineEdit_line_spacing = QtWidgets.QLineEdit(Form)
        self.lineEdit_line_spacing.setObjectName("lineEdit_line_spacing")
        self.horizontalLayout_6.addWidget(self.lineEdit_line_spacing)
        self.lineEdit_char_distance = QtWidgets.QLineEdit(Form)
        self.lineEdit_char_distance.setObjectName("lineEdit_char_distance")
        self.horizontalLayout_6.addWidget(self.lineEdit_char_distance)
        self.Info.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_margin = QtWidgets.QLabel(Form)
        self.label_margin.setObjectName("label_margin")
        self.horizontalLayout_7.addWidget(self.label_margin)
        self.Info.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_margin_top = QtWidgets.QLineEdit(Form)
        self.lineEdit_margin_top.setObjectName("lineEdit_margin_top")
        self.horizontalLayout_8.addWidget(self.lineEdit_margin_top)
        self.lineEdit_margin_bottom = QtWidgets.QLineEdit(Form)
        self.lineEdit_margin_bottom.setObjectName("lineEdit_margin_bottom")
        self.horizontalLayout_8.addWidget(self.lineEdit_margin_bottom)
        self.lineEdit_margin_left = QtWidgets.QLineEdit(Form)
        self.lineEdit_margin_left.setObjectName("lineEdit_margin_left")
        self.horizontalLayout_8.addWidget(self.lineEdit_margin_left)
        self.lineEdit_margin_right = QtWidgets.QLineEdit(Form)
        self.lineEdit_margin_right.setObjectName("lineEdit_margin_right")
        self.horizontalLayout_8.addWidget(self.lineEdit_margin_right)
        self.Info.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_char_color = QtWidgets.QLabel(Form)
        self.label_char_color.setObjectName("label_char_color")
        self.horizontalLayout_10.addWidget(self.label_char_color)
        self.label_background_color = QtWidgets.QLabel(Form)
        self.label_background_color.setObjectName("label_background_color")
        self.horizontalLayout_10.addWidget(self.label_background_color)
        self.Info.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comboBox_char_color = QtWidgets.QComboBox(Form)
        self.comboBox_char_color.setObjectName("comboBox_char_color")
        self.horizontalLayout_9.addWidget(self.comboBox_char_color)
        self.comboBox_background_color = QtWidgets.QComboBox(Form)
        self.comboBox_background_color.setObjectName("comboBox_background_color")
        self.horizontalLayout_9.addWidget(self.comboBox_background_color)
        self.Info.addLayout(self.horizontalLayout_9)
        self.textEdit_main = QtWidgets.QTextEdit(Form)
        self.textEdit_main.setObjectName("textEdit_main")
        self.Info.addWidget(self.textEdit_main)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.comboBox_resolution = QtWidgets.QComboBox(Form)
        self.comboBox_resolution.setIconSize(QtCore.QSize(16, 16))
        self.comboBox_resolution.setObjectName("comboBox_resolution")
        self.horizontalLayout_11.addWidget(self.comboBox_resolution)
        self.pushButton_export = QtWidgets.QPushButton(Form)
        self.pushButton_export.setObjectName("pushButton_export")
        self.horizontalLayout_11.addWidget(self.pushButton_export)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 5)
        self.Info.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14.addLayout(self.Info)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_line_spacing_sigma.setText(_translate("Form", "行间距扰动"))
        self.label_font_size_sigma.setText(_translate("Form", "字体大小扰动"))
        self.label_word_spacing_sigma.setText(_translate("Form", "字间距扰动"))
        self.label_perturb_x_sigma.setText(_translate("Form", "横向笔画扰动"))
        self.label_perturb_y_sigma.setText(_translate("Form", "纵向笔画扰动"))
        self.label_perturb_theta_sigma.setText(_translate("Form", "旋转笔画扰动"))
        self.page_label.setText(_translate("Form", "Page:"))
        self.label_width.setText(_translate("Form", "宽度"))
        self.label_height.setText(_translate("Form", "高度"))
        self.resolution_x.setText(_translate("Form", "x"))
        self.label_font_size.setText(_translate("Form", "字体大小"))
        self.label_line_spacing.setText(_translate("Form", "行距"))
        self.label_char_distance.setText(_translate("Form", "字距"))
        self.label_margin.setText(_translate("Form", "留白(上,下,左,右)"))
        self.label_char_color.setText(_translate("Form", "字体色"))
        self.label_background_color.setText(_translate("Form", "背景色"))
        self.pushButton_export.setText(_translate("Form", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
