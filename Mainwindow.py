# -*- coding=UTF-8  -*-
"""
作者: SVehicle
时间: 2021年11月10日
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class MainWindow(QWidget):        # 让整个窗口作为标签页
    def __init__(self):
        super(QWidget, self).__init__()

        self.setWindowTitle('日志分析工具')
        self.resize(1300, 590)
        self.setMinimumWidth(1300)
        self.setMaximumWidth(1300)
        self.setMaximumHeight(590)
        self.setMaximumHeight(590)

        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(10, 10, 1281, 520)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()

        self.tabWidget.addTab(self.tab_1, "日志曲线")
        self.tabWidget.addTab(self.tab_2, "飞行航线")
        self.tabWidget.addTab(self.tab_3, "日志参数")

        self.Tab_1()

    def Tab_1(self):
        frame = QFrame(self.tab_1)
        frame.setGeometry(10, 5, 158, 241)
        frame.setFrameShape(QFrame.Box)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setObjectName("frame")
        frame_2 = QFrame(self.tab_1)
        frame_2.setGeometry(10, 248, 158, 211)
        frame_2.setFrameShape(QFrame.Box)
        frame_2.setFrameShadow(QFrame.Sunken)
        frame_2.setObjectName("frame_2")
        frame_3 = QFrame(self.tab_1)
        frame_3.setGeometry(171, 5, 870, 451)
        frame_3.setFrameShape(QFrame.Box)
        frame_3.setFrameShadow(QFrame.Plain)

        verticalLayoutWidget = QWidget()
        verticalLayoutWidget.setGeometry(0, 0, 158, 211)
        verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        verticalLayout = QVBoxLayout(verticalLayoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        frame_2.setLayout(verticalLayout)
        checkBox_1 = QCheckBox(verticalLayoutWidget)
        checkBox_1.setText('姿态控制数据')
        verticalLayout.addWidget(checkBox_1, 0, Qt.AlignHCenter)

        checkBox_2 = QCheckBox(verticalLayoutWidget)
        checkBox_2.setText('偏航控制数据')
        verticalLayout.addWidget(checkBox_2, 0, Qt.AlignHCenter)

        checkBox_3 = QCheckBox(verticalLayoutWidget)
        checkBox_3.setText('电机控制数据')
        verticalLayout.addWidget(checkBox_3)
        verticalLayout.addWidget(checkBox_3, 0, Qt.AlignHCenter)

        checkBox_4 = QCheckBox(verticalLayoutWidget)
        checkBox_4.setText('震动数据    ')
        verticalLayout.addWidget(checkBox_4, 0, Qt.AlignHCenter)

        checkBox_5 = QCheckBox(verticalLayoutWidget)
        checkBox_5.setText('高度控制数据')
        verticalLayout.addWidget(checkBox_5, 0, Qt.AlignHCenter)

        buttonGroup = QButtonGroup(self)
        buttonGroup.setObjectName("buttonGroup")
        buttonGroup.addButton(checkBox_1)
        buttonGroup.addButton(checkBox_2)
        buttonGroup.addButton(checkBox_3)
        buttonGroup.addButton(checkBox_4)
        buttonGroup.addButton(checkBox_5)

        horizontalLayoutWidget = QWidget(self)
        horizontalLayoutWidget.setGeometry(279, 535, 731, 41)
        horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        horizontalLayout = QHBoxLayout(horizontalLayoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setObjectName("horizontalLayout")

        pushButton_1 = QPushButton(horizontalLayoutWidget)
        pushButton_2 = QPushButton(horizontalLayoutWidget)
        pushButton_3 = QPushButton(horizontalLayoutWidget)
        pushButton_4 = QPushButton(horizontalLayoutWidget)
        pushButton_5 = QPushButton(horizontalLayoutWidget)
        pushButton_6 = QPushButton(horizontalLayoutWidget)

        pushButton_1.setText("打开文件")
        pushButton_2.setText("清除图表")
        pushButton_3.setText("加载航点文件")
        pushButton_4.setText("清楚航路点")
        pushButton_5.setText("转成Log文")
        pushButton_6.setText("转成Matlab")

        horizontalLayout.addWidget(pushButton_1)
        horizontalLayout.addWidget(pushButton_2)
        horizontalLayout.addWidget(pushButton_3)
        horizontalLayout.addWidget(pushButton_4)
        horizontalLayout.addWidget(pushButton_5)
        horizontalLayout.addWidget(pushButton_6)

        # 三个复选框 + 运行时间
        horizontalLayoutWidget_2 = QWidget(self.tab_1)
        horizontalLayoutWidget_2.setGeometry(171, 455, 900, 31)
        horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        horizontalLayout_2 = QHBoxLayout(horizontalLayoutWidget_2)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")

        checkBox_6 = QCheckBox(horizontalLayoutWidget_2)
        checkBox_7 = QCheckBox(horizontalLayoutWidget_2)
        checkBox_8 = QCheckBox (horizontalLayoutWidget_2)

        checkBox_6.setText("显示模式状态")
        checkBox_7.setText("显示加锁状态")
        checkBox_8.setText("显示故障保护")

        horizontalLayout_2.addWidget(checkBox_6)
        horizontalLayout_2.addWidget(checkBox_7)
        horizontalLayout_2.addWidget(checkBox_8)

        spacerItem = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout_2.addItem(spacerItem)
        horizontalLayout_3 = QHBoxLayout()
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        label = QLabel(horizontalLayoutWidget_2)
        label.setText("运行时间：")
        horizontalLayout_3.addWidget(label)
        lineEdit = QLineEdit(horizontalLayoutWidget_2)
        lineEdit.setObjectName("lineEdit")
        lineEdit.setFrame(False)
        horizontalLayout_3.addWidget(lineEdit)
        horizontalLayout_2.addLayout(horizontalLayout_3)

        treeWidget = QTreeWidget(frame)
        treeWidget.setGeometry(3, 2, 150, 235)      # (10, 5, 158, 241)
        treeWidget.setFrameShape(QFrame.Box)
        treeWidget.setFrameShadow(QFrame.Plain)
        treeWidget.headerItem().setText(0, '数据选项')
        # treeWidget.header().setMinimumSectionSize(135)  # 其实就是这一句话，要添加，尽量把这一列的尺寸设置大一点，就好了
        root1 = QTreeWidgetItem(treeWidget)
        treeWidget.setHeaderItem(root1)
        root1.setText(0, '姿态数据')
        root1.setCheckState(0, Qt.Unchecked)
        child1 = QTreeWidgetItem(root1)
        child1.setText(0, '指令滚转角')
        child1.setCheckState(0, Qt.Unchecked)
        child2 = QTreeWidgetItem(root1)
        child2.setText(0, '滚转角')
        child2.setCheckState(0, Qt.Unchecked)
        child3 = QTreeWidgetItem(root1)
        child3.setText(0, '指令俯仰角')
        child3.setCheckState(0, Qt.Unchecked)
        child1.checkState(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

