import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from  constants import *

'''
This is to build all of the gui components for the program.  This means the application and
its main window along with the plots and buttons.

The purpose of this file is to reduce the clutter of the main file.
'''


#####################################################
####           BUILD GUI                         ####
#####################################################

print 'Building GUI'
#Main window
app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.setWindowTitle('Greenland')
mw.setMinimumHeight(1000)
mw.setMinimumWidth(1200)
cw = QtGui.QWidget()            # GENERIC WIDGET AS CENTRAL WIDGET (inside main window)
mw.setCentralWidget(cw)
mainLayout = QtGui.QHBoxLayout()
cw.setLayout(mainLayout)
iiContainer = QtGui.QStackedWidget()    # STACKED WIDGET (inside the layout)

#####################################################
####      SIDE WIDGET WITH BUTTONS               ####
#####################################################

buttonBoxWidget = QtGui.QWidget()
buttonBox = QtGui.QVBoxLayout()
buttonBoxWidget.setLayout(buttonBox)

mapList = QtGui.QComboBox()
maps = ['Velocity', 'Bed', 'Surface', 'Smb', 'Thickness']#, 'OldThickness']
mapList.addItems(maps)

autoCorrectVpt   = QtGui.QCheckBox('Auto-correct vpt pos.')
autoCorrectVpt.setTristate(False)
autoCorrectVpt.setCheckState(2)
instructionButton = QtGui.QPushButton('Instructions')
clearButton      = QtGui.QPushButton('Clear Points')
calcWidthButton  = QtGui.QPushButton('Calculate Velocity Width')
calcWidthButton.setEnabled(True)
intButton        = QtGui.QPushButton('Integrate')
intButton.setEnabled(False)
cProfButton      = QtGui.QPushButton('Plot Path') #FIXME should automatically get profile
cProfButton.setEnabled(False)
cRegionButton    = QtGui.QPushButton('Region')
cRegionButton.setEnabled(False)
cVelArrowsButton = QtGui.QPushButton('Arrows')
cVelArrowsButton.setEnabled(False)
modelButton      = QtGui.QPushButton('Run Model')
modelButton.setEnabled(False)
hiResButton      = QtGui.QPushButton('High-res interpolators (may take 2 minutes')
hiResButton.setEnabled(False)
meshButton       = QtGui.QPushButton('generate Mesh')
meshButton.setEnabled(False)
meshCheckBox    = QtGui.QCheckBox('Mesh')
autoCorrectVpt.setTristate(False)
autoCorrectVpt.setCheckState(0)
mouseCoordinates = QtGui.QLabel('x:\ty:')
textOut = QtGui.QTextBrowser()

maxWidth = 300

mapList.setMaximumWidth(maxWidth)
autoCorrectVpt.setMaximumWidth(maxWidth)
instructionButton.setMaximumWidth(maxWidth)
clearButton.setMaximumWidth(maxWidth)
clearButton.setMaximumWidth(maxWidth)
calcWidthButton.setMaximumWidth(maxWidth)
intButton.setMaximumWidth(maxWidth)
cProfButton.setMaximumWidth(maxWidth)
cRegionButton.setMaximumWidth(maxWidth)
cVelArrowsButton.setMaximumWidth(maxWidth)
modelButton.setMaximumWidth(maxWidth)
hiResButton.setMaximumWidth(maxWidth)
meshButton.setMaximumWidth(maxWidth)
textOut.setMaximumWidth(maxWidth)


buttonBox.addWidget(mapList)
buttonBox.addWidget(autoCorrectVpt)
buttonBox.addWidget(instructionButton)
buttonBox.addWidget(clearButton)
buttonBox.addWidget(calcWidthButton)
buttonBox.addWidget(intButton)
buttonBox.addWidget(cProfButton)
# buttonBox.addWidget(cRegionButton)
# buttonBox.addWidget(cVelArrowsButton)
buttonBox.addWidget(modelButton)
buttonBox.addWidget(hiResButton)
buttonBox.addWidget(meshButton)
buttonBox.addWidget(meshCheckBox)
buttonBox.addWidget(mouseCoordinates)


