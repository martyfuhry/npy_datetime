import parsedates as p
import Parser_ts  as dt_parse
import datetime

from numpy.testing import *

p.set_callback(dt_parse.DateTimeFromString)

freqs = ["Y", "M", "W", "B", "D", 
		 "h", "m", "s", "ms", "us", 
		 "ns", "ps", "fs", "as"]

# All test numbers were pulled from the SciKits TimeSeries Module (example):
#    >>> print t.Date("Minute", "1970-01-10").value
#    12961

class TestCreation():
# Test each frequencies' creation and proper value

	# YEAR
	def test_pre_epoch_year(self):
		"Test creation of years pre epoch."

		dstring = '1969'
		assert_equal(p.date_to_long(dstring, 'Y'), -1)

		dstring = '1940'
		assert_equal(p.date_to_long(dstring, 'Y'), -30)

		dstring = '1000'
		assert_equal(p.date_to_long(dstring, 'Y'), -970)

		dstring = '0001'
		assert_equal(p.date_to_long(dstring, 'Y'), -1969)

	def test_post_epoch_year(self):
		"Test creation of years post epoch."
		
		dstring = '1970'
		assert_equal(p.date_to_long(dstring, 'Y'), 0)

		dstring = '1980'
		assert_equal(p.date_to_long(dstring, 'Y'), 10)

		dstring = '2010'
		assert_equal(p.date_to_long(dstring, 'Y'), 40)

	# MONTH
	def test_pre_epoch_month(self):
		"Test creation of months pre epoch."

		dstring = '1969-12'
		assert_equal(p.date_to_long(dstring, 'M'), -1)

		dstring = '1969-01'
		assert_equal(p.date_to_long(dstring, 'M'), -12)

		dstring = '1950-01'
		assert_equal(p.date_to_long(dstring, 'M'), -240)

		dstring = '1900-06'
		assert_equal(p.date_to_long(dstring, 'M'), -835)

		dstring = '1492-02'
		assert_equal(p.date_to_long(dstring, 'M'), -5735)

		dstring = '1000-01'
		assert_equal(p.date_to_long(dstring, 'M'), -11640)

		dstring = '0800-10'
		assert_equal(p.date_to_long(dstring, 'M'), -14031)

		dstring = '0001-01'
		assert_equal(p.date_to_long(dstring, 'M'), -23628)

	def test_post_epoch_month(self):
		"Test creation of months post epoch."
	
		dstring = '1970-01'
		assert_equal(p.date_to_long(dstring, 'M'), 0)

		dstring = '1970-12'
		assert_equal(p.date_to_long(dstring, 'M'), 11)

		dstring = '1980-01'
		assert_equal(p.date_to_long(dstring, 'M'), 120)

		dstring = '1996-02'
		assert_equal(p.date_to_long(dstring, 'M'), 313)

	# WEEK
	def test_pre_epoch_week(self):
		"Test creation of weeks pre epoch."
		
		dstring = '1969-12-31'
		assert_equal(p.date_to_long(dstring, 'W'), 0)

		dstring = '1969-12-28'
		assert_equal(p.date_to_long(dstring, 'W'), 0)

		dstring = '1969-12-27'
		assert_equal(p.date_to_long(dstring, 'W'), -1)

		dstring = '1969-01-06'
		assert_equal(p.date_to_long(dstring, 'W'), -51)

		dstring = '1969-01-01'
		assert_equal(p.date_to_long(dstring, 'W'), -52)

		dstring = '1900-08-05'
		assert_equal(p.date_to_long(dstring, 'W'), -3621)

		dstring = '1900-08-04'
		assert_equal(p.date_to_long(dstring, 'W'), -3622)

		dstring = '1851-05-17'
		assert_equal(p.date_to_long(dstring, 'W'), -6190)

		dstring = '1851-05-18'
		assert_equal(p.date_to_long(dstring, 'W'), -6189)

		dstring = '1000-01-06'
		assert_equal(p.date_to_long(dstring, 'W'), -50611)

		dstring = '1000-01-07'
		assert_equal(p.date_to_long(dstring, 'W'), -50610)

		dstring = '0912-04-18'
		assert_equal(p.date_to_long(dstring, 'W'), -55188)

		dstring = '0912-04-19'
		assert_equal(p.date_to_long(dstring, 'W'), -55187)

		dstring = '0912-04-20'
		assert_equal(p.date_to_long(dstring, 'W'), -55187)

		dstring = '0912-04-21'
		assert_equal(p.date_to_long(dstring, 'W'), -55187)

		dstring = '0912-04-22'
		assert_equal(p.date_to_long(dstring, 'W'), -55187)

		dstring = '0912-04-23'
		assert_equal(p.date_to_long(dstring, 'W'), -55187)

		dstring = '0912-04-24'
		assert_equal(p.date_to_long(dstring, 'W'), -55187)

		dstring = '0912-04-25'
		assert_equal(p.date_to_long(dstring, 'W'), -55187)

		dstring = '0010-01-04'
		assert_equal(p.date_to_long(dstring, 'W'), -102267)

		dstring = '0010-01-03'
		assert_equal(p.date_to_long(dstring, 'W'), -102268)



	def test_post_epoch_week(self):
		"Test creation of weeks post epoch."

		dstring = '1970-01-01'
		assert_equal(p.date_to_long(dstring, 'W'), 0)
		
		dstring = '1970-01-04'
		assert_equal(p.date_to_long(dstring, 'W'), 1)
		
		dstring = '1970-01-10'
		assert_equal(p.date_to_long(dstring, 'W'), 1)
		
		dstring = '1970-01-11'
		assert_equal(p.date_to_long(dstring, 'W'), 2)
		
		dstring = '1970-03-01'
		assert_equal(p.date_to_long(dstring, 'W'), 9)

		dstring = '1970-03-07'
		assert_equal(p.date_to_long(dstring, 'W'), 9)

		dstring = '1970-03-08'
		assert_equal(p.date_to_long(dstring, 'W'), 10)

		dstring = '1980-01-04' 
		assert_equal(p.date_to_long(dstring, "W"), 522)

		dstring = '1980-01-06' 
		assert_equal(p.date_to_long(dstring, "W"), 523)

		dstring = '1980-01-07' 
		assert_equal(p.date_to_long(dstring, "W"), 523)

		dstring = '2000-09-02' 
		assert_equal(p.date_to_long(dstring, "W"), 1600)

		dstring = '2000-09-04'
		assert_equal(p.date_to_long(dstring, "W"), 1601)

		dstring = '2191-12-24' 
		assert_equal(p.date_to_long(dstring, "W"), 11582)

		dstring = '2191-12-25' 
		assert_equal(p.date_to_long(dstring, "W"), 11583)

		dstring = '2191-12-26' 
		assert_equal(p.date_to_long(dstring, "W"), 11583)

	# BUSINESS DAY
	def test_pre_epoch_business(self):
		"Test creation of business days pre epoch."

	def test_post_epoch_business_day(self):
		"Test creation of business days post epoch."
		
		dstring = '1970-01-01'
		assert_equal(p.date_to_long(dstring, "B"), 0)
	
		dstring = '1970-01-02'
		assert_equal(p.date_to_long(dstring, "B"), 1)
	
		dstring = '1970-01-03'
		assert_equal(p.date_to_long(dstring, "B"), 1)
	
		dstring = '1970-01-09'
		assert_equal(p.date_to_long(dstring, "B"), 6)
	
		dstring = '1970-01-11'
		assert_equal(p.date_to_long(dstring, "B"), 6)
	
		dstring = '1975-12-31'
		assert_equal(p.date_to_long(dstring, "B"), 1564)
	
		dstring = '1980-01-01'
		assert_equal(p.date_to_long(dstring, "B"), 2608)
	
		dstring = '2010-10-30'
		assert_equal(p.date_to_long(dstring, "B"), 10651)
	
		dstring = '2010-10-31'
		assert_equal(p.date_to_long(dstring, "B"), 10651)
	
		dstring = '2010-11-01'
		assert_equal(p.date_to_long(dstring, "B"), 10652)
	
	# DAY
	def test_pre_epoch_day(self):
		"Test creation of days pre epoch."

	def test_post_epoch_day(self):
		"Test creation of days post epoch."

		dstring = '1970-01-01'
		assert_equal(p.date_to_long(dstring, 'D'), 0)

		dstring = '1970-01-02'
		assert_equal(p.date_to_long(dstring, 'D'), 1)

		dstring = '1970-12-01'
		assert_equal(p.date_to_long(dstring, 'D'), 334)

		dstring = '1980-01-01'
		assert_equal(p.date_to_long(dstring, 'D'), 3652)

		dstring = '1990-06-10'
		assert_equal(p.date_to_long(dstring, 'D'), 7465)

		dstring = '2000-01-01'
		assert_equal(p.date_to_long(dstring, 'D'), 10957)

		dstring = '2004-12-31'
		assert_equal(p.date_to_long(dstring, 'D'), 12783)

	# HOUR
	def test_pre_epoch_hour(self):
		"Test creation of hours pre epoch."
	def test_post_epoch_hour(self):
		"Test creation of hours post epoch."

		dstring = '1970-01-01 00:00:00'
		assert_equal(p.date_to_long(dstring, 'h'), 0)
		
		dstring = '1970-01-01 01:00:00'
		assert_equal(p.date_to_long(dstring, 'h'), 1)
		
		dstring = '1970-02-01 12:00:00'
		assert_equal(p.date_to_long(dstring, 'h'), 756)

		dstring = '1970-10-25 00:00:00'
		assert_equal(p.date_to_long(dstring, 'h'), 7128)

		dstring = '1975-12-31 23:00:00'
		assert_equal(p.date_to_long(dstring, 'h'), 52583)

		dstring = '2001-01-01 01:00:00'
		assert_equal(p.date_to_long(dstring, 'h'), 271753)

		dstring = '2010-05-01 12:00:00'
		assert_equal(p.date_to_long(dstring, 'h'), 353532)

	# MINUTE
	def test_pre_epoch_minute(self):
		"Test creation of minutes pre epoch."
	def test_post_epoch_minute(self):
		"Test creation of minutes post epoch."

		dstring = '1970-01-01 00:00:00'
		assert_equal(p.date_to_long(dstring, 'm'), 0)

		dstring = '1970-01-01 00:01:00'
		assert_equal(p.date_to_long(dstring, 'm'), 1)

		dstring = '1970-01-01 12:00:00'
		assert_equal(p.date_to_long(dstring, 'm'), 720)

		dstring = '1970-05-01 00:00:00'
		assert_equal(p.date_to_long(dstring, 'm'), 172800)
		
		dstring = '1971-01-01 00:01:00'
		assert_equal(p.date_to_long(dstring, 'm'), 525601)

		dstring = '1975-01-01 23:59:00'
		assert_equal(p.date_to_long(dstring, 'm'), 2630879)

		dstring = '2000-11-12 01:30'
		assert_equal(p.date_to_long(dstring, 'm'), 16233210)

	# SECOND
	def test_pre_epoch_second(self):
		"Test creation of seconds pre epoch."
	def test_post_epoch_second(self):
		"Test creation of seconds post epoch."

		dstring = '1970-01-01 00:00:00'
		assert_equal(p.date_to_long(dstring, 's'), 0)

		dstring = '1970-01-01 00:00:01'
		assert_equal(p.date_to_long(dstring, 's'), 1)

		dstring = '1970-02-01 00:00:00'
		assert_equal(p.date_to_long(dstring, 's'), 2678400)

		dstring = '1972-01-01 12:30:01'
		assert_equal(p.date_to_long(dstring, 's'), 63117001)

		dstring = '1980-12-31 23:00:10'
		assert_equal(p.date_to_long(dstring, 's'), 347151610)

		dstring = '2000-01-01 00:00:00'
		assert_equal(p.date_to_long(dstring, 's'), 946684800)

		dstring = '2010-12-20 18:58:29'
		assert_equal(p.date_to_long(dstring, 's'), 1292871509)

	# MILLISECOND
	def test_pre_epoch_millisecond(self):
		"Test creation of milliseconds pre epoch."
	def test_post_epoch_millisecond(self):
		"Test creation of milliseconds post epoch."
		
		dstring = '1970-01-01 00:00:00.000'
		assert_equal(p.date_to_long(dstring, 'ms'), 0)

		dstring = '1970-01-01 00:00:00.001'
		assert_equal(p.date_to_long(dstring, 'ms'), 1)

		dstring = '1970-01-01 12:00:00.020'
		assert_equal(p.date_to_long(dstring, 'ms'), 43200020)

		dstring = '1980-01-01 00:00:00.111'
		assert_equal(p.date_to_long(dstring, 'ms'), 315532800111)

		dstring = '1981-08-15 03:48:28.847'
		assert_equal(p.date_to_long(dstring, 'ms'), 366695308847)

		dstring = '2001-11-27 23:59:59.999'
		assert_equal(p.date_to_long(dstring, 'ms'), 1006905599999)

		dstring = '2002-02-11 22:10:08.001'
		assert_equal(p.date_to_long(dstring, 'ms'), 1013465408001)

	# MICROSECOND
	def test_pre_epoch_microsecond(self):
		"Test creation of microseconds pre epoch."

		dstring = '1969-12-31 23:59:59.999999'
		assert_equal(p.date_to_long(dstring, 'us'), -1)

	def test_post_epoch_microsecond(self):
		"Test creation of microseconds post epoch."

		dstring = '1970-01-01 00:00:00.00'
		assert_equal(p.date_to_long(dstring, 'us'), 0)

		dstring = '1970-01-01 00:00:00.000001'
		assert_equal(p.date_to_long(dstring, 'us'), 1)

		dstring = '1970-01-01 01:01:01.000001'
		assert_equal(p.date_to_long(dstring, 'us'), 3661000001)

		dstring = '1980-12-10 12:30:13.002010'
		assert_equal(p.date_to_long(dstring, 'us'), 345299413002010)

		dstring = '2000-01-01 00:00:00.999999'
		assert_equal(p.date_to_long(dstring, 'us'), 946684800999999)

		dstring = '2001-10-20 00:59:59.000400'
		assert_equal(p.date_to_long(dstring, 'us'), 1003539599000400)

		dstring = '2010-12-31 01:20:00.000080'
		assert_equal(p.date_to_long(dstring, 'us'), 1293758400000080)

	# NANOSECOND
	def test_pre_epoch_nanosecond(self):
		"Test creation of nanoseconds pre epoch."
	def test_post_epoch_nanosecond(self):
		"Test creation of nanoseconds post epoch."
		
		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "ns")

	# PICOSECOND
	def test_pre_epoch_picosecond(self):
		"Test creation of picoseconds pre epoch."
	def test_post_epoch_picosecond(self):
		"Test creation of picoseconds post epoch."

		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "ps")

	# FEMTOSECOND
	def test_pre_epoch_femtosecond(self):
		"Test creation of femtoseconds pre epoch."

		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "fs")

	def test_post_epoch_femtosecond(self):
		"Test creation of femtoseconds post epoch."
	
		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "fs")

	# ATTOSECOND
	def test_pre_epoch_attosecond(self):
		"Test creation of attoseconds pre epoch."

		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "as")

	def test_post_epoch_attosecond(self):
		"Test creation of attoseconds post epoch."

		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "as")

	def test_pre_epoch_leapyears(self):
		"Test years with leap days pre epoch"

	def test_post_epoch_leapyears(self):
		"Test years with leap days post epoch."

