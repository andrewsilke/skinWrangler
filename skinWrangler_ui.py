# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skinWrangler.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# _______________________________________________________________________
# April 2024 update:                        UPDATED to work in Maya2025+
#
# dropped: Qt4-Support ( removed Qt.py from package )
# removed: *.ui -File
# fonts now scale by maya_dpi
# _______________________________________________________________________

import os

try:
    from PySide6.QtCore import *
    from PySide6.QtGui import *
    from PySide6.QtWidgets import *
    from PySide6 import QtWidgets
    from PySide6 import QtGui
except:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2 import QtWidgets
    from PySide2 import QtGui

import maya.cmds as cmds

# DPI Scaling ----------------------------------
def currentScreen():
    """Gets current screen.

    :rtype: :class:`QRect`
    """
    return QtWidgets.QApplication.screenAt(QtGui.QCursor.pos())

def dpiMult():
    # todo: Replace with a Host agnostic version
    #  Maya has a different way of getting DPI compared to QT where it doesn't modify QT
    # or at least it's undocumented.
    scaleFactor = os.getenv("ZOO_QT_SCALE_FACTOR")
    if scaleFactor is not None:
        return float(scaleFactor)
    try:
        dpi = cmds.mayaDpiSetting(query=True, realScaleValue=True)
    # AttributeError is raised on OSX because mayaDPISetting doesn't exist, ImportError for non maya
    except (ImportError, AttributeError):
        screen = currentScreen()
        logicalY = 96
        if screen is not None:
            logicalY = screen.logicalDotsPerInch()
        dpi = max(1, float(logicalY) / float(96))
    os.environ["ZOO_QT_SCALE_FACTOR"] = str(dpi)
    return dpi

dpi = dpiMult()

# Skin Wrangler Dialog ----------------------------------

