import parsedates as p
import Parser_ts  as dt_parse
import datetime

from numpy.testing import *

p.set_callback(dt_parse.DateTimeFromString)

# All test numbers were pulled from either the SciKits TimeSeries Module (example):
#    >>> print t.Date("Minute", "1970-01-10").value
#    12961
# or the Unix date command (example):
#    $ date -d "1000-01-01 00:00:01 GMT" +%s
#    -30610223999

class TestCreation():
# Test each frequencies' creation and proper value

    ########################################################################
    ## Frequency Tests
    ########################################################################

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

        dstring = '1000-01-05'
        assert_equal(p.date_to_long(dstring, 'W'), -50611)

        dstring = '1000-01-04'
        assert_equal(p.date_to_long(dstring, 'W'), -50612)

        dstring = '0912-04-18'
        assert_equal(p.date_to_long(dstring, 'W'), -55188)

        dstring = '0912-04-19'
        assert_equal(p.date_to_long(dstring, 'W'), -55188)

        dstring = '0912-04-20'
        assert_equal(p.date_to_long(dstring, 'W'), -55188)

        dstring = '0912-04-21'
        assert_equal(p.date_to_long(dstring, 'W'), -55188)

        dstring = '0912-04-22'
        assert_equal(p.date_to_long(dstring, 'W'), -55188)

        dstring = '0912-04-23'
        assert_equal(p.date_to_long(dstring, 'W'), -55188)

        dstring = '0912-04-24'
        assert_equal(p.date_to_long(dstring, 'W'), -55187)

        dstring = '0010-01-10'
        assert_equal(p.date_to_long(dstring, 'W'), -102266)

        dstring = '0010-01-09'
        assert_equal(p.date_to_long(dstring, 'W'), -102267)

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

        dstring = '1969-12-31'
        assert_equal(p.date_to_long(dstring, "B"), -1)

        dstring = '1969-12-30'
        assert_equal(p.date_to_long(dstring, "B"), -2)

        dstring = '1969-12-29'
        assert_equal(p.date_to_long(dstring, "B"), -3)

        dstring = '1969-12-28'
        assert_equal(p.date_to_long(dstring, "B"), -3)

        dstring = '1969-12-27'
        assert_equal(p.date_to_long(dstring, "B"), -3)

        dstring = '1969-12-26'
        assert_equal(p.date_to_long(dstring, "B"), -4)

        dstring = '1969-12-22'
        assert_equal(p.date_to_long(dstring, "B"), -8)

        dstring = '1969-12-21'
        assert_equal(p.date_to_long(dstring, "B"), -8)

        dstring = '1969-01-01'
        assert_equal(p.date_to_long(dstring, "B"), -261)

        dstring = '1900-10-15'
        assert_equal(p.date_to_long(dstring, "B"), -18058)

        dstring = '1403-05-02'
        assert_equal(p.date_to_long(dstring, "B"), -147838)

        dstring = '1403-05-01'
        assert_equal(p.date_to_long(dstring, "B"), -147838)

        dstring = '1403-04-30'
        assert_equal(p.date_to_long(dstring, "B"), -147838)

        dstring = '0100-12-26'
        assert_equal(p.date_to_long(dstring, "B"), -487603)

        dstring = '0100-12-27'
        assert_equal(p.date_to_long(dstring, "B"), -487603)

        dstring = '0001-01-01'
        assert_equal(p.date_to_long(dstring, "B"), -513688)


    def test_post_epoch_business_day(self):
        "Test creation of business days post epoch."
        
        dstring = '1970-01-01'
        assert_equal(p.date_to_long(dstring, "B"), 0)
    
        dstring = '1970-01-02'
        assert_equal(p.date_to_long(dstring, "B"), 1)
    
        dstring = '1970-01-03'
        assert_equal(p.date_to_long(dstring, "B"), 1)
    
        dstring = '1970-01-04'
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

        dstring = '1969-12-31'
        assert_equal(p.date_to_long(dstring, 'D'), -1)

        dstring = '1969-12-30'
        assert_equal(p.date_to_long(dstring, 'D'), -2)

        dstring = '1969-01-01'
        assert_equal(p.date_to_long(dstring, 'D'), -365)

        dstring = '1960-02-01'
        assert_equal(p.date_to_long(dstring, 'D'), -3622)

        dstring = '1900-01-30'
        assert_equal(p.date_to_long(dstring, 'D'), -25538)

        dstring = '1700-10-05'
        assert_equal(p.date_to_long(dstring, 'D'), -98338)

        dstring = '1000-06-02'
        assert_equal(p.date_to_long(dstring, 'D'), -354133)

        dstring = '0900-12-31'
        assert_equal(p.date_to_long(dstring, 'D'), -390445)

        dstring = '0001-01-01'
        assert_equal(p.date_to_long(dstring, 'D'), -719162)

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

        dstring = '1969-12-31 23:00:00'
        assert_equal(p.date_to_long(dstring, 'h'), -1)

        dstring = '1969-12-31 00:00:00'
        assert_equal(p.date_to_long(dstring, 'h'), -24)

        dstring = '1969-01-01 00:00:00'
        assert_equal(p.date_to_long(dstring, 'h'), -8760)

        dstring = '1959-03-01 12:00:00'
        assert_equal(p.date_to_long(dstring, 'h'), -95004)

        dstring = '1900-11-10 01:00:00'
        assert_equal(p.date_to_long(dstring, 'h'), -606095)

        dstring = '1800-01-01 20:00:00'
        assert_equal(p.date_to_long(dstring, 'h'), -1490164)

        dstring = '1750-01-31 00:00:00'
        assert_equal(p.date_to_long(dstring, 'h'), -1927752)

        dstring = '1600-10-10 10:00:00'
        assert_equal(p.date_to_long(dstring, 'h'), -3236558)

        dstring = '0001-01-01 00:00:00'
        assert_equal(p.date_to_long(dstring, 'h'), -17259888)

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

        dstring = '1969-12-31 23:59:00'
        assert_equal(p.date_to_long(dstring, 'm'), -1)

        dstring = '1969-12-31 23:00:00'
        assert_equal(p.date_to_long(dstring, 'm'), -60)

        dstring = '1969-12-31 20:00:00'
        assert_equal(p.date_to_long(dstring, 'm'), -240)

        dstring = '1969-11-30 00:00:00'
        assert_equal(p.date_to_long(dstring, 'm'), -46080)

        dstring = '1960-01-01 00:00:00'
        assert_equal(p.date_to_long(dstring, 'm'), -5260320)

        dstring = '1900-10-15 12:20:00'
        assert_equal(p.date_to_long(dstring, 'm'), -36402460)

        dstring = '1800-01-01 00:01:00'
        assert_equal(p.date_to_long(dstring, 'm'), -89411039)

        dstring = '1700-01-01 20:11:00'
        assert_equal(p.date_to_long(dstring, 'm'), -142004389)

        dstring = '1000-08-20 02:01:00'
        assert_equal(p.date_to_long(dstring, 'm'), -509837639)

        dstring = '0819-03-22 00:58:00'
        assert_equal(p.date_to_long(dstring, 'm'), -605252102)

        dstring = '0001-12-31 23:59:00'
        assert_equal(p.date_to_long(dstring, 'm'), -1035067681)

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

        dstring = '1969-12-31 23:59:59'
        assert_equal(p.date_to_long(dstring, 's'), -1)

        dstring = '1969-12-31 23:59:00'
        assert_equal(p.date_to_long(dstring, 's'), -60)

        dstring = '1969-12-31 23:00:00'
        assert_equal(p.date_to_long(dstring, 's'), -3600)

        dstring = '1969-01-01 00:00:00'
        assert_equal(p.date_to_long(dstring, 's'), -31536000)

        dstring = '1960-02-28 01:01:01'
        assert_equal(p.date_to_long(dstring, 's'), -310604339)

        dstring = '1900-01-15 08:18:58'
        assert_equal(p.date_to_long(dstring, 's'), -2207749262)

        dstring = '1756-01-01 00:00:00'
        assert_equal(p.date_to_long(dstring, 's'), -6753196800)

        dstring = '1000-01-01 00:00:01'
        assert_equal(p.date_to_long(dstring, 's'), -30610223999)

        dstring = '0001-01-01 12:00:00'
        assert_equal(p.date_to_long(dstring, 's'), -62135553600)


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
        
        dstring = '1969-12-31 23:59:59.999'
        assert_equal(p.date_to_long(dstring, 'ms'), -1)

        dstring = '1969-12-31 23:59:59.000'
        assert_equal(p.date_to_long(dstring, 'ms'), -1000)

        dstring = '1969-12-31 23:59:00.000'
        assert_equal(p.date_to_long(dstring, 'ms'), -60000)

        dstring = '1969-12-31 23:00:00.000'
        assert_equal(p.date_to_long(dstring, 'ms'), -3600000)

        dstring = '1969-12-31 00:00:00.000'
        assert_equal(p.date_to_long(dstring, 'ms'), -86400000)

        dstring = '1969-01-01 00:00:00.500'
        assert_equal(p.date_to_long(dstring, 'ms'), -31535999500)

        dstring = '1900-08-10 15:10:08.800'
        assert_equal(p.date_to_long(dstring, 'ms'), -2189839791200)

        dstring = '1821-11-14 05:29:15.111'
        assert_equal(p.date_to_long(dstring, 'ms'), -4674565844889)

        dstring = '1751-01-28 12:12:12.121'
        assert_equal(p.date_to_long(dstring, 'ms'), -6908586467879)

        dstring = '1111-05-29 02:02:48.918'
        assert_equal(p.date_to_long(dstring, 'ms'), -27094687031082)

        dstring = '0001-01-01 12:14:38.398'
        assert_equal(p.date_to_long(dstring, 'ms'), -62135552721602)

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

        dstring = '1969-12-31 23:59:00.000000'
        assert_equal(p.date_to_long(dstring, 'us'), -60000000)

        dstring = '1969-12-31 23:00:00.000000'
        assert_equal(p.date_to_long(dstring, 'us'), -3600000000)

        dstring = '1969-12-31 00:00:00.000000'
        assert_equal(p.date_to_long(dstring, 'us'), -86400000000)

        dstring = '1969-12-20 00:00:00.000900'
        assert_equal(p.date_to_long(dstring, 'us'), -1036799999100)

        dstring = '1969-01-01 00:00:00.120012'
        assert_equal(p.date_to_long(dstring, 'us'), -31535999879988)

        dstring = '1960-10-30 18:47:58.183871'
        assert_equal(p.date_to_long(dstring, 'us'), -289372321816129)

        dstring = '1903-08-05 20:15:01.000001'
        assert_equal(p.date_to_long(dstring, 'us'), -2095645498999999)

        dstring = '1801-01-01 00:01:00.000000'
        assert_equal(p.date_to_long(dstring, 'us'), -5333126340000000)

        dstring = '1700-12-15 15:50:05.098512'
        assert_equal(p.date_to_long(dstring, 'us'), -8490211794901488)

        dstring = '1000-01-31 10:30:18.583018'
        assert_equal(p.date_to_long(dstring, 'us'), -30607594181416982)

        dstring = '0816-04-20 01:28:10.000010'
        assert_equal(p.date_to_long(dstring, 'us'), -36407226709999990)

        dstring = '0001-01-01 12:00:00.888801'
        assert_equal(p.date_to_long(dstring, 'us'), -62135553599111199)

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

        dstring = '1970-01-01 00:00:00.00000'
        assert_raises(NotImplementedError, p.date_to_long, dstring, "ns")

    def test_post_epoch_nanosecond(self):
        "Test creation of nanoseconds post epoch."
        
        dstring = '1970-01-01 00:00:00.00000'
        assert_raises(NotImplementedError, p.date_to_long, dstring, "ns")

    # PICOSECOND
    def test_pre_epoch_picosecond(self):
        "Test creation of picoseconds pre epoch."

        dstring = '1970-01-01 00:00:00.00000'
        assert_raises(NotImplementedError, p.date_to_long, dstring, "ps")

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


    ########################################################################
    ## Leap Year Tests
    ########################################################################

    def test_pre_epoch_leapyears(self):
        "Test years with leap days pre epoch"

		# Days
        dstring = '1968-02-29'
        assert_equal(p.date_to_long(dstring, 'D'), -672)
        dstring = '1964-02-29'
        assert_equal(p.date_to_long(dstring, 'D'), -2133)
        dstring = '1004-02-29'
        assert_equal(p.date_to_long(dstring, 'D'), -352766)
        dstring = '1004-02-28'
        assert_equal(p.date_to_long(dstring, 'D'), -352767)
        dstring = '1004-03-01'
        assert_equal(p.date_to_long(dstring, 'D'), -352765)
        dstring = '0856-02-28'
        assert_equal(p.date_to_long(dstring, 'D'), -406822)
        dstring = '0856-02-29'
        assert_equal(p.date_to_long(dstring, 'D'), -406821)
        dstring = '0856-03-01'
        assert_equal(p.date_to_long(dstring, 'D'), -406820)

		# Business Days
        dstring = '1968-02-29'
        assert_equal(p.date_to_long(dstring, 'B'), -480)
        dstring = '1968-03-01'
        assert_equal(p.date_to_long(dstring, 'B'), -479)
        dstring = '1964-02-29'
        assert_equal(p.date_to_long(dstring, 'B'), -1523)
        dstring = '1964-02-28'
        assert_equal(p.date_to_long(dstring, 'B'), -1524)
        dstring = '1964-03-01'
        assert_equal(p.date_to_long(dstring, 'B'), -1523)
        dstring = '1612-02-28'
        assert_equal(p.date_to_long(dstring, 'B'), -93357)
        dstring = '1612-02-29'
        assert_equal(p.date_to_long(dstring, 'B'), -93356)
        dstring = '1612-03-01'
        assert_equal(p.date_to_long(dstring, 'B'), -93355)

    def test_post_epoch_leapyears(self):
        "Test years with leap days post epoch."

        # Days
        dstring = '1972-02-29'
        assert_equal(p.date_to_long(dstring, 'D'), 789)
        dstring = '2004-02-29'
        assert_equal(p.date_to_long(dstring, 'D'), 12477)
        dstring = '2036-02-29'
        assert_equal(p.date_to_long(dstring, 'D'), 24165)
        dstring = '2036-03-01'
        assert_equal(p.date_to_long(dstring, 'D'), 24166)

		# Business Days
        dstring = '1972-02-28'
        assert_equal(p.date_to_long(dstring, 'B'), 562)
        dstring = '1980-02-29'
        assert_equal(p.date_to_long(dstring, 'B'), 2651)
        dstring = '2004-02-29'
        assert_equal(p.date_to_long(dstring, 'B'), 8911)
        dstring = '2132-02-29'
        assert_equal(p.date_to_long(dstring, 'B'), 42306)

    ########################################################################
    ## September 1752 Tests
    ########################################################################

    def test_september_1752(self):
       	"Assure September 3 - 13, 1752 exist." 
        # September 5, 1752 is a Sunday
        # Weeks
        dstring = '1752-11-03'
        assert_equal(p.date_to_long(dstring, 'W'), -11331)
        dstring = '1752-11-04'
        assert_equal(p.date_to_long(dstring, 'W'), -11331)
        dstring = '1752-11-05'
        assert_equal(p.date_to_long(dstring, 'W'), -11330)
        dstring = '1752-11-06'
        assert_equal(p.date_to_long(dstring, 'W'), -11330)
        dstring = '1752-11-12'
        assert_equal(p.date_to_long(dstring, 'W'), -11329)
        dstring = '1752-11-13'
        assert_equal(p.date_to_long(dstring, 'W'), -11329)

        # Business Days
        dstring = '1752-11-03'
        assert_equal(p.date_to_long(dstring, 'B'), -56654) 
        dstring = '1752-11-04'
        assert_equal(p.date_to_long(dstring, 'B'), -56653) 
        dstring = '1752-11-05'
        assert_equal(p.date_to_long(dstring, 'B'), -56653) 
        dstring = '1752-11-06'
        assert_equal(p.date_to_long(dstring, 'B'), -56653) 
        dstring = '1752-11-12'
        assert_equal(p.date_to_long(dstring, 'B'), -56648) 
        dstring = '1752-11-13'
        assert_equal(p.date_to_long(dstring, 'B'), -56648) 

        # Days
        dstring = '1752-11-03'
        assert_equal(p.date_to_long(dstring, 'D'), -79316) 
        dstring = '1752-11-04'
        assert_equal(p.date_to_long(dstring, 'D'), -79315) 
        dstring = '1752-11-10'
        assert_equal(p.date_to_long(dstring, 'D'), -79309) 
        dstring = '1752-11-11'
        assert_equal(p.date_to_long(dstring, 'D'), -79308) 
        dstring = '1752-11-13'
        assert_equal(p.date_to_long(dstring, 'D'), -79306) 

    ########################################################################
    ## Out of Range Tests
    ########################################################################

    def test_out_of_range(self):
		"Test out of range dates."
