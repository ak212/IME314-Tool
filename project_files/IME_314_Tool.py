import sys

from PyQt4.QtGui import (QWidget, QLabel, QLineEdit, QSizePolicy, QPushButton,
                          QApplication)

import calculations
from simpleeval import simple_eval


__author__ = "Aaron Koeppel"
__version__ = 1.0

def is_number(number):
   try:
      float(number)
      return True
   except ValueError:
      return False

class Window(QWidget):
   def __init__(self):
      QWidget.__init__(self)
      
      self.factorValue = 1
      
      #Window Sizing
      self.setFixedSize(600, 400)
      self.setWindowTitle("IME 314 Tool")
      
      '''Start Top Panel'''
      #Interest label
      self.interest = QLabel('i: ', self)
      self.interest.move(200, 10)
      
      #Period label
      self.period = QLabel('n: ', self)
      self.period.move(350, 10)

      #Interest text box
      self.interestEdit = QLineEdit(self)
      self.interestEdit.setFixedWidth(40)
      self.interestEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.interestEdit.move(220, 10)
      
      #Period text box
      self.periodEdit = QLineEdit(self)
      self.periodEdit.setFixedWidth(30)
      self.periodEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.periodEdit.move(370, 10)
      
      #Multiplier Label
      self.multiplier = QLabel('Multiplier Value: ', self)
      self.multiplier.move(80, 50)
      
      #Multiplier text box
      self.multiplierEdit = QLineEdit(self)
      self.multiplierEdit.setFixedWidth(100)
      self.multiplierEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.multiplierEdit.move(160, 50)
      
      #Final Value Label
      self.finalValue = QLabel('Final Value: ', self)
      self.finalValue.move(370, 50)
      
      #Final Value text box
      self.finalValueEdit = QLineEdit(self)
      self.finalValueEdit.setFixedWidth(100)
      self.finalValueEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.finalValueEdit.move(440, 50)
      '''End Top Panel'''
      
      '''Start Column 1'''
      #F/P button
      self.FoPButton = QPushButton('F/P (P->F)', self)
      self.FoPButton.setFixedSize(70, 30)
      self.FoPButton.move(70, 110)
      self.FoPButton.clicked.connect(self.show_FoP)
      
      #F/P text box
      self.FoPButtonEdit = QLineEdit(self)
      self.FoPButtonEdit.setFixedWidth(100)
      self.FoPButtonEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.FoPButtonEdit.move(160, 115)
      
      #A/P button
      self.AoPButton = QPushButton('A/P (P->A)', self)
      self.AoPButton.setFixedSize(70, 30)
      self.AoPButton.move(70, 170)
      self.AoPButton.clicked.connect(self.show_AoP)
      
      #A/P text box
      self.AoPButtonEdit = QLineEdit(self)
      self.AoPButtonEdit.setFixedWidth(100)
      self.AoPButtonEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.AoPButtonEdit.move(160, 175)
      
      #F/A button
      self.FoAButton = QPushButton('F/A (A->F)', self)
      self.FoAButton.setFixedSize(70, 30)
      self.FoAButton.move(70, 230)
      self.FoAButton.clicked.connect(self.show_FoA)

      #F/A text box
      self.FoAButtonEdit = QLineEdit(self)
      self.FoAButtonEdit.setFixedWidth(100)
      self.FoAButtonEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.FoAButtonEdit.move(160, 235)
      
      #A/G button
      self.AoGButton = QPushButton('A/G (G->A)', self)
      self.AoGButton.setFixedSize(70, 30)
      self.AoGButton.move(70, 290)
      self.AoGButton.clicked.connect(self.show_AoG)
      
      #A/G text box
      self.AoGButtonEdit = QLineEdit(self)
      self.AoGButtonEdit.setFixedWidth(100)
      self.AoGButtonEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.AoGButtonEdit.move(160, 295)
      '''End Column 1'''
      
      '''Start Column 2'''
      #P/F button
      self.PoFButton = QPushButton('P/F (F->P)', self)
      self.PoFButton.setFixedSize(70, 30)
      self.PoFButton.move(350, 110)
      self.PoFButton.clicked.connect(self.show_PoF)
      
      #P/F text box
      self.PoFButtonEdit = QLineEdit(self)
      self.PoFButtonEdit.setFixedWidth(100)
      self.PoFButtonEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.PoFButtonEdit.move(440, 115)
      
      #P/A button
      self.PoAButton = QPushButton('P/A (A->P)', self)
      self.PoAButton.setFixedSize(70, 30)
      self.PoAButton.move(350, 170)
      self.PoAButton.clicked.connect(self.show_PoA)
      
      #P/A text box
      self.PoAButtonEdit = QLineEdit(self)
      self.PoAButtonEdit.setFixedWidth(100)
      self.PoAButtonEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.PoAButtonEdit.move(440, 175)
      
      #A/F button
      self.AoFButton = QPushButton('A/F (F->A)', self)
      self.AoFButton.setFixedSize(70, 30)
      self.AoFButton.move(350, 230)
      self.AoFButton.clicked.connect(self.show_AoF)
      
      #A/F text box
      self.AoFButtonEdit = QLineEdit(self)
      self.AoFButtonEdit.setFixedWidth(100)
      self.AoFButtonEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.AoFButtonEdit.move(440, 235)
      
      #A/G button
      self.PoGButton = QPushButton('P/G (G->P)', self)
      self.PoGButton.setFixedSize(70, 30)
      self.PoGButton.move(350, 290)
      self.PoGButton.clicked.connect(self.show_PoG)
      
      #A/G text box
      self.PoGButtonEdit = QLineEdit(self)
      self.PoGButtonEdit.setFixedWidth(100)
      self.PoGButtonEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.PoGButtonEdit.move(440, 295)
      '''End Column 2'''
      
      #Running Sum Label
      self.sumValue = QLabel('Sum: ', self)
      self.sumValue.move(130, 360)
      
      #Final Value text box
      self.sumEdit = QLineEdit(self)
      self.sumEdit.setFixedWidth(100)
      self.sumEdit.setSizePolicy(QSizePolicy.Fixed,
                                 QSizePolicy.Fixed)
      self.sumEdit.move(160, 355)
      
      #Clear button
      self.clearButton = QPushButton('Clear', self)
      self.clearButton.setFixedSize(50, 30)
      self.clearButton.move(350, 350)
      self.clearButton.clicked.connect(self.clear_sum)
      
      #Clear all button
      self.clearAllButton = QPushButton('Clear All', self)
      self.clearAllButton.setFixedSize(50, 30)
      self.clearAllButton.move(430, 350)
      self.clearAllButton.clicked.connect(self.clear_values)
      #List of all editable fields
      self.fields = [self.sumEdit, self.finalValueEdit, self.interestEdit,
                     self.periodEdit, self.multiplierEdit, self.sumEdit,
                     self.FoPButtonEdit, self.AoPButtonEdit, self.FoAButtonEdit,
                     self.AoGButtonEdit, self.PoFButtonEdit, self.PoAButtonEdit,
                     self.AoFButtonEdit, self.PoGButtonEdit]
      
      self.show()
   
   def update_value(self, button, calc):
      self.factor = calculations.Factors(float(self.interestEdit.text()),
                                    int(self.periodEdit.text()))
      calc = calc(self.factor)
      button.setText(str(calc))
      value = float(simple_eval(str(self.multiplierEdit.text()))) * calc
      self.finalValueEdit.setText(str(value))
      
      if is_number(str(self.sumEdit.text())):
         self.sum = float(self.sumEdit.text()) + value
      else:
         self.sum = value
      self.sumEdit.setText(str(self.sum))
      
   def show_FoP(self):
      self.update_value(self.FoPButtonEdit, calculations.FoP)
   
   def show_PoF(self):
      self.update_value(self.PoFButtonEdit, calculations.PoF)
   
   def show_AoP(self):
      self.update_value(self.AoPButtonEdit, calculations.AoP)
      
   def show_PoA(self):
      self.update_value(self.PoAButtonEdit, calculations.PoA)
   
   def show_FoA(self):
      self.update_value(self.FoAButtonEdit, calculations.FoA)
      
   def show_AoF(self):
      self.update_value(self.AoFButtonEdit, calculations.AoF)
   
   def show_AoG(self):
      self.update_value(self.AoGButtonEdit, calculations.AoG)
   
   def show_PoG(self):
      self.update_value(self.PoGButtonEdit, calculations.PoG)
   
   def clear_sum(self):
      self.sumEdit.setText("")
      
   def clear_values(self):
      for self.field in self.fields:
         self.field.setText("")
      
   
def main():
    
   app = QApplication(sys.argv)
   win = Window()
   sys.exit(app.exec_())


if __name__ == '__main__':
   main()
