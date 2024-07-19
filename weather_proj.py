# App to Get Temperature Data from "Open Weather Map" Service
import pyowm
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import sys

# Defining global variable to store OWM weather-query object
owm = pyowm.OWM('256ca78575297961a760d1780960af91')
wman = owm.weather_manager()

#Function that gets weather info from API
#  Returns results in dictionary with
#  keys 'temp', 'temp_max', 'temp_min'
#  and values that are floats

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        self.ui = loadUi('mainpage.ui', self)
        self.pushButton_2.clicked.connect(self.getWeather)

    def getWeather(self):
        # user needs to input a location in this format: city,country
        location = self.plainTextEdit.toPlainText()
        observation = wman.weather_at_place(location).weather
        weather_info = observation.temperature('fahrenheit')
        current_weather = str(weather_info['temp']) 
        max_temp = str(weather_info['temp_max'])
        min_temp = str(weather_info['temp_min'])

        temps = 'Current temperature: ' + current_weather + ' F' + '\nMaximum temperature: ' + max_temp + ' F' + '\nMinimum temperature: ' + min_temp + ' F'
    


        self.textEdit.setText(temps)

app = QApplication(sys.argv)
widget = MainPage()
widget.show()

sys.exit(app.exec_())


