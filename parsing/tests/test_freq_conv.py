import parsedates as p
import Parser_ts  as dt_parse
import datetime as d

from numpy.testing import *

p.set_callback(dt_parse.DateTimeFromString)

# These tests are for checking frequency conversions
# meant for the asfreq() function

class TestFreqConv():

	def test_from_year(self):
		# Create  bunch of year dates

		# Convert them to other frequencies
		# Check 

	def test_from_month(self):
	def test_from_week(self):
	def test_from_business(self):
	def test_from_day(self):
	def test_from_hour(self):
	def test_from_minute(self):
	def test_from_second(self):
	def test_from_millisecond(self):
	def test_from_microsecond(self):
	def test_from_nanosecond(self):
	def test_from_picosecond(self):
	def test_from_femtosecond(self):
	def test_from_attosecond(self):
