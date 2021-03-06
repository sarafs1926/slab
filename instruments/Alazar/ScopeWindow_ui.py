# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScopeWindow.ui'
#
# Created: Thu May 16 13:42:12 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ScopeWindow(object):
    def setupUi(self, ScopeWindow):
        ScopeWindow.setObjectName(_fromUtf8("ScopeWindow"))
        ScopeWindow.resize(1104, 737)
        self.centralwidget = QtGui.QWidget(ScopeWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.ScopeSettings = QtGui.QGroupBox(self.centralwidget)
        self.ScopeSettings.setObjectName(_fromUtf8("ScopeSettings"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.ScopeSettings)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.SampleSettings = QtGui.QGroupBox(self.ScopeSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SampleSettings.sizePolicy().hasHeightForWidth())
        self.SampleSettings.setSizePolicy(sizePolicy)
        self.SampleSettings.setObjectName(_fromUtf8("SampleSettings"))
        self.gridLayout = QtGui.QGridLayout(self.SampleSettings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.SampleSettings)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.samplesSpinBox = QtGui.QSpinBox(self.SampleSettings)
        self.samplesSpinBox.setMinimum(32)
        self.samplesSpinBox.setMaximum(999999999)
        self.samplesSpinBox.setSingleStep(64)
        self.samplesSpinBox.setProperty("value", 1024)
        self.samplesSpinBox.setObjectName(_fromUtf8("samplesSpinBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.samplesSpinBox)
        self.label_2 = QtGui.QLabel(self.SampleSettings)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.recordsSpinBox = QtGui.QSpinBox(self.SampleSettings)
        self.recordsSpinBox.setMinimum(1)
        self.recordsSpinBox.setMaximum(999999999)
        self.recordsSpinBox.setObjectName(_fromUtf8("recordsSpinBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.recordsSpinBox)
        self.label_3 = QtGui.QLabel(self.SampleSettings)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.buffersSpinBox = QtGui.QSpinBox(self.SampleSettings)
        self.buffersSpinBox.setMinimum(1)
        self.buffersSpinBox.setMaximum(999999999)
        self.buffersSpinBox.setObjectName(_fromUtf8("buffersSpinBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.buffersSpinBox)
        self.label_21 = QtGui.QLabel(self.SampleSettings)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_21)
        self.recordsPerAcquisitionSpinBox = QtGui.QSpinBox(self.SampleSettings)
        self.recordsPerAcquisitionSpinBox.setMinimum(1)
        self.recordsPerAcquisitionSpinBox.setMaximum(999999999)
        self.recordsPerAcquisitionSpinBox.setProperty("value", 1)
        self.recordsPerAcquisitionSpinBox.setObjectName(_fromUtf8("recordsPerAcquisitionSpinBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.recordsPerAcquisitionSpinBox)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.SampleSettings)
        self.VerticalSettings = QtGui.QGroupBox(self.ScopeSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VerticalSettings.sizePolicy().hasHeightForWidth())
        self.VerticalSettings.setSizePolicy(sizePolicy)
        self.VerticalSettings.setObjectName(_fromUtf8("VerticalSettings"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.VerticalSettings)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Ch1Vertical = QtGui.QGroupBox(self.VerticalSettings)
        self.Ch1Vertical.setObjectName(_fromUtf8("Ch1Vertical"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Ch1Vertical)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.ch1_enabledCheckBox = QtGui.QCheckBox(self.Ch1Vertical)
        self.ch1_enabledCheckBox.setChecked(True)
        self.ch1_enabledCheckBox.setObjectName(_fromUtf8("ch1_enabledCheckBox"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.ch1_enabledCheckBox)
        self.ch1_filteredCheckBox = QtGui.QCheckBox(self.Ch1Vertical)
        self.ch1_filteredCheckBox.setObjectName(_fromUtf8("ch1_filteredCheckBox"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.ch1_filteredCheckBox)
        self.label_16 = QtGui.QLabel(self.Ch1Vertical)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_16)
        self.ch1_rangeComboBox = QtGui.QComboBox(self.Ch1Vertical)
        self.ch1_rangeComboBox.setObjectName(_fromUtf8("ch1_rangeComboBox"))
        self.ch1_rangeComboBox.addItem(_fromUtf8(""))
        self.ch1_rangeComboBox.addItem(_fromUtf8(""))
        self.ch1_rangeComboBox.addItem(_fromUtf8(""))
        self.ch1_rangeComboBox.addItem(_fromUtf8(""))
        self.ch1_rangeComboBox.addItem(_fromUtf8(""))
        self.ch1_rangeComboBox.addItem(_fromUtf8(""))
        self.ch1_rangeComboBox.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.ch1_rangeComboBox)
        self.label_17 = QtGui.QLabel(self.Ch1Vertical)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_17)
        self.ch1_couplingComboBox = QtGui.QComboBox(self.Ch1Vertical)
        self.ch1_couplingComboBox.setObjectName(_fromUtf8("ch1_couplingComboBox"))
        self.ch1_couplingComboBox.addItem(_fromUtf8(""))
        self.ch1_couplingComboBox.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.ch1_couplingComboBox)
        self.verticalLayout_3.addLayout(self.formLayout_5)
        self.horizontalLayout_2.addWidget(self.Ch1Vertical)
        self.Ch2Vertical = QtGui.QGroupBox(self.VerticalSettings)
        self.Ch2Vertical.setObjectName(_fromUtf8("Ch2Vertical"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.Ch2Vertical)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.ch2_enabledCheckBox = QtGui.QCheckBox(self.Ch2Vertical)
        self.ch2_enabledCheckBox.setChecked(True)
        self.ch2_enabledCheckBox.setObjectName(_fromUtf8("ch2_enabledCheckBox"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.ch2_enabledCheckBox)
        self.ch2_filteredCheckBox = QtGui.QCheckBox(self.Ch2Vertical)
        self.ch2_filteredCheckBox.setObjectName(_fromUtf8("ch2_filteredCheckBox"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.ch2_filteredCheckBox)
        self.label_18 = QtGui.QLabel(self.Ch2Vertical)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_18)
        self.ch2_rangeComboBox = QtGui.QComboBox(self.Ch2Vertical)
        self.ch2_rangeComboBox.setObjectName(_fromUtf8("ch2_rangeComboBox"))
        self.ch2_rangeComboBox.addItem(_fromUtf8(""))
        self.ch2_rangeComboBox.addItem(_fromUtf8(""))
        self.ch2_rangeComboBox.addItem(_fromUtf8(""))
        self.ch2_rangeComboBox.addItem(_fromUtf8(""))
        self.ch2_rangeComboBox.addItem(_fromUtf8(""))
        self.ch2_rangeComboBox.addItem(_fromUtf8(""))
        self.ch2_rangeComboBox.addItem(_fromUtf8(""))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.ch2_rangeComboBox)
        self.label_19 = QtGui.QLabel(self.Ch2Vertical)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_19)
        self.ch2_couplingComboBox = QtGui.QComboBox(self.Ch2Vertical)
        self.ch2_couplingComboBox.setObjectName(_fromUtf8("ch2_couplingComboBox"))
        self.ch2_couplingComboBox.addItem(_fromUtf8(""))
        self.ch2_couplingComboBox.addItem(_fromUtf8(""))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.ch2_couplingComboBox)
        self.verticalLayout_4.addLayout(self.formLayout_6)
        self.horizontalLayout_2.addWidget(self.Ch2Vertical)
        self.verticalLayout_5.addWidget(self.VerticalSettings)
        self.ClockSettings = QtGui.QGroupBox(self.ScopeSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClockSettings.sizePolicy().hasHeightForWidth())
        self.ClockSettings.setSizePolicy(sizePolicy)
        self.ClockSettings.setObjectName(_fromUtf8("ClockSettings"))
        self.verticalLayout = QtGui.QVBoxLayout(self.ClockSettings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_6 = QtGui.QLabel(self.ClockSettings)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.samplerateComboBox = QtGui.QComboBox(self.ClockSettings)
        self.samplerateComboBox.setObjectName(_fromUtf8("samplerateComboBox"))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.samplerateComboBox.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.samplerateComboBox)
        self.label_4 = QtGui.QLabel(self.ClockSettings)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.clocksourceComboBox = QtGui.QComboBox(self.ClockSettings)
        self.clocksourceComboBox.setObjectName(_fromUtf8("clocksourceComboBox"))
        self.clocksourceComboBox.addItem(_fromUtf8(""))
        self.clocksourceComboBox.addItem(_fromUtf8(""))
        self.clocksourceComboBox.addItem(_fromUtf8(""))
        self.clocksourceComboBox.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.clocksourceComboBox)
        self.label_5 = QtGui.QLabel(self.ClockSettings)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.clockedgeComboBox = QtGui.QComboBox(self.ClockSettings)
        self.clockedgeComboBox.setObjectName(_fromUtf8("clockedgeComboBox"))
        self.clockedgeComboBox.addItem(_fromUtf8(""))
        self.clockedgeComboBox.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.clockedgeComboBox)
        self.label_10 = QtGui.QLabel(self.ClockSettings)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.timeoutSpinBox = QtGui.QSpinBox(self.ClockSettings)
        self.timeoutSpinBox.setMaximum(1000000000)
        self.timeoutSpinBox.setProperty("value", 5000)
        self.timeoutSpinBox.setObjectName(_fromUtf8("timeoutSpinBox"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.timeoutSpinBox)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_5.addWidget(self.ClockSettings)
        self.TriggerSettings = QtGui.QGroupBox(self.ScopeSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TriggerSettings.sizePolicy().hasHeightForWidth())
        self.TriggerSettings.setSizePolicy(sizePolicy)
        self.TriggerSettings.setObjectName(_fromUtf8("TriggerSettings"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.TriggerSettings)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_7 = QtGui.QLabel(self.TriggerSettings)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.trig1_sourceComboBox = QtGui.QComboBox(self.TriggerSettings)
        self.trig1_sourceComboBox.setObjectName(_fromUtf8("trig1_sourceComboBox"))
        self.trig1_sourceComboBox.addItem(_fromUtf8(""))
        self.trig1_sourceComboBox.addItem(_fromUtf8(""))
        self.trig1_sourceComboBox.addItem(_fromUtf8(""))
        self.trig1_sourceComboBox.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.trig1_sourceComboBox)
        self.trig1_edgeComboBox = QtGui.QComboBox(self.TriggerSettings)
        self.trig1_edgeComboBox.setObjectName(_fromUtf8("trig1_edgeComboBox"))
        self.trig1_edgeComboBox.addItem(_fromUtf8(""))
        self.trig1_edgeComboBox.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.trig1_edgeComboBox)
        self.label_9 = QtGui.QLabel(self.TriggerSettings)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.trig1_levelSpinBox = QtGui.QDoubleSpinBox(self.TriggerSettings)
        self.trig1_levelSpinBox.setProperty("value", 1.0)
        self.trig1_levelSpinBox.setObjectName(_fromUtf8("trig1_levelSpinBox"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.trig1_levelSpinBox)
        self.label_11 = QtGui.QLabel(self.TriggerSettings)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_11)
        self.trigCouplingComboBox = QtGui.QComboBox(self.TriggerSettings)
        self.trigCouplingComboBox.setObjectName(_fromUtf8("trigCouplingComboBox"))
        self.trigCouplingComboBox.addItem(_fromUtf8(""))
        self.trigCouplingComboBox.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.trigCouplingComboBox)
        self.label_8 = QtGui.QLabel(self.TriggerSettings)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout.addLayout(self.formLayout_3)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_12 = QtGui.QLabel(self.TriggerSettings)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_12)
        self.trig2_sourceComboBox = QtGui.QComboBox(self.TriggerSettings)
        self.trig2_sourceComboBox.setObjectName(_fromUtf8("trig2_sourceComboBox"))
        self.trig2_sourceComboBox.addItem(_fromUtf8(""))
        self.trig2_sourceComboBox.addItem(_fromUtf8(""))
        self.trig2_sourceComboBox.addItem(_fromUtf8(""))
        self.trig2_sourceComboBox.addItem(_fromUtf8(""))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.trig2_sourceComboBox)
        self.trig2_edgeComboBox = QtGui.QComboBox(self.TriggerSettings)
        self.trig2_edgeComboBox.setObjectName(_fromUtf8("trig2_edgeComboBox"))
        self.trig2_edgeComboBox.addItem(_fromUtf8(""))
        self.trig2_edgeComboBox.addItem(_fromUtf8(""))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.trig2_edgeComboBox)
        self.label_13 = QtGui.QLabel(self.TriggerSettings)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_13)
        self.trig2_levelSpinBox = QtGui.QDoubleSpinBox(self.TriggerSettings)
        self.trig2_levelSpinBox.setProperty("value", 1.0)
        self.trig2_levelSpinBox.setObjectName(_fromUtf8("trig2_levelSpinBox"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.trig2_levelSpinBox)
        self.label_14 = QtGui.QLabel(self.TriggerSettings)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtGui.QLabel(self.TriggerSettings)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_15)
        self.trigOpComboBox = QtGui.QComboBox(self.TriggerSettings)
        self.trigOpComboBox.setObjectName(_fromUtf8("trigOpComboBox"))
        self.trigOpComboBox.addItem(_fromUtf8(""))
        self.trigOpComboBox.addItem(_fromUtf8(""))
        self.trigOpComboBox.addItem(_fromUtf8(""))
        self.trigOpComboBox.addItem(_fromUtf8(""))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.trigOpComboBox)
        self.horizontalLayout.addLayout(self.formLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.TriggerSettings)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_5.addWidget(self.ScopeSettings)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.datapathButton = QtGui.QPushButton(self.centralwidget)
        self.datapathButton.setObjectName(_fromUtf8("datapathButton"))
        self.horizontalLayout_3.addWidget(self.datapathButton)
        self.datapathLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.datapathLineEdit.setObjectName(_fromUtf8("datapathLineEdit"))
        self.horizontalLayout_3.addWidget(self.datapathLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_6.addWidget(self.label_20)
        self.filenumberLabel = QtGui.QLabel(self.centralwidget)
        self.filenumberLabel.setObjectName(_fromUtf8("filenumberLabel"))
        self.horizontalLayout_6.addWidget(self.filenumberLabel)
        self.prefixLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.prefixLineEdit.setObjectName(_fromUtf8("prefixLineEdit"))
        self.horizontalLayout_6.addWidget(self.prefixLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.runButton = QtGui.QPushButton(self.centralwidget)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.horizontalLayout_4.addWidget(self.runButton)
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_4.addWidget(self.saveButton)
        self.autosaveCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.autosaveCheckBox.setObjectName(_fromUtf8("autosaveCheckBox"))
        self.horizontalLayout_4.addWidget(self.autosaveCheckBox)
        self.autorunCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.autorunCheckBox.setChecked(True)
        self.autorunCheckBox.setObjectName(_fromUtf8("autorunCheckBox"))
        self.horizontalLayout_4.addWidget(self.autorunCheckBox)
        self.PSDCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.PSDCheckBox.setObjectName(_fromUtf8("PSDCheckBox"))
        self.horizontalLayout_4.addWidget(self.PSDCheckBox)
        self.x_autoscaleCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.x_autoscaleCheckBox.setEnabled(False)
        self.x_autoscaleCheckBox.setChecked(True)
        self.x_autoscaleCheckBox.setObjectName(_fromUtf8("x_autoscaleCheckBox"))
        self.horizontalLayout_4.addWidget(self.x_autoscaleCheckBox)
        self.y_autoscaleCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.y_autoscaleCheckBox.setEnabled(False)
        self.y_autoscaleCheckBox.setChecked(True)
        self.y_autoscaleCheckBox.setObjectName(_fromUtf8("y_autoscaleCheckBox"))
        self.horizontalLayout_4.addWidget(self.y_autoscaleCheckBox)
        self.autoscaleCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.autoscaleCheckBox.setChecked(True)
        self.autoscaleCheckBox.setObjectName(_fromUtf8("autoscaleCheckBox"))
        self.horizontalLayout_4.addWidget(self.autoscaleCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.curvewidget = CurveWidget(self.centralwidget)
        self.curvewidget.setOrientation(QtCore.Qt.Horizontal)
        self.curvewidget.setObjectName(_fromUtf8("curvewidget"))
        self.verticalLayout_2.addWidget(self.curvewidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        ScopeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ScopeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ScopeWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ScopeWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ScopeWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(ScopeWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        ScopeWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(ScopeWindow)
        self.trig1_sourceComboBox.setCurrentIndex(2)
        self.trig2_sourceComboBox.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(ScopeWindow)

    def retranslateUi(self, ScopeWindow):
        ScopeWindow.setWindowTitle(QtGui.QApplication.translate("ScopeWindow", "DScope", None, QtGui.QApplication.UnicodeUTF8))
        self.ScopeSettings.setTitle(QtGui.QApplication.translate("ScopeWindow", "Scope Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.SampleSettings.setTitle(QtGui.QApplication.translate("ScopeWindow", "Sample / Buffer Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ScopeWindow", "Samples", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ScopeWindow", "Records per Buffer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ScopeWindow", "Buffers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("ScopeWindow", "Records per Acquisition", None, QtGui.QApplication.UnicodeUTF8))
        self.VerticalSettings.setTitle(QtGui.QApplication.translate("ScopeWindow", "Vertical Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.Ch1Vertical.setTitle(QtGui.QApplication.translate("ScopeWindow", "Channel 1", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_enabledCheckBox.setText(QtGui.QApplication.translate("ScopeWindow", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_filteredCheckBox.setText(QtGui.QApplication.translate("ScopeWindow", "Filtered", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("ScopeWindow", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_rangeComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "4 V", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_rangeComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "2 V", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_rangeComboBox.setItemText(2, QtGui.QApplication.translate("ScopeWindow", "1 V", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_rangeComboBox.setItemText(3, QtGui.QApplication.translate("ScopeWindow", "400 mV", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_rangeComboBox.setItemText(4, QtGui.QApplication.translate("ScopeWindow", "200 mV", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_rangeComboBox.setItemText(5, QtGui.QApplication.translate("ScopeWindow", "100 mV", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_rangeComboBox.setItemText(6, QtGui.QApplication.translate("ScopeWindow", "40 mV", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("ScopeWindow", "Coupling", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_couplingComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "DC", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1_couplingComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "AC", None, QtGui.QApplication.UnicodeUTF8))
        self.Ch2Vertical.setTitle(QtGui.QApplication.translate("ScopeWindow", "Channel 2", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_enabledCheckBox.setText(QtGui.QApplication.translate("ScopeWindow", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_filteredCheckBox.setText(QtGui.QApplication.translate("ScopeWindow", "Filtered", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("ScopeWindow", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_rangeComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "4 V", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_rangeComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "2 V", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_rangeComboBox.setItemText(2, QtGui.QApplication.translate("ScopeWindow", "1 V", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_rangeComboBox.setItemText(3, QtGui.QApplication.translate("ScopeWindow", "400 mV", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_rangeComboBox.setItemText(4, QtGui.QApplication.translate("ScopeWindow", "200 mV", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_rangeComboBox.setItemText(5, QtGui.QApplication.translate("ScopeWindow", "100 mV", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_rangeComboBox.setItemText(6, QtGui.QApplication.translate("ScopeWindow", "40 mV", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("ScopeWindow", "Coupling", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_couplingComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "DC", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2_couplingComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "AC", None, QtGui.QApplication.UnicodeUTF8))
        self.ClockSettings.setTitle(QtGui.QApplication.translate("ScopeWindow", "Clock Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ScopeWindow", "Clock Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "1 GHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "500 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(2, QtGui.QApplication.translate("ScopeWindow", "250 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(3, QtGui.QApplication.translate("ScopeWindow", "100 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(4, QtGui.QApplication.translate("ScopeWindow", "50 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(5, QtGui.QApplication.translate("ScopeWindow", "20 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(6, QtGui.QApplication.translate("ScopeWindow", "10 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(7, QtGui.QApplication.translate("ScopeWindow", "5 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(8, QtGui.QApplication.translate("ScopeWindow", "2 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(9, QtGui.QApplication.translate("ScopeWindow", "1 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(10, QtGui.QApplication.translate("ScopeWindow", "20 kHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(11, QtGui.QApplication.translate("ScopeWindow", "10 kHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(12, QtGui.QApplication.translate("ScopeWindow", "5 kHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(13, QtGui.QApplication.translate("ScopeWindow", "2 kHz", None, QtGui.QApplication.UnicodeUTF8))
        self.samplerateComboBox.setItemText(14, QtGui.QApplication.translate("ScopeWindow", "1 kHz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ScopeWindow", "Clock Source", None, QtGui.QApplication.UnicodeUTF8))
        self.clocksourceComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "internal", None, QtGui.QApplication.UnicodeUTF8))
        self.clocksourceComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "reference", None, QtGui.QApplication.UnicodeUTF8))
        self.clocksourceComboBox.setItemText(2, QtGui.QApplication.translate("ScopeWindow", "60 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.clocksourceComboBox.setItemText(3, QtGui.QApplication.translate("ScopeWindow", "1 GHz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ScopeWindow", "Clock Edge", None, QtGui.QApplication.UnicodeUTF8))
        self.clockedgeComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "rising", None, QtGui.QApplication.UnicodeUTF8))
        self.clockedgeComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "falling", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ScopeWindow", "Timeout", None, QtGui.QApplication.UnicodeUTF8))
        self.TriggerSettings.setTitle(QtGui.QApplication.translate("ScopeWindow", "Trigger Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ScopeWindow", "Source 1", None, QtGui.QApplication.UnicodeUTF8))
        self.trig1_sourceComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "CH_A", None, QtGui.QApplication.UnicodeUTF8))
        self.trig1_sourceComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "CH_B", None, QtGui.QApplication.UnicodeUTF8))
        self.trig1_sourceComboBox.setItemText(2, QtGui.QApplication.translate("ScopeWindow", "external", None, QtGui.QApplication.UnicodeUTF8))
        self.trig1_sourceComboBox.setItemText(3, QtGui.QApplication.translate("ScopeWindow", "disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.trig1_edgeComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "rising", None, QtGui.QApplication.UnicodeUTF8))
        self.trig1_edgeComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "falling", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ScopeWindow", "Level 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ScopeWindow", "Coupling", None, QtGui.QApplication.UnicodeUTF8))
        self.trigCouplingComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "DC", None, QtGui.QApplication.UnicodeUTF8))
        self.trigCouplingComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "AC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ScopeWindow", "Edge 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ScopeWindow", "Source 2", None, QtGui.QApplication.UnicodeUTF8))
        self.trig2_sourceComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "CH_A", None, QtGui.QApplication.UnicodeUTF8))
        self.trig2_sourceComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "CH_B", None, QtGui.QApplication.UnicodeUTF8))
        self.trig2_sourceComboBox.setItemText(2, QtGui.QApplication.translate("ScopeWindow", "external", None, QtGui.QApplication.UnicodeUTF8))
        self.trig2_sourceComboBox.setItemText(3, QtGui.QApplication.translate("ScopeWindow", "disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.trig2_edgeComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "rising", None, QtGui.QApplication.UnicodeUTF8))
        self.trig2_edgeComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "falling", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ScopeWindow", "Level 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ScopeWindow", "Operation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ScopeWindow", "Edge 2", None, QtGui.QApplication.UnicodeUTF8))
        self.trigOpComboBox.setItemText(0, QtGui.QApplication.translate("ScopeWindow", "or", None, QtGui.QApplication.UnicodeUTF8))
        self.trigOpComboBox.setItemText(1, QtGui.QApplication.translate("ScopeWindow", "and", None, QtGui.QApplication.UnicodeUTF8))
        self.trigOpComboBox.setItemText(2, QtGui.QApplication.translate("ScopeWindow", "xor", None, QtGui.QApplication.UnicodeUTF8))
        self.trigOpComboBox.setItemText(3, QtGui.QApplication.translate("ScopeWindow", "and not", None, QtGui.QApplication.UnicodeUTF8))
        self.datapathButton.setText(QtGui.QApplication.translate("ScopeWindow", "Datapath", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("ScopeWindow", "File Prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.filenumberLabel.setText(QtGui.QApplication.translate("ScopeWindow", "000_", None, QtGui.QApplication.UnicodeUTF8))
        self.prefixLineEdit.setText(QtGui.QApplication.translate("ScopeWindow", "trace", None, QtGui.QApplication.UnicodeUTF8))
        self.runButton.setText(QtGui.QApplication.translate("ScopeWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("ScopeWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.autosaveCheckBox.setText(QtGui.QApplication.translate("ScopeWindow", "autosave", None, QtGui.QApplication.UnicodeUTF8))
        self.autorunCheckBox.setText(QtGui.QApplication.translate("ScopeWindow", "autorun", None, QtGui.QApplication.UnicodeUTF8))
        self.PSDCheckBox.setText(QtGui.QApplication.translate("ScopeWindow", "PSD", None, QtGui.QApplication.UnicodeUTF8))
        self.x_autoscaleCheckBox.setText(QtGui.QApplication.translate("ScopeWindow", "autoscale X", None, QtGui.QApplication.UnicodeUTF8))
        self.y_autoscaleCheckBox.setText(QtGui.QApplication.translate("ScopeWindow", "autoscale Y", None, QtGui.QApplication.UnicodeUTF8))
        self.autoscaleCheckBox.setText(QtGui.QApplication.translate("ScopeWindow", "autoscale", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("ScopeWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

from guiqwt.plot import CurveWidget
