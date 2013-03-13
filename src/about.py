# -*- encoding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from ui.ui_about import Ui_DialogAbout

class DialogAbout(QtGui.QDialog, Ui_DialogAbout):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