class Ui_skinWranglerDlg(object):

    def setupUi(self, skinWranglerDlg):
        if not skinWranglerDlg.objectName():
            skinWranglerDlg.setObjectName(u"skinWranglerDlg")
        skinWranglerDlg.resize(356, 823)
        self.verticalLayout = QVBoxLayout(skinWranglerDlg)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(skinWranglerDlg)
        self.groupBox.setObjectName(u"groupBox")
        font = self.groupBox.font()
        font.setBold(True)
        font.setWeight(QFont.Bold)  # 75
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.msh = QLabel(self.groupBox)
        self.msh.setObjectName(u"msh")
        font1 = self.msh.font()
        font.setBold(True)
        font.setWeight(QFont.Bold)  # 75
        self.msh.setFont(font1)

        self.gridLayout_2.addWidget(self.msh, 0, 0, 1, 1)

        self.skn = QLabel(self.groupBox)
        self.skn.setObjectName(u"skn")
        self.skn.setFont(font1)

        self.gridLayout_2.addWidget(self.skn, 0, 2, 1, 1)

        self.vtx = QLabel(self.groupBox)
        self.vtx.setObjectName(u"vtx")
        self.vtx.setFont(font1)

        self.gridLayout_2.addWidget(self.vtx, 0, 4, 1, 1)

        self.mshLBL = QLabel(self.groupBox)
        self.mshLBL.setObjectName(u"mshLBL")
        font2 = self.mshLBL.font()
        font2.setBold(False)

        font2.setWeight(QFont.Normal)  # 50 Medium , Normal, Light <---

        self.mshLBL.setFont(font2)

        self.gridLayout_2.addWidget(self.mshLBL, 1, 0, 1, 1)

        self.sknLBL = QLabel(self.groupBox)
        self.sknLBL.setObjectName(u"sknLBL")
        self.sknLBL.setFont(font2)

        self.gridLayout_2.addWidget(self.sknLBL, 1, 2, 1, 1)

        self.vtxLBL = QLabel(self.groupBox)
        self.vtxLBL.setObjectName(u"vtxLBL")
        self.vtxLBL.setFont(font2)

        self.gridLayout_2.addWidget(self.vtxLBL, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selGrowBTN = QPushButton(self.groupBox)
        self.selGrowBTN.setObjectName(u"selGrowBTN")
        self.selGrowBTN.setMinimumSize(QSize(50, 0))
        self.selGrowBTN.setFont(font1)

        self.horizontalLayout.addWidget(self.selGrowBTN)

        self.selShrinkBTN = QPushButton(self.groupBox)
        self.selShrinkBTN.setObjectName(u"selShrinkBTN")
        self.selShrinkBTN.setMinimumSize(QSize(50, 0))
        self.selShrinkBTN.setFont(font1)

        self.horizontalLayout.addWidget(self.selShrinkBTN)

        self.selShellBTN = QPushButton(self.groupBox)
        self.selShellBTN.setObjectName(u"selShellBTN")
        self.selShellBTN.setMinimumSize(QSize(50, 0))
        self.selShellBTN.setFont(font1)

        self.horizontalLayout.addWidget(self.selShellBTN)

        self.selLoopBTN = QPushButton(self.groupBox)
        self.selLoopBTN.setObjectName(u"selLoopBTN")
        self.selLoopBTN.setMinimumSize(QSize(50, 0))
        self.selLoopBTN.setFont(font1)

        self.horizontalLayout.addWidget(self.selLoopBTN)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.selPointsEffectedBTN = QPushButton(self.groupBox)
        self.selPointsEffectedBTN.setObjectName(u"selPointsEffectedBTN")
        self.selPointsEffectedBTN.setFont(font1)

        self.verticalLayout_2.addWidget(self.selPointsEffectedBTN)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(skinWranglerDlg)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 0, 6, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.skinMaxInfLBL = QLabel(self.groupBox_2)
        self.skinMaxInfLBL.setObjectName(u"skinMaxInfLBL")
        self.skinMaxInfLBL.setFont(font2)

        self.gridLayout_3.addWidget(self.skinMaxInfLBL, 0, 7, 1, 1)

        self.skinAlgoLBL = QLabel(self.groupBox_2)
        self.skinAlgoLBL.setObjectName(u"skinAlgoLBL")
        self.skinAlgoLBL.setFont(font2)

        self.gridLayout_3.addWidget(self.skinAlgoLBL, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 5, 1, 1)

        self.skinNormalCMB = QComboBox(self.groupBox_2)
        self.skinNormalCMB.addItem("")
        self.skinNormalCMB.addItem("")
        self.skinNormalCMB.addItem("")
        self.skinNormalCMB.setObjectName(u"skinNormalCMB")
        self.skinNormalCMB.setMaximumSize(QSize(16777215, 20))
        font3 = self.skinNormalCMB.font()
        self.skinNormalCMB.setFont(font3)

        self.gridLayout_3.addWidget(self.skinNormalCMB, 0, 4, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.weightZeroBTN = QPushButton(self.groupBox_2)
        self.weightZeroBTN.setObjectName(u"weightZeroBTN")
        self.weightZeroBTN.setFont(font1)

        self.horizontalLayout_2.addWidget(self.weightZeroBTN)

        self.weightHalfBTN = QPushButton(self.groupBox_2)
        self.weightHalfBTN.setObjectName(u"weightHalfBTN")
        self.weightHalfBTN.setFont(font1)

        self.horizontalLayout_2.addWidget(self.weightHalfBTN)

        self.weightFullBTN = QPushButton(self.groupBox_2)
        self.weightFullBTN.setObjectName(u"weightFullBTN")
        self.weightFullBTN.setFont(font1)

        self.horizontalLayout_2.addWidget(self.weightFullBTN)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.setWeightBTN = QPushButton(self.groupBox_2)
        self.setWeightBTN.setObjectName(u"setWeightBTN")
        self.setWeightBTN.setMinimumSize(QSize(90, 0))
        self.setWeightBTN.setFont(font)

        self.gridLayout.addWidget(self.setWeightBTN, 0, 0, 1, 1)

        self.plusWeightBTN = QPushButton(self.groupBox_2)
        self.plusWeightBTN.setObjectName(u"plusWeightBTN")
        self.plusWeightBTN.setMaximumSize(QSize(25, 16777215))

        self.gridLayout.addWidget(self.plusWeightBTN, 0, 3, 1, 1)

        self.minusWeightBTN = QPushButton(self.groupBox_2)
        self.minusWeightBTN.setObjectName(u"minusWeightBTN")
        self.minusWeightBTN.setMaximumSize(QSize(25, 16777215))

        self.gridLayout.addWidget(self.minusWeightBTN, 0, 4, 1, 1)

        self.setWeightSpin = QDoubleSpinBox(self.groupBox_2)
        self.setWeightSpin.setObjectName(u"setWeightSpin")
        self.setWeightSpin.setMinimumSize(QSize(60, 0))
        self.setWeightSpin.setFont(font)
        self.setWeightSpin.setSingleStep(0.010000000000000)
        self.setWeightSpin.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.setWeightSpin, 0, 2, 1, 1)

        self.scaleWeightBTN = QPushButton(self.groupBox_2)
        self.scaleWeightBTN.setObjectName(u"scaleWeightBTN")
        self.scaleWeightBTN.setEnabled(False)
        self.scaleWeightBTN.setFont(font)

        self.gridLayout.addWidget(self.scaleWeightBTN, 1, 0, 1, 1)

        self.scaleWeightSpin = QDoubleSpinBox(self.groupBox_2)
        self.scaleWeightSpin.setObjectName(u"scaleWeightSpin")
        self.scaleWeightSpin.setEnabled(False)
        self.scaleWeightSpin.setFont(font)
        self.scaleWeightSpin.setSingleStep(0.010000000000000)
        self.scaleWeightSpin.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.scaleWeightSpin, 1, 2, 1, 1)

        self.multWeightBTN = QPushButton(self.groupBox_2)
        self.multWeightBTN.setObjectName(u"multWeightBTN")
        self.multWeightBTN.setEnabled(False)
        self.multWeightBTN.setMaximumSize(QSize(25, 16777215))

        self.gridLayout.addWidget(self.multWeightBTN, 1, 3, 1, 1)

        self.pasteBTN = QPushButton(self.groupBox_2)
        self.pasteBTN.setObjectName(u"pasteBTN")
        self.pasteBTN.setEnabled(False)
        self.pasteBTN.setMinimumSize(QSize(0, 0))
        self.pasteBTN.setMaximumSize(QSize(70, 16777215))
        self.pasteBTN.setFont(font)

        self.gridLayout.addWidget(self.pasteBTN, 2, 2, 1, 1)

        self.refreshBTN = QPushButton(self.groupBox_2)
        self.refreshBTN.setObjectName(u"refreshBTN")
        self.refreshBTN.setMaximumSize(QSize(25, 16777215))

        self.gridLayout.addWidget(self.refreshBTN, 2, 4, 1, 1)

        self.divWeightBTN = QPushButton(self.groupBox_2)
        self.divWeightBTN.setObjectName(u"divWeightBTN")
        self.divWeightBTN.setEnabled(False)
        self.divWeightBTN.setMaximumSize(QSize(25, 16777215))

        self.gridLayout.addWidget(self.divWeightBTN, 1, 4, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.setAverageWeightBTN = QPushButton(self.groupBox_2)
        self.setAverageWeightBTN.setObjectName(u"setAverageWeightBTN")
        self.setAverageWeightBTN.setFont(font)

        self.horizontalLayout_8.addWidget(self.setAverageWeightBTN)

        self.copyBTN = QPushButton(self.groupBox_2)
        self.copyBTN.setObjectName(u"copyBTN")
        self.copyBTN.setMaximumSize(QSize(16777215, 16777215))
        self.copyBTN.setFont(font)
        self.copyBTN.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.copyBTN)

        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.filterBTN = QPushButton(self.groupBox_2)
        self.filterBTN.setObjectName(u"filterBTN")
        self.filterBTN.setMaximumSize(QSize(dpi * 55, dpi * 20))

        self.horizontalLayout_6.addWidget(self.filterBTN)

        self.filterLINE = QLineEdit(self.groupBox_2)
        self.filterLINE.setObjectName(u"filterLINE")
        self.filterLINE.setFont(font2)

        self.horizontalLayout_6.addWidget(self.filterLINE)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.jointLST = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem = QTreeWidgetItem()
        #         __qtreewidgetitem.setFont(1, font1);
        __qtreewidgetitem.setText(0, u"JOINT")
        #         __qtreewidgetitem.setFont(0, font1);
        self.jointLST.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.jointLST)
        #         __qtreewidgetitem1.setFont(1, font2);
        #         __qtreewidgetitem1.setFont(0, font);
        self.jointLST.setObjectName(u"jointLST")
        font4 = self.jointLST.font()
        font4.setBold(True)
        font4.setWeight(QFont.Bold)  # 75
        self.jointLST.setFont(font4)
        self.jointLST.setLineWidth(1)
        self.jointLST.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.jointLST.setIconSize(QSize(17, 17))
        self.jointLST.setRootIsDecorated(False)
        self.jointLST.setItemsExpandable(False)
        self.jointLST.setColumnCount(2)
        self.jointLST.header().setVisible(True)
        self.jointLST.header().setDefaultSectionSize(120)

        self.verticalLayout_3.addWidget(self.jointLST)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listAllCHK = QCheckBox(self.groupBox_2)
        self.listAllCHK.setObjectName(u"listAllCHK")
        self.listAllCHK.setFont(font3)
        self.listAllCHK.setChecked(True)

        self.horizontalLayout_4.addWidget(self.listAllCHK)

        self.nameSpaceCHK = QCheckBox(self.groupBox_2)
        self.nameSpaceCHK.setObjectName(u"nameSpaceCHK")
        self.nameSpaceCHK.setFont(font1)
        self.nameSpaceCHK.setChecked(True)

        self.horizontalLayout_4.addWidget(self.nameSpaceCHK)

        self.longNamesCHK = QCheckBox(self.groupBox_2)
        self.longNamesCHK.setObjectName(u"longNamesCHK")
        self.longNamesCHK.setEnabled(False)
        self.longNamesCHK.setFont(font3)

        self.horizontalLayout_4.addWidget(self.longNamesCHK)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.dynAnnotationCHK = QCheckBox(self.groupBox_2)
        self.dynAnnotationCHK.setObjectName(u"dynAnnotationCHK")
        self.dynAnnotationCHK.setFont(font3)
        self.dynAnnotationCHK.setChecked(False)

        self.horizontalLayout_10.addWidget(self.dynAnnotationCHK)

        self.labelJointsCHK = QCheckBox(self.groupBox_2)
        self.labelJointsCHK.setObjectName(u"labelJointsCHK")
        self.labelJointsCHK.setEnabled(False)
        self.labelJointsCHK.setFont(font3)

        self.horizontalLayout_10.addWidget(self.labelJointsCHK)

        self.showLocksCHK = QCheckBox(self.groupBox_2)
        self.showLocksCHK.setObjectName(u"showLocksCHK")
        self.showLocksCHK.setFont(font1)

        self.horizontalLayout_10.addWidget(self.showLocksCHK)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.tabs = QTabWidget(skinWranglerDlg)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setEnabled(True)
        # self.tabs.setMaximumSize(QSize(16777215, 85))
        self.tabs.setFixedHeight(dpi * 60)

        font5 = self.tabs.font()
        font5.setBold(True)
        font5.setWeight(QFont.Bold)  # 75
        self.tabs.setFont(font5)
        self.tab_3 = QWidget()

        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.removeUnusedBTN = QPushButton(self.tab_3)
        self.removeUnusedBTN.setObjectName(u"removeUnusedBTN")
        self.removeUnusedBTN.setFont(font1)  # font

        self.horizontalLayout_5.addWidget(self.removeUnusedBTN)

        self.clampInfBTN = QPushButton(self.tab_3)
        self.clampInfBTN.setObjectName(u"clampInfBTN")
        self.clampInfBTN.setFont(font1)  # font

        self.horizontalLayout_5.addWidget(self.clampInfBTN)

        self.clampInfSPIN = QSpinBox(self.tab_3)
        self.clampInfSPIN.setObjectName(u"clampInfSPIN")
        self.clampInfSPIN.setValue(4)
        self.clampInfSPIN.setFont(font1)  # font
        self.clampInfSPIN.setFixedSize(QSize(dpi * 40, dpi * 20))

        self.horizontalLayout_5.addWidget(self.clampInfSPIN)

        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.addJntBTN = QPushButton(self.tab_3)
        self.addJntBTN.setObjectName(u"addJntBTN")
        self.addJntBTN.setFont(font1)  # font

        self.horizontalLayout_7.addWidget(self.addJntBTN)

        self.bindPoseBTN = QPushButton(self.tab_3)
        self.bindPoseBTN.setObjectName(u"bindPoseBTN")
        self.bindPoseBTN.setFont(font1)  # font

        self.horizontalLayout_7.addWidget(self.bindPoseBTN)

        self.selectVertsWithInfBTN = QPushButton(self.tab_3)
        self.selectVertsWithInfBTN.setObjectName(u"selectVertsWithInfBTN")
        self.selectVertsWithInfBTN.setFont(font1)  # font

        self.horizontalLayout_7.addWidget(self.selectVertsWithInfBTN)

        self.selectVertsWithInfSPIN = QSpinBox(self.tab_3)
        self.selectVertsWithInfSPIN.setObjectName(u"selectVertsWithInfSPIN")
        self.selectVertsWithInfSPIN.setValue(4)
        self.selectVertsWithInfSPIN.setFont(font1)  # font
        self.selectVertsWithInfSPIN.setFixedSize(QSize(dpi * 60, dpi * 20))

        self.horizontalLayout_7.addWidget(self.selectVertsWithInfSPIN)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.tabs.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_7 = QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.jointOnBboxCenterBTN = QPushButton(self.tab_4)
        self.jointOnBboxCenterBTN.setObjectName(u"jointOnBboxCenterBTN")
        self.jointOnBboxCenterBTN.setCheckable(True)

        self.verticalLayout_7.addWidget(self.jointOnBboxCenterBTN)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.rigidShellsBtn = QPushButton(self.tab_4)
        self.rigidShellsBtn.setObjectName(u"rigidShellsBtn")

        self.horizontalLayout_14.addWidget(self.rigidShellsBtn)

        self.avgOptionCHK = QCheckBox(self.tab_4)
        self.avgOptionCHK.setObjectName(u"avgOptionCHK")
        font6 = self.avgOptionCHK.font()
        self.avgOptionCHK.setFont(font6)

        self.horizontalLayout_14.addWidget(self.avgOptionCHK)

        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.tabs.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(False)
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.bButton = QPushButton(self.tab)
        self.bButton.setObjectName(u"bButton")

        self.horizontalLayout_9.addWidget(self.bButton)

        self.ubButton = QPushButton(self.tab)
        self.ubButton.setObjectName(u"ubButton")

        self.horizontalLayout_9.addWidget(self.ubButton)

        self.bDeleteButton = QPushButton(self.tab)
        self.bDeleteButton.setObjectName(u"bDeleteButton")

        self.horizontalLayout_9.addWidget(self.bDeleteButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.ubSmoothWeightsCheckbox = QCheckBox(self.tab)
        self.ubSmoothWeightsCheckbox.setObjectName(u"ubSmoothWeightsCheckbox")

        self.horizontalLayout_9.addWidget(self.ubSmoothWeightsCheckbox)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.bSelectVertsButton = QPushButton(self.tab)
        self.bSelectVertsButton.setObjectName(u"bSelectVertsButton")

        self.horizontalLayout_11.addWidget(self.bSelectVertsButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.ubDeleteSkinclusterCheckbox = QCheckBox(self.tab)
        self.ubDeleteSkinclusterCheckbox.setObjectName(u"ubDeleteSkinclusterCheckbox")
        self.ubDeleteSkinclusterCheckbox.setChecked(True)

        self.horizontalLayout_11.addWidget(self.ubDeleteSkinclusterCheckbox)

        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.tabs.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(False)
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sfDirectoryEdit = QLineEdit(self.tab_2)
        self.sfDirectoryEdit.setObjectName(u"sfDirectoryEdit")

        self.horizontalLayout_12.addWidget(self.sfDirectoryEdit)

        self.sfDirectoryButton = QPushButton(self.tab_2)
        self.sfDirectoryButton.setObjectName(u"sfDirectoryButton")
        self.sfDirectoryButton.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_12.addWidget(self.sfDirectoryButton)

        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.sfSaveButton = QPushButton(self.tab_2)
        self.sfSaveButton.setObjectName(u"sfSaveButton")
        self.sfSaveButton.setMinimumSize(QSize(0, 0))
        self.sfSaveButton.setMaximumSize(QSize(9999, 9999))

        self.horizontalLayout_13.addWidget(self.sfSaveButton)

        self.lfLoadButton = QPushButton(self.tab_2)
        self.lfLoadButton.setObjectName(u"lfLoadButton")
        self.lfLoadButton.setMinimumSize(QSize(0, 0))
        self.lfLoadButton.setMaximumSize(QSize(9999, 9999))

        self.horizontalLayout_13.addWidget(self.lfLoadButton)

        self.lfRemapperButton = QPushButton(self.tab_2)
        self.lfRemapperButton.setObjectName(u"lfRemapperButton")
        # self.lfRemapperButton.setMaximumSize(QSize(102, 16777215))
        self.lfRemapperButton.setMinimumSize(QSize(0, 0))
        self.lfRemapperButton.setMaximumSize(QSize(9999, 9999))

        self.horizontalLayout_13.addWidget(self.lfRemapperButton)

        self.lfUseWorldspacePosCheckbox = QCheckBox(self.tab_2)
        self.lfUseWorldspacePosCheckbox.setObjectName(u"lfUseWorldspacePosCheckbox")
        self.lfUseWorldspacePosCheckbox.setEnabled(False)
        self.lfUseWorldspacePosCheckbox.setFont(font2)

        self.horizontalLayout_13.addWidget(self.lfUseWorldspacePosCheckbox)

        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.tabs.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabs)

        self.retranslateUi(skinWranglerDlg)

        self.tabs.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(skinWranglerDlg)

    def retranslateUi(self, skinWranglerDlg):
        skinWranglerDlg.setWindowTitle(u"skinWrangler")
        self.groupBox.setTitle(u"VERT SELECTION")
        self.msh.setText(u"MSH:")
        self.skn.setText(u"SKN:")
        self.vtx.setText(u"VTX:")
        self.mshLBL.setText(u"None")
        self.sknLBL.setText(u"None")
        self.vtxLBL.setText(u"None")
        self.selGrowBTN.setText(u"GROW")
        self.selShrinkBTN.setText(u"SHRINK")
        self.selShellBTN.setText(u"SHELL")
        self.selLoopBTN.setText(u"LOOP")
        self.selPointsEffectedBTN.setText(u"VERTS EFFECTED BY SELECTED JOINTS")
        self.groupBox_2.setTitle(u"SKINNING")
        self.label_2.setText(u"NORMALIZATION:  ")
        self.label_3.setText(u"MAX INF:  ")
        self.label_4.setText(u"SKIN:  ")
        self.skinMaxInfLBL.setText(u"None")
        self.skinAlgoLBL.setText(u"None")
        self.skinNormalCMB.setItemText(0, u"None")
        self.skinNormalCMB.setItemText(1, u"Interactive")
        self.skinNormalCMB.setItemText(2, u"Post")

        self.weightZeroBTN.setText(u"0.0")
        self.weightHalfBTN.setText(u"0.5")
        self.weightFullBTN.setText(u"1.0")
        self.setWeightBTN.setToolTip(u"Explicitely set the weight value")
        self.setWeightBTN.setText(u"SET WEIGHT")
        self.plusWeightBTN.setToolTip(u"Add value to current weight for selected joint")
        self.plusWeightBTN.setText(u"+")
        self.minusWeightBTN.setToolTip(u"Subtract value to current weight for selected joint")
        self.minusWeightBTN.setText(u"-")
        self.scaleWeightBTN.setText(u"SCALE WEIGHT")
        self.multWeightBTN.setText(u"*")
        self.pasteBTN.setToolTip(u"Paste stored skinning weights")
        self.pasteBTN.setText(u"PASTE")
        self.refreshBTN.setToolTip(u"Used to refresh the weight list")
        self.refreshBTN.setText(u"<")
        self.divWeightBTN.setText(u"/")
        self.setAverageWeightBTN.setText(u"AVG")
        self.copyBTN.setToolTip(u"Copy/store skinning info for current selection")
        self.copyBTN.setText(u"COPY")
        self.label.setText(u"JOINT INFLUENCE LIST:")
        self.filterBTN.setText(u"FILTER")
        ___qtreewidgetitem = self.jointLST.headerItem()
        ___qtreewidgetitem.setText(1, u"AVG WEIGHT")

        __sortingEnabled = self.jointLST.isSortingEnabled()
        self.jointLST.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.jointLST.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, u"joint01")
        self.jointLST.setSortingEnabled(__sortingEnabled)

        self.listAllCHK.setText(u"List all influences")
        self.nameSpaceCHK.setText(u"strip nameSpace")
        self.longNamesCHK.setText(u"longNames")
        self.dynAnnotationCHK.setText(u"Dynamic annotation")
        self.labelJointsCHK.setText(u"Label joints")
        self.showLocksCHK.setText(u"show locks")
        self.removeUnusedBTN.setToolTip(u"Maya remove unused influences command")
        self.removeUnusedBTN.setText(u"REMOVE UNUSED INFS")
        self.clampInfBTN.setToolTip(u"Trims down the smallest values and re-normalizes")
        self.clampInfBTN.setText(u"CLAMP MAX INFS")
        self.addJntBTN.setText(u"ADD JNT")
        self.bindPoseBTN.setText(u"BIND POSE")
        self.selectVertsWithInfBTN.setToolTip(u"Select vertices that have more influences than the number")
        self.selectVertsWithInfBTN.setText(u"SEL VTX WITH >")
        self.selectVertsWithInfSPIN.setSuffix(u" INF")
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), u"SKIN UTILS")
        self.jointOnBboxCenterBTN.setText(u"MAKE JOINT ON BBOX CENTER")
        self.rigidShellsBtn.setText(u"MAKE RIGID SHELLS")
        self.avgOptionCHK.setToolTip(u"Uses custom code to average skinning,\nrespecting the max influences")
        self.avgOptionCHK.setText(u"Calc avg with max inf (no hammer)")
        self.tabs.setTabText(self.tabs.indexOf(self.tab_4), u"TOOLBOX")
        self.bButton.setToolTip(u"Bake skinning information on selected meshes")
        self.bButton.setText(u"BAKE")
        self.ubButton.setToolTip(u"Transfer baked information back to the skinCluster")
        self.ubButton.setText(u"UNBAKE")
        self.bDeleteButton.setToolTip(u"Bake skinning information on selected meshes")
        self.bDeleteButton.setText(u"CLEAR BAKING")
        self.ubSmoothWeightsCheckbox.setToolTip(
            u"<html><head/><body><p>(SLOW) Smooth vertices with no influences across the mesh topology.</p><p>To be used when the mesh topology changed (eg. Mesh got smoothed)</p></body></html>")
        self.ubSmoothWeightsCheckbox.setText(u"Smooth")
        self.bSelectVertsButton.setToolTip(u"Select vertices that contain baked skinning information")
        self.bSelectVertsButton.setText(u"SELECT BAKED VERTS")
        self.ubDeleteSkinclusterCheckbox.setToolTip(u"Delete current skinCluster when unbacking")
        self.ubDeleteSkinclusterCheckbox.setText(u"Delete cluster")
        self.tabs.setTabText(self.tabs.indexOf(self.tab), u"BAKE")
        self.sfDirectoryButton.setText(u"...")
        self.sfSaveButton.setText(u"Save")
        self.lfLoadButton.setToolTip(u"Load single or multiple .weight files on the selected geometry")
        self.lfLoadButton.setText(u"Load")
        self.lfRemapperButton.setToolTip(u"Load single or multiple .weight files on the selected geometry")
        self.lfRemapperButton.setText(u"Load->Remap")
        self.lfUseWorldspacePosCheckbox.setText(u"worldSpace")
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), u"SAVE/LOAD")



