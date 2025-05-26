#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Copyright 2015 Recursos Python - www.recursospython.com
#
#
from random import choice
from string import (ascii_letters, ascii_lowercase, ascii_uppercase,
                    digits, punctuation)
from PyQt5.QtCore import pyqtSlot, Qt, QEvent
from PyQt5.QtGui import QApplication, QMainWindow, QRegExpValidator
from gui import Ui_MainWindow
class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        
        self.on_both_radio_toggled(True)
        self.on_specific_radio_toggled(False)
        self.window.specials_text.setText(punctuation)
        
        self.window.letters_text.installEventFilter(self)
        self.window.specific_text.installEventFilter(self)
        self.window.specials_text.installEventFilter(self)
    
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.text():
            charset = {
                self.window.letters_text: self.charset,
                self.window.specific_text: digits,
                self.window.specials_text: punctuation
            }[obj] + "\b"
            if event.text() in obj.text() or event.text() not in charset:
                return True
        
        return QMainWindow.eventFilter(self, obj, event)
    
    def on_letters_check_stateChanged(self, checked):
        self.window.letters_group.setVisible(checked)
    
    def on_numbers_check_stateChanged(self, checked):
        self.window.numbers_group.setVisible(checked)
    
    def on_specials_check_stateChanged(self, checked):
        self.window.specials_group.setVisible(checked)
    
    def on_lower_radio_toggled(self, checked):
        self.charset = ascii_lowercase
        self.window.letters_text.setText(ascii_lowercase)
    
    def on_upper_radio_toggled(self, checked):
        self.charset = ascii_uppercase
        self.window.letters_text.setText(ascii_uppercase)
    
    def on_both_radio_toggled(self, checked):
        self.charset = ascii_letters
        self.window.letters_text.setText(ascii_letters)
    
    def on_range_radio_toggled(self, checked):
        self.window.range_from_spin.setEnabled(checked)
        self.window.range_to_spin.setEnabled(checked)
    
    def on_specific_radio_toggled(self, checked):
        self.window.specific_text.setEnabled(checked)
    
    @pyqtSlot(int)
    def on_range_from_spin_valueChanged(self, value):
        if value >= self.window.range_to_spin.value():
            self.window.range_from_spin.setValue(value - 1)
    
    @pyqtSlot(int)
    def on_range_to_spin_valueChanged(self, value):
        if value <= self.window.range_from_spin.value():
            self.window.range_to_spin.setValue(value + 1)
    
    def on_generate_button_released(self):
        password = ""
        charset = ""
        
        if self.window.letters_check.isChecked():
            letters = self.window.letters_text.text()
            if letters:
                charset += letters
        if self.window.numbers_check.isChecked():
            if self.window.range_radio.isChecked():
                charset += "".join(
                    str(i) for i in range(
                        self.window.range_from_spin.value(),
                        self.window.range_to_spin.value() + 1
                    )
                )
            else:
                numbers = self.window.specific_text.text()
                if numbers:
                    charset += numbers
        if self.window.specials_check.isChecked():
            specials = self.window.specials_text.text()
            if specials:
                charset += specials
        if self.window.spaces_check.isChecked():
            charset += " "
        
        if charset:
            for i in range(self.window.length_spin.value()):
                password += choice(charset)
            
            self.window.password_text.setText(password)
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()