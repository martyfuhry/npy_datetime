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

	def test_post_epoch_year(self):
		"Test creation of years post epoch."
		
		dstring = '1970'
		assert_equal(p.date_to_long(dstring, 'Y'), 0)

		dstring = '1980'
		assert_equal(p.date_to_long(dstring, 'Y'), 10)

		dstring = '2010'
		assert_equal(p.date_to_long(dstring, 'Y'), 40)

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

	def test_post_epoch_week(self):
		"Test creation of weeks post epoch."

		dstring = '1970-01-01'
		assert_equal(p.date_to_long(dstring, 'W'), 0)
		
		dstring = '1970-03-05'
		assert_equal(p.date_to_long(dstring, 'W'), 9)

		dstring = '1980-01-04' 
		assert_equal(p.date_to_long(dstring, "W"), 470)

	def test_post_epoch_business_day(self):
		"Test creation of business days post epoch."
		# Not sure how to get test numbers yet...
		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "B")

	def test_post_epoch_day(self):
		"Test creation of days post epoch."

		dstring = '1970-01-01'
		assert_equal(p.date_to_long(dstring, 'D'), 0)

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

	def test_post_epoch_hour(self):
		"Test creation of hours post epoch."

		dstring = '1970-01-01 00:00:00'
		assert_equal(p.date_to_long(dstring, 'h'), 0)
		
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

	def test_post_epoch_minute(self):
		"Test creation of minutes post epoch."

		dstring = '1970-01-01 00:00:00'
		assert_equal(p.date_to_long(dstring, 'm'), 0)

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

	def test_post_epoch_second(self):
		"Test creation of seconds post epoch."

		dstring = '1970-01-01 00:00:00'
		assert_equal(p.date_to_long(dstring, 's'), 0)

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

	def test_post_epoch_millisecond(self):
		"Test creation of milliseconds post epoch."
		
		dstring = '1970-01-01 00:00:00.000'
		assert_equal(p.date_to_long(dstring, 'ms'), 0)

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

	def test_post_epoch_microsecond(self):
		"Test creation of microseconds post epoch."

		dstring = '1970-01-01 00:00:00.00'
		assert_equal(p.date_to_long(dstring, 'us'), 0)

	def test_post_epoch_nanosecond(self):
		"Test creation of nanoseconds post epoch."
		
		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "ns")

	def test_post_epoch_picosecond(self):
		"Test creation of picoseconds post epoch."

		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "ps")

	def test_post_epoch_femtosecond(self):
		"Test creation of femtoseconds post epoch."
	
		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "fs")


	def test_post_epoch_attosecond(self):
		"Test creation of attoseconds post epoch."

		dstring = '1970-01-01 00:00:00.00000'
		assert_raises(NotImplementedError, p.date_to_long, dstring, "as")

	def tests_post_epoch_leapyears(self):
		"Test years with leap days."

