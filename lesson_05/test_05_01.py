
import time
from lesson_03.com import driver
from lesson_05.search_page import  search


driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx')
driver.maximize_window()
search("notice01","#notice08","dateObj")
