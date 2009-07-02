import parsedates as p
import Parser_ts  as dt_parse
import datetime

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
		
		# Test 1970 - 1979
		dlist = ['197%i' % i for i in range(0, 10)]
		for i in range(0,9):
			assert p.date_to_long(dlist[i], "Y") == i

		# Test 1980 - 1989
		dlist = ['198%i' % i for i in range(0, 10)]
		for i in range(0,9):
			assert p.date_to_long(dlist[i], "Y") == 10 + i

		# Test 1990 - 1999
		dlist = ['197%i' % i for i in range(0, 10)]
		for i in range(0,9):
			assert p.date_to_long(dlist[i], "Y") == 20 + i

		# Test 2000 - 2009
		dlist = ['200%i' % i for i in range(0, 10)]
		for i in range(0,9):
			assert p.date_to_long(dlist[i], "Y") == 30 + i

	def test_post_epoch_month(self):
		"Test creation of months post epoch."
	
		# Test 1970
		dlist = ['1970-%02i' % i for i in range(1, 13)]
		for i in range(0,11):
			assert p.date_to_long(dlist[i], "M") == i

		# Test 1980
		dlist = ['1980-%02i' % i for i in range(1, 13)]
		for i in range(0,11):
			assert p.date_to_long(dlist[i], "M") == 120 + i

		# Test 1990
		dlist = ['1990-%02i' % i for i in range(1, 13)]
		for i in range(0,11):
			assert p.date_to_long(dlist[i], "M") == 240 + i

		# Test 2000
		dlist = ['2000-%02i' % i for i in range(1, 13)]
		for i in range(0,11):
			assert p.date_to_long(dlist[i], "M") == 360 + i

	def test_post_epoch_week(self):
		"Test creation of weeks post epoch."

		# Test Week 1, 1970
		dlist = ['1970-01-%02i' % i for i in range(1,8)]
		for i in range(0,6):
			assert p.date_to_long(dlist[i], "W") == 1

		# Test Week 10, 1970
		dlist = ['1970-03-%02i' % i for i in range(5,12)]
		for i in range(0,6):
			assert p.date_to_long(dlist[i], "W") == 10

		# Test Week 471 in 1980
		dlist = ['1980-01-%02i' % i for i in range(4,11)]
		for i in range(0,6):
			assert p.date_to_long(dlist[i], "W") == 471


	def test_post_epoch_business_day(self):
		"Test creation of business days post epoch."
		# Not sure how to get test numbers yet...
		assert False


	def test_post_epoch_day(self):
		"Test creation of days post epoch."

		# Test January 1970 
		dlist = ['1970-01-%02i' % i for i in range(1, 32)]
		for i in range(0,30):
			assert p.date_to_long(dlist[i], "D") == i

		# Test December 1970 
		dlist = ['1970-12-%02i' % i for i in range(1, 32)]
		for i in range(0,30):
			assert p.date_to_long(dlist[i], "D") == 335 + i

		# Test January 1980 
		dlist = ['1980-01-%02i' % i for i in range(1, 32)]
		for i in range(0,30):
			assert p.date_to_long(dlist[i], "D") == 3288 + i

		# Test June 1980 
		dlist = ['1980-06-%02i' % i for i in range(1, 31)]
		for i in range(0,29):
			assert p.date_to_long(dlist[i], "D") == 3439 + i

		# Test June 1990 
		dlist = ['1990-06-%02i' % i for i in range(1, 31)]
		for i in range(0,29):
			assert p.date_to_long(dlist[i], "D") == 7092 + i

		# Test May 2000 
		dlist = ['2000-05-%02i' % i for i in range(1, 32)]
		for i in range(0,30):
			assert p.date_to_long(dlist[i], "D") == 10713 + i

		# Test January 2010
		dlist = ['2010-01-%02i' % i for i in range(1, 32)]
		for i in range(0,30):
			assert p.date_to_long(dlist[i], "D") == 14245 + i

	def test_post_epoch_hour(self):
		"Test creation of hours post epoch."

		# Test January 1, 1970
		dlist = ['1970-01-01 %02i:00:00' % i for i in range(0,24)]
		for i in range(0,23):
			assert p.date_to_long(dlist[i], "h") == 1 + i

		# Test February 1, 1970
		dlist = ['1970-02-01 %02i:00:00' % i for i in range(0,24)]
		for i in range(0,23):
			assert p.date_to_long(dlist[i], "h") == 745 + i

		# Test December 1, 1975
		dlist = ['1975-12-01 %02i:00:00' % i for i in range(0,24)]
		for i in range(0,23):
			assert p.date_to_long(dlist[i], "h") == 51941 + i

		# Test December 31, 1975
		dlist = ['1975-12-31 %02i:00:00' % i for i in range(0,24)]
		for i in range(0,23):
			assert p.date_to_long(dlist[i], "h") == 52561 + i

		# Test May 10, 1981
		dlist = ['1981-05-10 %02i:00:00' % i for i in range(0,24)]
		for i in range(0,23):
			assert p.date_to_long(dlist[i], "h") == 99529 + i

		# Test January 1, 2000
		dlist = ['2000-01-01 %02i:00:00' % i for i in range(0,24)]
		for i in range(0,23):
			assert p.date_to_long(dlist[i], "h") == 262969 + i

		# Test March 25, 2009
		dlist = ['2009-05-25 %02i:00:00' % i for i in range(0,24)]
		for i in range(0,23):
			assert p.date_to_long(dlist[i], "h") == 345337 + i
		
		# Test January 1, 2010
		dlist = ['2010-01-01 %02i:00:00' % i for i in range(0,24)]
		for i in range(0,23):
			assert p.date_to_long(dlist[i], "h") == 350641 + i

		# Test January 1, 2060
		dlist = ['2060-01-01 %02i:00:00' % i for i in range(0,24)]
		for i in range(0,23):
			assert p.date_to_long(dlist[i], "h") == 788929 + i
		

	def test_post_epoch_minute(self):
		"Test creation of minutes post epoch."

		# Test January 1, 1970 (00:00:00 to 00:59:00)
		dlist = ['1970-01-01 00:%02i:00' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 1 + i

		# Test January 1, 1970 (12:00:00 to 12:59:00)
		dlist = ['1970-01-01 12:%02i:00' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 721 + i

		# Test January 1, 1970 (23:00:00 to 23:59:00)
		dlist = ['1970-01-01 23:%02i:00' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 1381 + i

		# Test January 1, 1971 (00:00:00 to 00:59:00)
		dlist = ['1971-01-01 00:%02i:00' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 525601 + i

		# Test December 1, 1971 (00:00:00 to 00:59:00)
		dlist = ['1970-12-01 00:%02i:00' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 1006561 + i

		# Test December 31, 1980 (06:00:00 to 06:59:00)
		dlist = ['1970-12-31 00:%02i:00' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 5784481 + i

		# Test May 10, 2000 (00:00:00 to 00:59:00)
		dlist = ['2000-10-01 00:%02i:00' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 15965281 + i

		# Test August 1, 2010 (15:00:00 to 15:59:00)
		dlist = ['2010-08-01 15:%02i:00' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 21344581 + i

	def test_post_epoch_second(self):
		"Test creation of seconds post epoch."

		# Test January 1, 1970 (00:00:00 to 00:00:59)
		dlist = ['1970-01-01 00:00:%02i' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 1 + i

		# Test January 1, 1970 (23:59:00 to 23:59:59)
		dlist = ['1970-01-01 23:59:%02i' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 86341 + i

		# Test January 1, 1980 (00:00:00 to 00:00:59)
		dlist = ['1980-01-01 00:00:%02i' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 315532801 + i

		# Test Febuary 15, 1999 (00:01:00 to 00:01:59)
		dlist = ['1999-02-15 00:01:%02i' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 919036861 + i

		# Test December 31, 2008 (23:59:00 to 23:59:59)
		dlist = ['2008-12-31 23:59:%02i' % i for i in range(0,60)]
		for i in range(0,59):
			assert p.date_to_long(dlist[i], "m") == 1230767941 + i

	def test_post_epoch_millisecond(self):
		"Test creation of milliseconds post epoch."
		assert False

	def test_post_epoch_microsecond(self):
		"Test creation of microseconds post epoch."
		assert False

	def test_post_epoch_nanosecond(self):
		"Test creation of nanoseconds post epoch."
		assert False
	def test_post_epoch_picosecond(self):
		"Test creation of picoseconds post epoch."
		assert False

	def test_post_epoch_femtosecond(self):
		"Test creation of femtoseconds post epoch."
		assert False

	def test_post_epoch_attosecond(self):
		"Test creation of attoseconds post epoch."
		assert False


	def test_ones(self):
		"Test January 1, 1970 at XXX is 0 for each frequency"
		for f in freqs:
			assert p.date_to_long("01/01/1970 00:00:00", f) == 1

