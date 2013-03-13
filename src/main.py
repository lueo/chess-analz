# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from about import DialogAbout
from ui.ui_mainWindow import Ui_MainWindow

# import our module
import uci

# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        # Let's do something interesting: load the database contents 
        # into our task list widget
        text = self.ui.textBrowserStdout
        try:
            engine = uci.Engine()
            # init & check options
            try:
                engine.put('uci')
                re = engine.get()
                assert 'uciok' in re
            except:
                print 'UCI not ready!'
            # settings
            text.append(re)
            engine.put('setoption name Hash value 256')
            engine.put('setoption name Threads value 4')
            engine.put('position fen r1b1k1nr/p5pp/5p2/1Bn1p3/5B2/P7/1PP2PPP/2KR2NR b - - 1 14')
            engine.put('go infinite')
            re = engine.get()
            

        except:
            print "Error!"
        
        
        text.append('this<br />')
        text.append('this\n')
        text.append('this\n')
        text.append('this\n')

    def openAboutDialog(self):
        dialog = DialogAbout(self)
        dialog.exec_()

def main():
    # Init the database before doing anything else
    
    # Again, this is boilerplate, it's going to be the same on 
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
    