# LABELS AND LINE EDITS
time_widget    = QtGui.QWidget()

time_container = QtGui.QGridLayout()
time_widget.setLayout(time_container)

model_res_label    = QtGui.QLabel('Sptl res(m):')
model_res_lineEdit = QtGui.QLineEdit('2000')

t_end_label    = QtGui.QLabel('t_end(yr):')
t_end_lineEdit = QtGui.QLineEdit('20000')

t_step_label    = QtGui.QLabel('t_step(yr):')
t_step_lineEdit = QtGui.QLineEdit('10')
t_current = QtGui.QLabel('Current year: ')

time_container.addWidget(model_res_label,    0, 0)
time_container.addWidget(model_res_lineEdit, 0, 1)
time_container.addWidget(t_end_label,        1, 0)
time_container.addWidget(t_end_lineEdit,     1, 1)
time_container.addWidget(t_step_label,       2, 0)
time_container.addWidget(t_step_lineEdit,    2, 1)
time_container.addWidget(t_current,          3, 0, 1, 2)

buttonBox.addWidget(time_widget)
buttonBox.addWidget(textOut)


#####################################################
####         CREATE BOTTOM PLOT                  ####
#####################################################
# bp = pg.PlotWidget()
# bpLegend = bp.getPlotItem().addLegend()

# iiContainer.setMinimumHeight(mw.height()*(2/3))

lsw = QtGui.QWidget()
leftSide = QtGui.QVBoxLayout()
lsw.setLayout(leftSide)
leftSide.addWidget(iiContainer)
# leftSide.addWidget(bp,1)
dataCheckContainer = QtGui.QWidget()
dCClayout = QtGui.QHBoxLayout()


dataCheckContainer.setLayout(dCClayout)

allCheck        = QtGui.QCheckBox('Plot All')
velocityCheck   = QtGui.QCheckBox('Velocity')
vWidthCheck     = QtGui.QCheckBox('Velocity Width')
smbCheck        = QtGui.QCheckBox('SMB')
surfaceCheck    = QtGui.QCheckBox('Surface')
bedCheck        = QtGui.QCheckBox('Bed')
thicknessCheck  = QtGui.QCheckBox('Thickness')


# velocityCheck.setMaximumWidth(80)
# vWidthCheck.setMaximumWidth(80)
# smbCheck.setMaximumWidth(80)
# surfaceCheck.setMaximumWidth(80)
# bedCheck.setMaximumWidth(80)


checkBoxW = QtGui.QWidget()
checkBLayout = QtGui.QVBoxLayout()
checkBoxW.setLayout(checkBLayout)

allCheck.setTristate(False)
velocityCheck.setTristate(False)
vWidthCheck.setTristate(False)
smbCheck.setTristate(False)
surfaceCheck.setTristate(False)
bedCheck.setTristate(False)
thicknessCheck.setTristate(False)

allCheck.setCheckState(2)
velocityCheck.setCheckState(2)
vWidthCheck.setCheckState(2)
smbCheck.setCheckState(2)
surfaceCheck.setCheckState(2)
bedCheck.setCheckState(2)
thicknessCheck.setCheckState(2)

checkBLayout.addWidget(QtGui.QLabel('Plot Checked Data:'))
checkBLayout.addWidget(allCheck)
checkBLayout.addWidget(velocityCheck)
checkBLayout.addWidget(vWidthCheck)
checkBLayout.addWidget(smbCheck)
checkBLayout.addWidget(surfaceCheck)
checkBLayout.addWidget(bedCheck)
checkBLayout.addWidget(thicknessCheck)
checkBLayout.setSpacing(0)

buttonBox.addWidget(checkBoxW)
dataCheckContainer.setMaximumWidth(500)

mainLayout.addWidget(lsw)
mainLayout.addWidget(buttonBoxWidget)
buttonBoxWidget.setMaximumWidth(maxWidth + 12)

mw.show()


#####################################################
####         MISCELLANEOUS                       ####
#####################################################
currentMap = 0  # selects which data map to show [velocity, bed, surface]
vptSel = False
shift = False

print 'Done building gui'