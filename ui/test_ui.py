# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 571)
        MainWindow.setMinimumSize(QtCore.QSize(700, 571))
        MainWindow.setMaximumSize(QtCore.QSize(700, 571))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("color: rgb(162, 162, 162);\n"
"background-color: rgb(30, 39, 44);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 55, 682, 439))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.vkloginPage = QtWidgets.QWidget()
        self.vkloginPage.setObjectName("vkloginPage")
        self.layoutWidget = QtWidgets.QWidget(self.vkloginPage)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 30, 302, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 23)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.vkImage = QtWidgets.QLabel(self.layoutWidget)
        self.vkImage.setEnabled(True)
        self.vkImage.setMinimumSize(QtCore.QSize(100, 100))
        self.vkImage.setMaximumSize(QtCore.QSize(100, 100))
        self.vkImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vkImage.setMidLineWidth(2)
        self.vkImage.setText("")
        self.vkImage.setScaledContents(True)
        self.vkImage.setObjectName("vkImage")
        self.gridLayout.addWidget(self.vkImage, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setStyleSheet("background-color: rgb(32, 42, 48);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(32, 42, 48);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 35))
        self.pushButton_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_4.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignHCenter)
        self.ResultOfLogin = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultOfLogin.sizePolicy().hasHeightForWidth())
        self.ResultOfLogin.setSizePolicy(sizePolicy)
        self.ResultOfLogin.setMinimumSize(QtCore.QSize(200, 50))
        self.ResultOfLogin.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.ResultOfLogin.setFont(font)
        self.ResultOfLogin.setStyleSheet("")
        self.ResultOfLogin.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ResultOfLogin.setLineWidth(2)
        self.ResultOfLogin.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ResultOfLogin.setWordWrap(False)
        self.ResultOfLogin.setIndent(0)
        self.ResultOfLogin.setObjectName("ResultOfLogin")
        self.verticalLayout.addWidget(self.ResultOfLogin, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.vkloginPage)
        self.LogsPage = QtWidgets.QWidget()
        self.LogsPage.setMinimumSize(QtCore.QSize(0, 502))
        self.LogsPage.setMaximumSize(QtCore.QSize(746, 16777215))
        self.LogsPage.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.LogsPage.setToolTipDuration(0)
        self.LogsPage.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.LogsPage.setStyleSheet("border-color: rgb(138, 226, 52);")
        self.LogsPage.setObjectName("LogsPage")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.LogsPage)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 10, 681, 421))
        self.plainTextEdit.setStyleSheet("background-color: rgb(35, 46, 52);\n"
"")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.layoutWidget1 = QtWidgets.QWidget(self.LogsPage)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 470, 681, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget.addWidget(self.LogsPage)
        self.LikesPage = QtWidgets.QWidget()
        self.LikesPage.setObjectName("LikesPage")
        self.ResultSaveUrl = QtWidgets.QLabel(self.LikesPage)
        self.ResultSaveUrl.setGeometry(QtCore.QRect(100, 110, 471, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ResultSaveUrl.setFont(font)
        self.ResultSaveUrl.setText("")
        self.ResultSaveUrl.setAlignment(QtCore.Qt.AlignCenter)
        self.ResultSaveUrl.setObjectName("ResultSaveUrl")
        self.layoutWidget2 = QtWidgets.QWidget(self.LikesPage)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 30, 671, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LabelLikesUrl = QtWidgets.QLineEdit(self.layoutWidget2)
        self.LabelLikesUrl.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        self.LabelLikesUrl.setFont(font)
        self.LabelLikesUrl.setStyleSheet("background-color: rgb(35, 46, 52);")
        self.LabelLikesUrl.setObjectName("LabelLikesUrl")
        self.horizontalLayout.addWidget(self.LabelLikesUrl)
        self.SaveUrlButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.SaveUrlButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.SaveUrlButton.setObjectName("SaveUrlButton")
        self.horizontalLayout.addWidget(self.SaveUrlButton)
        self.LikesCount = QtWidgets.QLineEdit(self.LikesPage)
        self.LikesCount.setGeometry(QtCore.QRect(0, 170, 121, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        self.LikesCount.setFont(font)
        self.LikesCount.setToolTipDuration(-1)
        self.LikesCount.setText("")
        self.LikesCount.setCursorPosition(0)
        self.LikesCount.setAlignment(QtCore.Qt.AlignCenter)
        self.LikesCount.setObjectName("LikesCount")
        self.ResultStartLikes = QtWidgets.QLabel(self.LikesPage)
        self.ResultStartLikes.setGeometry(QtCore.QRect(340, 180, 271, 21))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ResultStartLikes.setFont(font)
        self.ResultStartLikes.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.ResultStartLikes.setLineWidth(-1)
        self.ResultStartLikes.setMidLineWidth(0)
        self.ResultStartLikes.setText("")
        self.ResultStartLikes.setScaledContents(False)
        self.ResultStartLikes.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.ResultStartLikes.setIndent(0)
        self.ResultStartLikes.setObjectName("ResultStartLikes")
        self.StartLikes = QtWidgets.QToolButton(self.LikesPage)
        self.StartLikes.setGeometry(QtCore.QRect(130, 170, 91, 41))
        self.StartLikes.setStyleSheet("color: rgb(154, 255, 152);")
        self.StartLikes.setObjectName("StartLikes")
        self.StopLikes = QtWidgets.QToolButton(self.LikesPage)
        self.StopLikes.setGeometry(QtCore.QRect(230, 170, 91, 41))
        self.StopLikes.setStyleSheet("color: rgb(255, 121, 123);")
        self.StopLikes.setObjectName("StopLikes")
        self.layoutWidget3 = QtWidgets.QWidget(self.LikesPage)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 220, 201, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(43)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.LikesBalanceLabel = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LikesBalanceLabel.setFont(font)
        self.LikesBalanceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LikesBalanceLabel.setObjectName("LikesBalanceLabel")
        self.horizontalLayout_5.addWidget(self.LikesBalanceLabel)
        self.getBalance = QtWidgets.QPushButton(self.layoutWidget3)
        self.getBalance.setMinimumSize(QtCore.QSize(89, 20))
        self.getBalance.setMaximumSize(QtCore.QSize(91, 40))
        self.getBalance.setFocusPolicy(QtCore.Qt.NoFocus)
        self.getBalance.setObjectName("getBalance")
        self.horizontalLayout_5.addWidget(self.getBalance)
        self.layoutWidget_2 = QtWidgets.QWidget(self.LikesPage)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 360, 430, 81))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.LabelCoupon = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.LabelCoupon.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        self.LabelCoupon.setFont(font)
        self.LabelCoupon.setStyleSheet("background-color: rgb(35, 46, 52);")
        self.LabelCoupon.setObjectName("LabelCoupon")
        self.horizontalLayout_6.addWidget(self.LabelCoupon)
        self.SaveCouponButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.SaveCouponButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.SaveCouponButton.setObjectName("SaveCouponButton")
        self.horizontalLayout_6.addWidget(self.SaveCouponButton)
        self.ResultCoupon = QtWidgets.QLabel(self.layoutWidget_2)
        self.ResultCoupon.setMinimumSize(QtCore.QSize(100, 0))
        self.ResultCoupon.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ResultCoupon.setObjectName("ResultCoupon")
        self.horizontalLayout_6.addWidget(self.ResultCoupon)
        self.LikestCheckBox = QtWidgets.QCheckBox(self.LikesPage)
        self.LikestCheckBox.setGeometry(QtCore.QRect(0, 140, 161, 21))
        self.LikestCheckBox.setObjectName("LikestCheckBox")
        self.stackedWidget.addWidget(self.LikesPage)
        self.repostPage = QtWidgets.QWidget()
        self.repostPage.setObjectName("repostPage")
        self.ResultStartLikes_R = QtWidgets.QLabel(self.repostPage)
        self.ResultStartLikes_R.setGeometry(QtCore.QRect(430, 180, 191, 21))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ResultStartLikes_R.setFont(font)
        self.ResultStartLikes_R.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.ResultStartLikes_R.setLineWidth(-1)
        self.ResultStartLikes_R.setMidLineWidth(0)
        self.ResultStartLikes_R.setText("")
        self.ResultStartLikes_R.setScaledContents(False)
        self.ResultStartLikes_R.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.ResultStartLikes_R.setIndent(0)
        self.ResultStartLikes_R.setObjectName("ResultStartLikes_R")
        self.layoutWidget_9 = QtWidgets.QWidget(self.repostPage)
        self.layoutWidget_9.setGeometry(QtCore.QRect(0, 30, 671, 81))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.LabelRepostsUrl = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.LabelRepostsUrl.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        self.LabelRepostsUrl.setFont(font)
        self.LabelRepostsUrl.setStyleSheet("background-color: rgb(35, 46, 52);")
        self.LabelRepostsUrl.setObjectName("LabelRepostsUrl")
        self.horizontalLayout_21.addWidget(self.LabelRepostsUrl)
        self.SaveUrlButton_R = QtWidgets.QPushButton(self.layoutWidget_9)
        self.SaveUrlButton_R.setMaximumSize(QtCore.QSize(16777215, 40))
        self.SaveUrlButton_R.setObjectName("SaveUrlButton_R")
        self.horizontalLayout_21.addWidget(self.SaveUrlButton_R)
        self.RepostsCheckBox = QtWidgets.QCheckBox(self.repostPage)
        self.RepostsCheckBox.setGeometry(QtCore.QRect(0, 140, 161, 21))
        self.RepostsCheckBox.setObjectName("RepostsCheckBox")
        self.ResultSaveUrl_R = QtWidgets.QLabel(self.repostPage)
        self.ResultSaveUrl_R.setGeometry(QtCore.QRect(100, 110, 471, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ResultSaveUrl_R.setFont(font)
        self.ResultSaveUrl_R.setText("")
        self.ResultSaveUrl_R.setAlignment(QtCore.Qt.AlignCenter)
        self.ResultSaveUrl_R.setObjectName("ResultSaveUrl_R")
        self.StartLikes_R = QtWidgets.QToolButton(self.repostPage)
        self.StartLikes_R.setGeometry(QtCore.QRect(240, 170, 91, 41))
        self.StartLikes_R.setStyleSheet("color: rgb(154, 255, 152);")
        self.StartLikes_R.setObjectName("StartLikes_R")
        self.RepostsCount = QtWidgets.QLineEdit(self.repostPage)
        self.RepostsCount.setGeometry(QtCore.QRect(0, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        self.RepostsCount.setFont(font)
        self.RepostsCount.setToolTipDuration(-1)
        self.RepostsCount.setText("")
        self.RepostsCount.setCursorPosition(0)
        self.RepostsCount.setAlignment(QtCore.Qt.AlignCenter)
        self.RepostsCount.setObjectName("RepostsCount")
        self.StopLikes_R = QtWidgets.QToolButton(self.repostPage)
        self.StopLikes_R.setGeometry(QtCore.QRect(340, 170, 91, 41))
        self.StopLikes_R.setStyleSheet("color: rgb(255, 121, 123);")
        self.StopLikes_R.setObjectName("StopLikes_R")
        self.Reward = QtWidgets.QLineEdit(self.repostPage)
        self.Reward.setGeometry(QtCore.QRect(120, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        self.Reward.setFont(font)
        self.Reward.setToolTipDuration(-1)
        self.Reward.setText("")
        self.Reward.setCursorPosition(0)
        self.Reward.setAlignment(QtCore.Qt.AlignCenter)
        self.Reward.setObjectName("Reward")
        self.ResultStartLikes_R.raise_()
        self.layoutWidget_9.raise_()
        self.ResultSaveUrl_R.raise_()
        self.StartLikes_R.raise_()
        self.RepostsCount.raise_()
        self.StopLikes_R.raise_()
        self.RepostsCheckBox.raise_()
        self.Reward.raise_()
        self.stackedWidget.addWidget(self.repostPage)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(11, 9, 671, 42))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LikesButton = QtWidgets.QPushButton(self.layoutWidget4)
        self.LikesButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(13)
        self.LikesButton.setFont(font)
        self.LikesButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LikesButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.LikesButton.setObjectName("LikesButton")
        self.horizontalLayout_3.addWidget(self.LikesButton, 0, QtCore.Qt.AlignLeft)
        self.ReposButton = QtWidgets.QPushButton(self.layoutWidget4)
        self.ReposButton.setEnabled(True)
        self.ReposButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(13)
        font.setStrikeOut(True)
        self.ReposButton.setFont(font)
        self.ReposButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ReposButton.setObjectName("ReposButton")
        self.horizontalLayout_3.addWidget(self.ReposButton, 0, QtCore.Qt.AlignRight)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(9, 500, 671, 42))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.VkLoginButton = QtWidgets.QPushButton(self.layoutWidget5)
        self.VkLoginButton.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.VkLoginButton.setFont(font)
        self.VkLoginButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.VkLoginButton.setStyleSheet("")
        self.VkLoginButton.setObjectName("VkLoginButton")
        self.horizontalLayout_4.addWidget(self.VkLoginButton)
        self.LogsButton = QtWidgets.QPushButton(self.layoutWidget5)
        self.LogsButton.setEnabled(True)
        self.LogsButton.setMinimumSize(QtCore.QSize(0, 40))
        self.LogsButton.setMaximumSize(QtCore.QSize(100, 40))
        self.LogsButton.setSizeIncrement(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(13)
        self.LogsButton.setFont(font)
        self.LogsButton.setMouseTracking(False)
        self.LogsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LogsButton.setStyleSheet("")
        self.LogsButton.setCheckable(False)
        self.LogsButton.setChecked(False)
        self.LogsButton.setAutoRepeat(False)
        self.LogsButton.setAutoExclusive(False)
        self.LogsButton.setAutoDefault(False)
        self.LogsButton.setDefault(False)
        self.LogsButton.setFlat(False)
        self.LogsButton.setObjectName("LogsButton")
        self.horizontalLayout_4.addWidget(self.LogsButton, 0, QtCore.Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.action456 = QtWidgets.QAction(MainWindow)
        self.action456.setObjectName("action456")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_4.clicked.connect(self.lineEdit_2.copy)
        self.pushButton_4.clicked.connect(self.lineEdit.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VkPr"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Login"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_4.setText(_translate("MainWindow", "Log in"))
        self.ResultOfLogin.setText(_translate("MainWindow", "test"))
        self.LabelLikesUrl.setPlaceholderText(_translate("MainWindow", "Repost URL"))
        self.SaveUrlButton.setText(_translate("MainWindow", "Save"))
        self.LikesCount.setPlaceholderText(_translate("MainWindow", "Likes Count"))
        self.StartLikes.setText(_translate("MainWindow", "Start"))
        self.StopLikes.setText(_translate("MainWindow", "Stop"))
        self.LikesBalanceLabel.setText(_translate("MainWindow", "0"))
        self.getBalance.setText(_translate("MainWindow", "Get Balance"))
        self.LabelCoupon.setPlaceholderText(_translate("MainWindow", "Coupon"))
        self.SaveCouponButton.setText(_translate("MainWindow", "Activate"))
        self.ResultCoupon.setText(_translate("MainWindow", "Result"))
        self.LikestCheckBox.setText(_translate("MainWindow", "Auto add likest task"))
        self.LabelRepostsUrl.setPlaceholderText(_translate("MainWindow", "Repost URL"))
        self.SaveUrlButton_R.setText(_translate("MainWindow", "Save"))
        self.RepostsCheckBox.setText(_translate("MainWindow", "Auto add likest task"))
        self.StartLikes_R.setText(_translate("MainWindow", "Start"))
        self.RepostsCount.setPlaceholderText(_translate("MainWindow", "Reposts Count"))
        self.StopLikes_R.setText(_translate("MainWindow", "Stop"))
        self.Reward.setPlaceholderText(_translate("MainWindow", "Reward"))
        self.LikesButton.setText(_translate("MainWindow", "Likes"))
        self.ReposButton.setText(_translate("MainWindow", "Repost"))
        self.VkLoginButton.setText(_translate("MainWindow", "Vk data"))
        self.LogsButton.setText(_translate("MainWindow", "Logs"))
        self.LogsButton.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action456.setText(_translate("MainWindow", "456"))
