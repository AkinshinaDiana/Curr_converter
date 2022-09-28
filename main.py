import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QLineEdit
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow


class myCurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(myCurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()


    def init_UI(self):
        self.setWindowIcon(QIcon('img/icon70x70.jpg'))
        self.setWindowTitle('Конвертация валюты')
        self.ui.pushButton.clicked.connect(self.clear_lines)
        self.ui.pushButton_2.clicked.connect(self.my_converter)

    def clear_lines(self):
        self.ui.input_amount_usd.setText('')
        self.ui.input_amount_euro.setText('')
        self.ui.input_amount_pln.setText('')
        self.ui.input_amount_byn.setText('')
        self.ui.input_amount_cny.setText('')
        self.ui.input_amount_rur.setText('')

    def my_converter(self):
        from forex_python.converter import CurrencyRates
        c = CurrencyRates()

        # input_amount_usd = float(self.ui.input_amount_usd.text())
        # output_amount_usd = round(c.convert('USD', 'USD', input_amount_usd), 2)
        # self.ui.input_amount_usd.setText(str(output_amount_usd))
        # output_amount_euro = round(c.convert('USD', 'EUR', input_amount_usd), 2)
        # self.ui.input_amount_euro.setText(str(output_amount_euro))
        # output_amount_pln = round(c.convert('USD', 'PLN', input_amount_usd), 2)
        # self.ui.input_amount_pln.setText(str(output_amount_pln))
        # output_amount_byn = round(c.convert('USD', 'JPY', input_amount_usd), 2) # нет данных по BYN
        # self.ui.input_amount_byn.setText(str(output_amount_byn))
        # output_amount_cny = round(c.convert('USD', 'CNY', input_amount_usd), 2)
        # self.ui.input_amount_cny.setText(str(output_amount_cny))
        # output_amount_rur = round(c.convert('USD', 'AUD', input_amount_usd), 2) #нет данных по рос.руб.
        # self.ui.input_amount_rur.setText(str(output_amount_rur))

        input_amount_euro = float(self.ui.input_amount_euro.text())
        output_amount_euro = round(c.convert('EUR', 'EUR', input_amount_euro), 2)
        self.ui.input_amount_euro.setText(str(output_amount_euro))
        output_amount_usd = round(c.convert('EUR', 'USD', input_amount_euro), 2)
        self.ui.input_amount_usd.setText(str(output_amount_usd))
        output_amount_pln = round(c.convert('EUR', 'PLN', input_amount_euro), 2)
        self.ui.input_amount_pln.setText(str(output_amount_euro))
        output_amount_byn = round(c.convert('EUR', 'JPY', input_amount_euro), 2)  # нет данных по BYN
        self.ui.input_amount_byn.setText(str(output_amount_byn))
        output_amount_cny = round(c.convert('EUR', 'CNY', input_amount_euro), 2)
        self.ui.input_amount_cny.setText(str(output_amount_cny))
        output_amount_rur = round(c.convert('EUR', 'AUD', input_amount_euro), 2)  # нет данных по рос.руб.
        self.ui.input_amount_rur.setText(str(output_amount_rur))
        # # input_amount_pln = float(self.ui.input_amount_pln.text())
        # # input_amount_byn = float(self.ui.input_amount_byn.text())
        # # input_amount_cny = float(self.ui.input_amount_byn.text())
        # # input_amount_rur = float(self.ui.input_amount_rur.text())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = myCurrencyConv()
    application.show()
    sys.exit(app.exec())