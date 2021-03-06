#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form_TagSelector"))
        Form.resize(336, 463)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 111, 261))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 89, 229))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox2 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox2.setObjectName(_fromUtf8("checkBox2"))
        self.verticalLayout.addWidget(self.checkBox2)
        self.checkBox3 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox3.setObjectName(_fromUtf8("checkBox3"))
        self.verticalLayout.addWidget(self.checkBox3)
        self.checkBox4 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox4.setObjectName(_fromUtf8("checkBox4"))
        self.verticalLayout.addWidget(self.checkBox4)
        self.checkBox5 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox5.setObjectName(_fromUtf8("checkBox5"))
        self.verticalLayout.addWidget(self.checkBox5)
        self.checkBox6 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox6.setObjectName(_fromUtf8("checkBox6"))
        self.verticalLayout.addWidget(self.checkBox6)
        self.checkBox7 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox7.setObjectName(_fromUtf8("checkBox7"))
        self.verticalLayout.addWidget(self.checkBox7)
        self.checkBox8 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox8.setObjectName(_fromUtf8("checkBox8"))
        self.verticalLayout.addWidget(self.checkBox8)
        self.checkBox9 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox9.setObjectName(_fromUtf8("checkBox9"))
        self.verticalLayout.addWidget(self.checkBox9)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 270, 101, 131))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget1 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 20, 89, 99))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBox10 = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox10.setObjectName(_fromUtf8("checkBox10"))
        self.verticalLayout_2.addWidget(self.checkBox10)
        self.checkBox11 = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox11.setObjectName(_fromUtf8("checkBox11"))
        self.verticalLayout_2.addWidget(self.checkBox11)
        self.checkBox12 = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox12.setObjectName(_fromUtf8("checkBox12"))
        self.verticalLayout_2.addWidget(self.checkBox12)
        self.checkBox13 = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox13.setObjectName(_fromUtf8("checkBox13"))
        self.verticalLayout_2.addWidget(self.checkBox13)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(130, 140, 101, 261))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.layoutWidget2 = QtGui.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 20, 89, 231))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.checkBox18 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox18.setObjectName(_fromUtf8("checkBox18"))
        self.verticalLayout_3.addWidget(self.checkBox18)
        self.checkBox19 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox19.setObjectName(_fromUtf8("checkBox19"))
        self.verticalLayout_3.addWidget(self.checkBox19)
        self.checkBox20 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox20.setObjectName(_fromUtf8("checkBox20"))
        self.verticalLayout_3.addWidget(self.checkBox20)
        self.checkBox21 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox21.setObjectName(_fromUtf8("checkBox21"))
        self.verticalLayout_3.addWidget(self.checkBox21)
        self.checkBox22 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox22.setObjectName(_fromUtf8("checkBox22"))
        self.verticalLayout_3.addWidget(self.checkBox22)
        self.checkBox23 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox23.setObjectName(_fromUtf8("checkBox23"))
        self.verticalLayout_3.addWidget(self.checkBox23)
        self.checkBox24 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox24.setObjectName(_fromUtf8("checkBox24"))
        self.verticalLayout_3.addWidget(self.checkBox24)
        self.checkBox25 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox25.setObjectName(_fromUtf8("checkBox25"))
        self.verticalLayout_3.addWidget(self.checkBox25)
        self.checkBox26 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox26.setObjectName(_fromUtf8("checkBox26"))
        self.verticalLayout_3.addWidget(self.checkBox26)
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(130, 10, 101, 131))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.layoutWidget3 = QtGui.QWidget(self.groupBox_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 20, 89, 99))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.checkBox14 = QtGui.QCheckBox(self.layoutWidget3)
        self.checkBox14.setObjectName(_fromUtf8("checkBox14"))
        self.verticalLayout_4.addWidget(self.checkBox14)
        self.checkBox15 = QtGui.QCheckBox(self.layoutWidget3)
        self.checkBox15.setObjectName(_fromUtf8("checkBox15"))
        self.verticalLayout_4.addWidget(self.checkBox15)
        self.checkBox16 = QtGui.QCheckBox(self.layoutWidget3)
        self.checkBox16.setObjectName(_fromUtf8("checkBox16"))
        self.verticalLayout_4.addWidget(self.checkBox16)
        self.checkBox17 = QtGui.QCheckBox(self.layoutWidget3)
        self.checkBox17.setObjectName(_fromUtf8("checkBox17"))
        self.verticalLayout_4.addWidget(self.checkBox17)
        self.groupBox_6 = QtGui.QGroupBox(Form)
        self.groupBox_6.setGeometry(QtCore.QRect(240, 10, 81, 291))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.layoutWidget4 = QtGui.QWidget(self.groupBox_6)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 20, 74, 255))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.checkBox27 = QtGui.QCheckBox(self.layoutWidget4)
        self.checkBox27.setObjectName(_fromUtf8("checkBox27"))
        self.verticalLayout_6.addWidget(self.checkBox27)
        self.checkBox28 = QtGui.QCheckBox(self.layoutWidget4)
        self.checkBox28.setObjectName(_fromUtf8("checkBox28"))
        self.verticalLayout_6.addWidget(self.checkBox28)
        self.checkBox29 = QtGui.QCheckBox(self.layoutWidget4)
        self.checkBox29.setObjectName(_fromUtf8("checkBox29"))
        self.verticalLayout_6.addWidget(self.checkBox29)
        self.checkBox30 = QtGui.QCheckBox(self.layoutWidget4)
        self.checkBox30.setObjectName(_fromUtf8("checkBox30"))
        self.verticalLayout_6.addWidget(self.checkBox30)
        self.checkBox31 = QtGui.QCheckBox(self.layoutWidget4)
        self.checkBox31.setObjectName(_fromUtf8("checkBox31"))
        self.verticalLayout_6.addWidget(self.checkBox31)
        self.checkBox32 = QtGui.QCheckBox(self.layoutWidget4)
        self.checkBox32.setObjectName(_fromUtf8("checkBox32"))
        self.verticalLayout_6.addWidget(self.checkBox32)
        self.checkBox33 = QtGui.QCheckBox(self.layoutWidget4)
        self.checkBox33.setObjectName(_fromUtf8("checkBox33"))
        self.verticalLayout_6.addWidget(self.checkBox33)
        self.checkBox34 = QtGui.QCheckBox(self.layoutWidget4)
        self.checkBox34.setObjectName(_fromUtf8("checkBox34"))
        self.verticalLayout_6.addWidget(self.checkBox34)
        self.checkBox35 = QtGui.QCheckBox(self.layoutWidget4)
        self.checkBox35.setObjectName(_fromUtf8("checkBox35"))
        self.verticalLayout_6.addWidget(self.checkBox35)
        self.checkBox36 = QtGui.QCheckBox(self.layoutWidget4)
        self.checkBox36.setObjectName(_fromUtf8("checkBox36"))
        self.verticalLayout_6.addWidget(self.checkBox36)
        self.btn_tag_ok = QtGui.QPushButton(Form)
        self.btn_tag_ok.setGeometry(QtCore.QRect(130, 420, 93, 28))
        self.btn_tag_ok.setObjectName(_fromUtf8("btn_tag_ok"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "风格", None))
        self.checkBox.setText(_translate("Form", "流行摇滚", None))
        self.checkBox2.setText(_translate("Form", "乡村民谣", None))
        self.checkBox3.setText(_translate("Form", "爵士蓝调", None))
        self.checkBox4.setText(_translate("Form", "金属朋克", None))
        self.checkBox5.setText(_translate("Form", "轻音乐", None))
        self.checkBox6.setText(_translate("Form", "古典", None))
        self.checkBox7.setText(_translate("Form", "国风", None))
        self.checkBox8.setText(_translate("Form", "电子", None))
        self.checkBox9.setText(_translate("Form", "说唱", None))
        self.groupBox_2.setTitle(_translate("Form", "场景", None))
        self.checkBox10.setText(_translate("Form", "清晨", None))
        self.checkBox11.setText(_translate("Form", "下午茶", None))
        self.checkBox12.setText(_translate("Form", "夜晚", None))
        self.checkBox13.setText(_translate("Form", "学习工作", None))
        self.groupBox_3.setTitle(_translate("Form", "情感", None))
        self.checkBox18.setText(_translate("Form", "清新明媚", None))
        self.checkBox19.setText(_translate("Form", "兴奋动感", None))
        self.checkBox20.setText(_translate("Form", "治愈感动", None))
        self.checkBox21.setText(_translate("Form", "怀旧伤感", None))
        self.checkBox22.setText(_translate("Form", "安静放松", None))
        self.checkBox23.setText(_translate("Form", "快乐", None))
        self.checkBox24.setText(_translate("Form", "浪漫", None))
        self.checkBox25.setText(_translate("Form", "孤独", None))
        self.checkBox26.setText(_translate("Form", "思念", None))
        self.checkBox14.setText(_translate("Form", "运动旅行", None))
        self.checkBox15.setText(_translate("Form", "婚礼庆典", None))
        self.checkBox16.setText(_translate("Form", "影视", None))
        self.checkBox17.setText(_translate("Form", "ACG", None))
        self.groupBox_6.setTitle(_translate("Form", "乐器", None))
        self.checkBox27.setText(_translate("Form", "钢琴", None))
        self.checkBox28.setText(_translate("Form", "弦乐组", None))
        self.checkBox29.setText(_translate("Form", "管乐组", None))
        self.checkBox30.setText(_translate("Form", "室内乐", None))
        self.checkBox31.setText(_translate("Form", "电吉他", None))
        self.checkBox32.setText(_translate("Form", "口琴", None))
        self.checkBox33.setText(_translate("Form", "古筝", None))
        self.checkBox34.setText(_translate("Form", "二胡", None))
        self.checkBox35.setText(_translate("Form", "琵琶", None))
        self.checkBox36.setText(_translate("Form", "箫笛", None))
        self.btn_tag_ok.setText(_translate("Form", "确定", None))

