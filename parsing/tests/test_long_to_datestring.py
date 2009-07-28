import parsedates as p
import Parser_ts  as dt_parse
import datetime as d

from numpy.testing import *

p.set_callback(dt_parse.DateTimeFromString)

# All test numbers were pulled from either the SciKits TimeSeries Module (example), 
#    >>> print t.Date("Minute", "1970-01-10").value
#    12961
# or the Unix date command (example), 
#    $ date -d "1000-01-01 0-0-01 GMT" +%s
#    -30610223999

class TestCreation():
# Test each frequencies' creation and proper value

    ########################################################################
    ## Frequency Tests
    ########################################################################

    # YEAR
    def test_pre_epoch_year(self): 
        "Test creation of years pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datestring(dlong, 'Y'), "1969-01-01")

        dlong = -30L
        assert_equal(p.long_to_datestring(dlong, 'Y'), "1940-01-01")

        dlong = -970L
        assert_equal(p.long_to_datestring(dlong, 'Y'), "1000-01-01")

        dlong = -1969L
        assert_equal(p.long_to_datestring(dlong, 'Y'), "0001-01-01")

    def test_post_epoch_year(self): 
        "Test creation of years post epoch."
        
        dlong = 0L
        assert_equal(p.long_to_datestring(dlong, 'Y'), "1970-01-01")

        dlong = 10L
        assert_equal(p.long_to_datestring(dlong, 'Y'), "1980-01-01")

        dlong = 40L
        assert_equal(p.long_to_datestring(dlong, 'Y'), "2010-01-01")

    # MONTH
    def test_pre_epoch_month(self): 
        "Test creation of months pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datestring(dlong, 'M'), "1969-12-01")

        dlong = -12L
        assert_equal(p.long_to_datestring(dlong, 'M'), "1969-01-01")

        dlong = -240L
        assert_equal(p.long_to_datestring(dlong, 'M'), "1950-01-01")

        dlong = -835L
        assert_equal(p.long_to_datestring(dlong, 'M'), "1900-06-01")

        dlong = -5735L
        assert_equal(p.long_to_datestring(dlong, 'M'), "1492-02-01")

        dlong = -11640L
        assert_equal(p.long_to_datestring(dlong, 'M'), "1000-01-01")

        dlong = -14031L
        assert_equal(p.long_to_datestring(dlong, 'M'), "0800-10-01")

        dlong = -23628L
        assert_equal(p.long_to_datestring(dlong, 'M'), "0001-01-01")

    def test_post_epoch_month(self): 
        "Test creation of months post epoch."
    
        dlong = 0L
        assert_equal(p.long_to_datestring(dlong, 'M'), "1970-01-01")

        dlong = 11L
        assert_equal(p.long_to_datestring(dlong, 'M'), "1970-12-01")

        dlong = 120L
        assert_equal(p.long_to_datestring(dlong, 'M'), "1980-01-01")

        dlong = 313L
        assert_equal(p.long_to_datestring(dlong, 'M'), "1996-02-01")

    # WEEK
    def test_pre_epoch_week(self): 
        "Test creation of weeks pre epoch."
        
        dlong = 0L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1969-12-28")

        dlong = -1L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1969-12-21")

        dlong = -51L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1969-01-05")

        dlong = -52L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1968-12-29")

        dlong = -3621L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1900-08-05")

        dlong = -3622L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1900-07-29")

        dlong = -6190L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1851-05-11")

        dlong = -6189L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1851-05-18")

        dlong = -50611L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1000-01-05")

        dlong = -50612L
        assert_equal(p.long_to_datestring(dlong, 'W'), "0999-12-29")

        dlong = -55188L
        assert_equal(p.long_to_datestring(dlong, 'W'), "0912-04-17")

        dlong = -55187L
        assert_equal(p.long_to_datestring(dlong, 'W'), "0912-04-24")

        dlong = -102266L
        assert_equal(p.long_to_datestring(dlong, 'W'), "0010-01-10")

        dlong = -102267L
        assert_equal(p.long_to_datestring(dlong, 'W'), "0010-01-03")

    def test_post_epoch_week(self): 
        "Test creation of weeks post epoch."

        dlong = 1L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1970-01-04")
        
        dlong = 2L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1970-01-11")
        
        dlong = 9L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1970-03-01")

        dlong = 10L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1970-03-08")

        dlong = 522L
        assert_equal(p.long_to_datestring(dlong, "W"), "1979-12-30")

        dlong = 523L
        assert_equal(p.long_to_datestring(dlong, "W"), "1980-01-06")

        dlong = 1600L
        assert_equal(p.long_to_datestring(dlong, "W"), "2000-08-27")

        dlong = 1601L
        assert_equal(p.long_to_datestring(dlong, "W"), "2000-09-03")

        dlong = 11582L
        assert_equal(p.long_to_datestring(dlong, "W"), "2191-12-18")

        dlong = 11583L
        assert_equal(p.long_to_datestring(dlong, "W"), "2191-12-25")

        dlong = 11584L
        assert_equal(p.long_to_datestring(dlong, "W"), "2192-01-01")

    # BUSINESS DAY
    def test_pre_epoch_business(self): 
        "Test creation of business days pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datestring(dlong, "B"), "1969-12-31")

        dlong = -2L
        assert_equal(p.long_to_datestring(dlong, "B"), "1969-12-30")

        dlong = -3L
        assert_equal(p.long_to_datestring(dlong, "B"), "1969-12-29")

        dlong = -4L
        assert_equal(p.long_to_datestring(dlong, "B"), "1969-12-26")

        dlong = -8L
        assert_equal(p.long_to_datestring(dlong, "B"), "1969-12-22")

        dlong = -9L
        assert_equal(p.long_to_datestring(dlong, "B"), "1969-12-19")

        dlong = -261L
        assert_equal(p.long_to_datestring(dlong, "B"), "1969-01-01")

        dlong = -18058L
        assert_equal(p.long_to_datestring(dlong, "B"), "1900-10-15")

        dlong = -147838L
        assert_equal(p.long_to_datestring(dlong, "B"), "1403-05-02")

        dlong = -487604L
        assert_equal(p.long_to_datestring(dlong, "B"), "0100-12-24")

        dlong = -513688L
        assert_equal(p.long_to_datestring(dlong, "B"), "0001-01-01")


    def test_post_epoch_business_day(self): 
        "Test creation of business days post epoch."
        
        # XXX Needs to be rewritten for Weekends
        dlong = 0L
        assert_equal(p.long_to_datestring(dlong, "B"), "1970-01-01")
    
        dlong = 1L
        assert_equal(p.long_to_datestring(dlong, "B"), "1970-01-02")
    
        dlong = 3L
        assert_equal(p.long_to_datestring(dlong, "B"), "1970-01-06")
    
        dlong = 6L
        assert_equal(p.long_to_datestring(dlong, "B"), "1970-01-09")
    
        dlong = 10L
        assert_equal(p.long_to_datestring(dlong, "B"), "1970-01-15")
    
        dlong = 21L
        assert_equal(p.long_to_datestring(dlong, "B"), "1970-01-30")
    
        dlong = 91L
        assert_equal(p.long_to_datestring(dlong, "B"), "1970-05-08")
    
        dlong = 1564L
        assert_equal(p.long_to_datestring(dlong, "B"), "1975-12-31")
    
        dlong = 2608L
        assert_equal(p.long_to_datestring(dlong, "B"), "1980-01-01")
    
        dlong = 10651L
        assert_equal(p.long_to_datestring(dlong, "B"), "2010-10-29")
    
        dlong = 10652L
        assert_equal(p.long_to_datestring(dlong, "B"), "2010-11-01")
    
    # DAY
    def test_pre_epoch_day(self): 
        "Test creation of days pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1969-12-31")

        dlong = -2L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1969-12-30")

        dlong = -365L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1969-01-01")

        dlong = -3622L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1960-02-01")

        dlong = -25538L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1900-01-30")

        dlong = -98338L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1700-10-05")

        dlong = -354133L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1000-06-02")

        dlong = -390445L
        assert_equal(p.long_to_datestring(dlong, 'D'), "0900-12-31")

        dlong = -719162L
        assert_equal(p.long_to_datestring(dlong, 'D'), "0001-01-01")

    def test_post_epoch_day(self): 
        "Test creation of days post epoch."

        dlong = 0L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1970-01-01")

        dlong = 1L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1970-01-02")

        dlong = 334L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1970-12-01")

        dlong = 3652L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1980-01-01")

        dlong = 7465L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1990-06-10")

        dlong = 10957L
        assert_equal(p.long_to_datestring(dlong, 'D'), "2000-01-01")

        dlong = 12783L
        assert_equal(p.long_to_datestring(dlong, 'D'), "2004-12-31")

    # HOUR
    def test_pre_epoch_hour(self): 
        "Test creation of hours pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1969-12-31 23:00:00")

        dlong = -24L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1969-12-31 00:00:00")

        dlong = -8760L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1969-01-01 00:00:00")

        dlong = -95004L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1959-03-01 12:00:00")

        dlong = -606095L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1900-11-10 01:00:00")

        dlong = -1490164L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1800-01-01 20:00:00")

        dlong = -1927752L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1750-01-31 00:00:00")

        dlong = -3236558L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1600-10-10 10:00:00")

        dlong = -17259888L
        assert_equal(p.long_to_datestring(dlong, 'h'), "0001-01-01 00:00:00")

    def test_post_epoch_hour(self): 
        "Test creation of hours post epoch."

        dlong = 0L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1970-01-01 00:00:00")
        
        dlong = 1L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1970-01-01 01:00:00")
        
        dlong = 756L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1970-02-01 12:00:00")

        dlong = 7128L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1970-10-25 00:00:00")

        dlong = 52583L
        assert_equal(p.long_to_datestring(dlong, 'h'), "1975-12-31 23:00:00")

        dlong = 271753L
        assert_equal(p.long_to_datestring(dlong, 'h'), "2001-01-01 01:00:00")

        dlong = 353532L
        assert_equal(p.long_to_datestring(dlong, 'h'), "2010-05-01 12:00:00")

    # MINUTE
    def test_pre_epoch_minute(self): 
        "Test creation of minutes pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1969-12-31 23:59:00")

        dlong = -60L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1969-12-31 23:00:00")

        dlong = -240L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1969-12-31 20:00:00")

        dlong = -46080L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1969-11-30 00:00:00")

        dlong = -5260320L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1960-01-01 00:00:00")

        dlong = -36402460L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1900-10-15 12:20:00")

        dlong = -89411039L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1800-01-01 00:01:00")

        dlong = -142004389L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1700-01-01 20:11:00")

        dlong = -509837639L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1000-08-20 02:01:00")

        dlong = -605252102L
        assert_equal(p.long_to_datestring(dlong, 'm'), "0819-03-22 00:58:00")

        dlong = -1035067681L
        assert_equal(p.long_to_datestring(dlong, 'm'), "0001-12-31 23:59:00")

    def test_post_epoch_minute(self): 
        "Test creation of minutes post epoch."

        dlong = 0L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1970-01-01 00:00:00")

        dlong = 1L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1970-01-01 00:01:00")

        dlong = 720L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1970-01-01 12:00:00")

        dlong = 172800L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1970-05-01 00:00:00")
        
        dlong = 525601L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1971-01-01 00:01:00")

        dlong = 2630879L
        assert_equal(p.long_to_datestring(dlong, 'm'), "1975-01-01 23:59:00")

        dlong = 16233210L
        assert_equal(p.long_to_datestring(dlong, 'm'), "2000-11-12 01:30:00")

    # SECOND
    def test_pre_epoch_second(self): 
        "Test creation of seconds pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datestring(dlong, 's'), "1969-12-31 23:59:59")

        dlong = -60L
        assert_equal(p.long_to_datestring(dlong, 's'), "1969-12-31 23:59:00")

        dlong = -3600L
        assert_equal(p.long_to_datestring(dlong, 's'), "1969-12-31 23:00:00")

        dlong = -31536000L
        assert_equal(p.long_to_datestring(dlong, 's'), "1969-01-01 00:00:00")

        dlong = -310604339L
        assert_equal(p.long_to_datestring(dlong, 's'), "1960-02-28 01:01:01")

        dlong = -2207749262L
        assert_equal(p.long_to_datestring(dlong, 's'), "1900-01-15 08:18:58")

        dlong = -6753196800L
        assert_equal(p.long_to_datestring(dlong, 's'), "1756-01-01 00:00:00")

        dlong = -30610223999L
        assert_equal(p.long_to_datestring(dlong, 's'), "1000-01-01 00:00:01")

        dlong = -62135553600L
        assert_equal(p.long_to_datestring(dlong, 's'), "0001-01-01 12:00:00")


    def test_post_epoch_second(self): 
        "Test creation of seconds post epoch."

        dlong = 0L
        assert_equal(p.long_to_datestring(dlong, 's'), "1970-01-01 00:00:00")

        dlong = 1L
        assert_equal(p.long_to_datestring(dlong, 's'), "1970-01-01 00:00:01")

        dlong = 2678400L
        assert_equal(p.long_to_datestring(dlong, 's'), "1970-02-01 00:00:00")

        dlong = 63117001L
        assert_equal(p.long_to_datestring(dlong, 's'), "1972-01-01 12:30:01")

        dlong = 347151610L
        assert_equal(p.long_to_datestring(dlong, 's'), "1980-12-31 23:00:10")

        dlong = 946684800L
        assert_equal(p.long_to_datestring(dlong, 's'), "2000-01-01 00:00:00")

        dlong = 1292871509L
        assert_equal(p.long_to_datestring(dlong, 's'), "2010-12-20 18:58:29")

    # MILLISECOND
    def test_pre_epoch_millisecond(self): 
        "Test creation of milliseconds pre epoch."
        
        dlong = -1L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1969-12-31 23:59:59.999000")

        dlong = -1000L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1969-12-31 23:59:59.0")

        dlong = -60000L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1969-12-31 23:59:00.0")

        dlong = -3600000L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1969-12-31 23:00:00.0")

        dlong = -86400000L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1969-12-31 00:00:00.0")

        dlong = -31535999500L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1969-01-01 00:00:00.500000")

        dlong = -2189839791200L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1900-08-10 15:10:08.800000")

        dlong = -4674565844889L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1821-11-14 05:29:15.111000")

        dlong = -6908586467879L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1751-01-28 12:12:12.121000")

        dlong = -27094687031082L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1111-05-29 02:02:48.918000")

        dlong = -62135552721602L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "0001-01-01 12:14:38.398000")

    def test_post_epoch_millisecond(self): 
        "Test creation of milliseconds post epoch."
        
        dlong = 0L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1970-01-01 00:00:00.0")

        dlong = 1L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1970-01-01 00:00:00.1000")

        dlong = 43200020L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1970-01-01 12:00:00.20000")

        dlong = 315532800111L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1980-01-01 00:00:00.111000")

        dlong = 366695308847L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "1981-08-15 03:48:28.847000")

        dlong = 1006905599999L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "2001-11-27 23:59:59.999000")

        dlong = 1013465408001L
        assert_equal(p.long_to_datestring(dlong, 'ms'), "2002-02-11 22:10:08.1000")

    # MICROSECOND
    def test_pre_epoch_microsecond(self): 
        "Test creation of microseconds pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1969-12-31 23:59:59.999999")

        dlong = -60000000L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1969-12-31 23:59:00.0")

        dlong = -3600000000L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1969-12-31 23:00:00.0")

        dlong = -86400000000L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1969-12-31 00:00:00.0")

        dlong = -1036799999100L 
        assert_equal(p.long_to_datestring(dlong, 'us'), "1969-12-20 00:00:00.900")

        dlong = -31535999879988L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1969-01-01 00:00:00.120012")

        dlong = -289372321816129L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1960-10-30 18:47:58.183871")

        dlong = -2095645498999999L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1903-08-05 20:15:01.1")

        dlong = -5333126340000000L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1801-01-01 00:01:00.0")

        dlong = -8490211794901488L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1700-12-15 15:50:05.98512")

        dlong = -30607594181416982L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1000-01-31 10:30:18.583018")

        dlong = -36407226709999990L
        assert_equal(p.long_to_datestring(dlong, 'us'), "0816-04-20 01:28:10.10")

        dlong = -62135553599111199L
        assert_equal(p.long_to_datestring(dlong, 'us'), "0001-01-01 12:00:00.888801")

    def test_post_epoch_microsecond(self): 
        "Test creation of microseconds post epoch."

        dlong = 0L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1970-01-01 00:00:00.0")

        dlong = 1L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1970-01-01 00:00:00.1")

        dlong = 3661000001L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1970-01-01 01:01:01.1")

        dlong = 345299413002010L
        assert_equal(p.long_to_datestring(dlong, 'us'), "1980-12-10 12:30:13.2010")

        dlong = 946684800999999L
        assert_equal(p.long_to_datestring(dlong, 'us'), "2000-01-01 00:00:00.999999")

        dlong = 1003539599000400L
        assert_equal(p.long_to_datestring(dlong, 'us'), "2001-10-20 00:59:59.400")

        dlong = 1293758400000080L
        assert_equal(p.long_to_datestring(dlong, 'us'), "2010-12-31 01:20:00.80")

    # NANOSECOND
    def test_pre_epoch_nanosecond(self): 
        "Test creation of nanoseconds pre epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datestring, dlong, "ns")

    def test_post_epoch_nanosecond(self): 
        "Test creation of nanoseconds post epoch."
        
        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datestring, dlong, "ns")

    # PICOSECOND
    def test_pre_epoch_picosecond(self): 
        "Test creation of picoseconds pre epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datestring, dlong, "ps")

    def test_post_epoch_picosecond(self): 
        "Test creation of picoseconds post epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datestring, dlong, "ps")

    # FEMTOSECOND
    def test_pre_epoch_femtosecond(self): 
        "Test creation of femtoseconds pre epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datestring, dlong, "fs")

    def test_post_epoch_femtosecond(self): 
        "Test creation of femtoseconds post epoch."
    
        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datestring, dlong, "fs")

    # ATTOSECOND
    def test_pre_epoch_attosecond(self): 
        "Test creation of attoseconds pre epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datestring, dlong, "as")

    def test_post_epoch_attosecond(self): 
        "Test creation of attoseconds post epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datestring, dlong, "as")


    ########################################################################
    ## Leap Year Tests
    ########################################################################

    def test_pre_epoch_leapyears(self): 
        "Test years with leap days pre epoch"

        # Days
        dlong = -672L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1968-02-29")
        dlong = -2133L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1964-02-29")
        dlong = -352766L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1004-02-29")
        dlong = -352767L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1004-02-28")
        dlong = -352765L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1004-03-01")
        dlong = -406822L
        assert_equal(p.long_to_datestring(dlong, 'D'), "0856-02-28")
        dlong = -406821L
        assert_equal(p.long_to_datestring(dlong, 'D'), "0856-02-29")
        dlong = -406820L
        assert_equal(p.long_to_datestring(dlong, 'D'), "0856-03-01")

        # Business Days
        dlong = -480L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1968-02-29")
        dlong = -479L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1968-03-01")
        dlong = -1524L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1964-02-28")
        dlong = -1523L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1964-03-02")
        dlong = -93357L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1612-02-28")
        dlong = -93356L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1612-02-29")
        dlong = -93355L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1612-03-01")

    def test_post_epoch_leapyears(self): 
        "Test years with leap days post epoch."

        # Days
        dlong = 789L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1972-02-29")
        dlong = 12477L
        assert_equal(p.long_to_datestring(dlong, 'D'), "2004-02-29")
        dlong = 24165L
        assert_equal(p.long_to_datestring(dlong, 'D'), "2036-02-29")
        dlong = 24166L
        assert_equal(p.long_to_datestring(dlong, 'D'), "2036-03-01")

        # Business Days
        dlong = 562L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1972-02-28")
        dlong = 2651L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1980-02-29")
        dlong = 8911L
        assert_equal(p.long_to_datestring(dlong, 'B'), "2004-02-27")
        dlong = 42306L
        assert_equal(p.long_to_datestring(dlong, 'B'), "2132-02-29")

    ########################################################################
    ## September 1752 Tests
    ########################################################################

    def test_september_1752(self): 
        "Assure September 3 - 13-1752 exist." 
        # September 5-1752 is a Sunday
        # Weeks
        dlong = -11330L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1752-11-05")
        dlong = -11329L
        assert_equal(p.long_to_datestring(dlong, 'W'), "1752-11-12")

        # Days
        dlong = -79316L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1752-11-03")
        dlong = -79315L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1752-11-04")
        dlong = -79309L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1752-11-10")
        dlong = -79308L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1752-11-11")
        dlong = -79306L
        assert_equal(p.long_to_datestring(dlong, 'D'), "1752-11-13")
        
        # Business Days
        dlong = -56654L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1752-11-03")
        dlong = -56653L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1752-11-06")
        dlong = -56648L
        assert_equal(p.long_to_datestring(dlong, 'B'), "1752-11-13")

    ########################################################################
    ## Out of Range Tests
    ########################################################################

    def test_out_of_range(self): 
        "Test out of range dates."

