import parsedates as p
import Parser_ts  as dt_parse
import datetime as d

from numpy.testing import *

p.set_callback(dt_parse.DateTimeFromString)

# All test numbers were pulled from either the SciKits TimeSeries Module (example), 
#    >>> print t.Date("Minute", "1970, 1, 10").value
#    12961
# or the Unix date command (example), 
#    $ date -d "1000, 1, 1 0, 0, 1 GMT" +%s
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
        assert_equal(p.long_to_datetime(dlong, 'Y'), d.datetime(1969, 1, 1))

        dlong = -30L
        assert_equal(p.long_to_datetime(dlong, 'Y'), d.datetime(1940, 1, 1))

        dlong = -970L
        assert_equal(p.long_to_datetime(dlong, 'Y'), d.datetime(1000, 1, 1))

        dlong = -1969L
        assert_equal(p.long_to_datetime(dlong, 'Y'), d.datetime(1, 1, 1))

    def test_post_epoch_year(self): 
        "Test creation of years post epoch."
        
        dlong = 0L
        assert_equal(p.long_to_datetime(dlong, 'Y'), d.datetime(1970, 1, 1))

        dlong = 10L
        assert_equal(p.long_to_datetime(dlong, 'Y'), d.datetime(1980, 1, 1))

        dlong = 40L
        assert_equal(p.long_to_datetime(dlong, 'Y'), d.datetime(2010, 1, 1))

    # MONTH
    def test_pre_epoch_month(self): 
        "Test creation of months pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1969, 12, 1))

        dlong = -12L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1969, 1, 1))

        dlong = -240L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1950, 1, 1))

        dlong = -835L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1900, 6, 1))

        dlong = -5735L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1492, 2, 1))

        dlong = -11640L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1000, 1, 1))

        dlong = -14031L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(800, 10, 1))

        dlong = -23628L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1, 1, 1))

    def test_post_epoch_month(self): 
        "Test creation of months post epoch."
    
        dlong = 0L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1970, 1, 1))

        dlong = 11L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1970, 12, 1))

        dlong = 120L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1980, 1, 1))

        dlong = 313L
        assert_equal(p.long_to_datetime(dlong, 'M'), d.datetime(1996, 2, 1))

    # WEEK
    def test_pre_epoch_week(self): 
        "Test creation of weeks pre epoch."
        
        dlong = 0L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1969, 12, 28))

        dlong = -1L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1969, 12, 21))

        dlong = -51L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1969, 1, 5))

        dlong = -52L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1968, 12, 29))

        dlong = -3621L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1900, 8, 5))

        dlong = -3622L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1900, 7, 29))

        dlong = -6190L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1851, 5, 11))

        dlong = -6189L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1851, 5, 18))

        dlong = -50611L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1000, 1, 5))

        dlong = -50612L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(999, 12, 29))

        dlong = -55188L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(912, 4, 17))

        dlong = -55187L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(912, 4, 24))

        dlong = -102266L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(10, 1, 10))

        dlong = -102267L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(10, 1, 3))

    def test_post_epoch_week(self): 
        "Test creation of weeks post epoch."

        dlong = 1L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1970, 1, 4))
        
        dlong = 2L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1970, 1, 11))
        
        dlong = 9L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1970, 3, 1))

        dlong = 10L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1970, 3, 8))

        dlong = 522L
        assert_equal(p.long_to_datetime(dlong, "W"), d.datetime(1979, 12, 30))

        dlong = 523L
        assert_equal(p.long_to_datetime(dlong, "W"), d.datetime(1980, 1, 6))

        dlong = 1600L
        assert_equal(p.long_to_datetime(dlong, "W"), d.datetime(2000, 8, 27))

        dlong = 1601L
        assert_equal(p.long_to_datetime(dlong, "W"), d.datetime(2000, 9, 3))

        dlong = 11582L
        assert_equal(p.long_to_datetime(dlong, "W"), d.datetime(2191, 12, 18))

        dlong = 11583L
        assert_equal(p.long_to_datetime(dlong, "W"), d.datetime(2191, 12, 25))

        dlong = 11584L
        assert_equal(p.long_to_datetime(dlong, "W"), d.datetime(2192, 1, 1))

    # BUSINESS DAY
    def test_pre_epoch_business(self): 
        "Test creation of business days pre epoch."

        # XXX Needs to be rewritten for Weekends
        dlong = -1L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1969, 12, 31))

        dlong = -2L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1969, 12, 30))

        dlong = -3L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1969, 12, 29))

        dlong = -4L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1969, 12, 26))

        dlong = -8L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1969, 12, 22))

        dlong = -9L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1969, 12, 19))

        dlong = -261L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1969, 1, 1))

        dlong = -18058L
        assert_equal(p.long_to_datetime(dlong, "B"),d.datetime(1900, 10, 15))

        dlong = -147838L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1403, 5, 2))

        dlong = -487604L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(100, 12, 24))

        dlong = -513688L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1, 1, 1))


    def test_post_epoch_business_day(self): 
        "Test creation of business days post epoch."
        
        # XXX Needs to be rewritten for Weekends
        dlong = 0L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1970, 1, 1))
    
        dlong = 1L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1970, 1, 2))
    
        dlong = 3L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1970, 1, 6))
    
        dlong = 6L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1970, 1, 9))
    
        dlong = 10L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1970, 1, 15))
    
        dlong = 21L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1970, 1, 30))
    
        dlong = 91L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1970, 5, 8))
    
        dlong = 1564L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1975, 12, 31))
    
        dlong = 2608L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(1980, 1, 1))
    
        dlong = 10651L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(2010, 10, 29))
    
        dlong = 10652L
        assert_equal(p.long_to_datetime(dlong, "B"), d.datetime(2010, 11, 1))
    
    # DAY
    def test_pre_epoch_day(self): 
        "Test creation of days pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1969, 12, 31))

        dlong = -2L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1969, 12, 30))

        dlong = -365L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1969, 1, 1))

        dlong = -3622L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1960, 2, 1))

        dlong = -25538L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1900, 1, 30))

        dlong = -98338L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1700, 10, 5))

        dlong = -354133L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1000, 6, 2))

        dlong = -390445L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(900, 12, 31))

        dlong = -719162L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1, 1, 1))

    def test_post_epoch_day(self): 
        "Test creation of days post epoch."

        dlong = 0L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1970, 1, 1))

        dlong = 1L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1970, 1, 2))

        dlong = 334L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1970, 12, 1))

        dlong = 3652L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1980, 1, 1))

        dlong = 7465L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1990, 6, 10))

        dlong = 10957L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(2000, 1, 1))

        dlong = 12783L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(2004, 12, 31))

    # HOUR
    def test_pre_epoch_hour(self): 
        "Test creation of hours pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1969, 12, 31, 23, 0, 0))

        dlong = -24L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1969, 12, 31, 0, 0, 0))

        dlong = -8760L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1969, 1, 1, 0, 0, 0))

        dlong = -95004L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1959, 3, 1, 12, 0, 0))

        dlong = -606095L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1900, 11, 10, 1, 0, 0))

        dlong = -1490164L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1800, 1, 1, 20, 0, 0))

        dlong = -1927752L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1750, 1, 31, 0, 0, 0))

        dlong = -3236558L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1600, 10, 10, 10, 0, 0))

        dlong = -17259888L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1, 1, 1, 0, 0, 0))

    def test_post_epoch_hour(self): 
        "Test creation of hours post epoch."

        dlong = 0L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1970, 1, 1, 0, 0, 0))
        
        dlong = 1L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1970, 1, 1, 1, 0, 0))
        
        dlong = 756L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1970, 2, 1, 12, 0, 0))

        dlong = 7128L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1970, 10, 25, 0, 0, 0))

        dlong = 52583L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(1975, 12, 31, 23, 0, 0))

        dlong = 271753L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(2001, 1, 1, 1, 0, 0))

        dlong = 353532L
        assert_equal(p.long_to_datetime(dlong, 'h'), d.datetime(2010, 5, 1, 12, 0, 0))

    # MINUTE
    def test_pre_epoch_minute(self): 
        "Test creation of minutes pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1969, 12, 31, 23, 59, 0))

        dlong = -60L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1969, 12, 31, 23, 0, 0))

        dlong = -240L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1969, 12, 31, 20, 0, 0))

        dlong = -46080L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1969, 11, 30, 0, 0, 0))

        dlong = -5260320L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1960, 1, 1, 0, 0, 0))

        dlong = -36402460L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1900, 10, 15, 12, 20, 0))

        dlong = -89411039L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1800, 1, 1, 0, 1, 0))

        dlong = -142004389L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1700, 1, 1, 20, 11, 0))

        dlong = -509837639L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1000, 8, 20, 2, 1, 0))

        dlong = -605252102L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(819, 3, 22, 0, 58, 0))

        dlong = -1035067681L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1, 12, 31, 23, 59, 0))

    def test_post_epoch_minute(self): 
        "Test creation of minutes post epoch."

        dlong = 0L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1970, 1, 1, 0, 0, 0))

        dlong = 1L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1970, 1, 1, 0, 1, 0))

        dlong = 720L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1970, 1, 1, 12, 0, 0))

        dlong = 172800L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1970, 5, 1, 0, 0, 0))
        
        dlong = 525601L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1971, 1, 1, 0, 1, 0))

        dlong = 2630879L
        assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(1975, 1, 1, 23, 59, 0))

        dlong = 16233210L
    	assert_equal(p.long_to_datetime(dlong, 'm'), d.datetime(2000, 11, 12, 1, 30, 0))

    # SECOND
    def test_pre_epoch_second(self): 
        "Test creation of seconds pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1969, 12, 31, 23, 59, 59))

        dlong = -60L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1969, 12, 31, 23, 59, 0))

        dlong = -3600L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1969, 12, 31, 23, 0, 0))

        dlong = -31536000L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1969, 1, 1, 0, 0, 0))

        dlong = -310604339L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1960, 2, 28, 1, 1, 1))

        dlong = -2207749262L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1900, 1, 15, 8, 18, 58))

        dlong = -6753196800L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1756, 1, 1, 0, 0, 0))

        dlong = -30610223999L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1000, 1, 1, 0, 0, 1))

        dlong = -62135553600L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1, 1, 1, 12, 0, 0))


    def test_post_epoch_second(self): 
        "Test creation of seconds post epoch."

        dlong = 0L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1970, 1, 1, 0, 0, 0))

        dlong = 1L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1970, 1, 1, 0, 0, 1))

        dlong = 2678400L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1970, 2, 1, 0, 0, 0))

        dlong = 63117001L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1972, 1, 1, 12, 30, 1))

        dlong = 347151610L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(1980, 12, 31, 23, 0, 10))

        dlong = 946684800L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(2000, 1, 1, 0, 0, 0))

        dlong = 1292871509L
        assert_equal(p.long_to_datetime(dlong, 's'), d.datetime(2010, 12, 20, 18, 58, 29))

    # MILLISECOND
    def test_pre_epoch_millisecond(self): 
        "Test creation of milliseconds pre epoch."
        
        dlong = -1L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1969, 12, 31, 23, 59, 59, 999000))

        dlong = -1000L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1969, 12, 31, 23, 59, 59, 0))

        dlong = -60000L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1969, 12, 31, 23, 59, 0, 0))

        dlong = -3600000L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1969, 12, 31, 23, 0, 0, 0))

        dlong = -86400000L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1969, 12, 31, 0, 0, 0, 0))

        dlong = -31535999500L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1969, 1, 1, 0, 0, 0, 500000))

        dlong = -2189839791200L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1900, 8, 10, 15, 10, 8, 800000))

        dlong = -4674565844889L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1821, 11, 14, 5, 29, 15, 111000))

        dlong = -6908586467879L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1751, 1, 28, 12, 12, 12, 121000))

        dlong = -27094687031082L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1111, 5, 29, 2, 2, 48, 918000))

        dlong = -62135552721602L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1, 1, 1, 12, 14, 38, 398000))

    def test_post_epoch_millisecond(self): 
        "Test creation of milliseconds post epoch."
        
        dlong = 0L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1970, 1, 1, 0, 0, 0, 0))

        dlong = 1L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1970, 1, 1, 0, 0, 0, 1000))

        dlong = 43200020L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1970, 1, 1, 12, 0, 0, 20000))

        dlong = 315532800111L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1980, 1, 1, 0, 0, 0, 111000))

        dlong = 366695308847L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(1981, 8, 15, 3, 48, 28, 847000))

        dlong = 1006905599999L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(2001, 11, 27, 23, 59, 59, 999000))

        dlong = 1013465408001L
        assert_equal(p.long_to_datetime(dlong, 'ms'), d.datetime(2002, 2, 11, 22, 10, 8, 1000))

    # MICROSECOND
    def test_pre_epoch_microsecond(self): 
        "Test creation of microseconds pre epoch."

        dlong = -1L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1969, 12, 31, 23, 59, 59, 999999))

        dlong = -60000000L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1969, 12, 31, 23, 59, 0, 0))

        dlong = -3600000000L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1969, 12, 31, 23, 0, 0, 0))

        dlong = -86400000000L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1969, 12, 31, 0, 0, 0, 0))

        dlong = -1036799999100L 
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1969, 12, 20, 0, 0, 0, 900))

        dlong = -31535999879988L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1969, 1, 1, 0, 0, 0, 120012))

        dlong = -289372321816129L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1960, 10, 30, 18, 47, 58, 183871))

        dlong = -2095645498999999L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1903, 8, 5, 20, 15, 1, 1))

        dlong = -5333126340000000L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1801, 1, 1, 0, 1, 0, 0))

        dlong = -8490211794901488L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1700, 12, 15, 15, 50, 5, 98512))

        dlong = -30607594181416982L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1000, 1, 31, 10, 30, 18, 583018))

        dlong = -36407226709999990L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(816, 4, 20, 1, 28, 10, 10))

        dlong = -62135553599111199L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1, 1, 1, 12, 0, 0, 888801))

    def test_post_epoch_microsecond(self): 
        "Test creation of microseconds post epoch."

        dlong = 0L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1970, 1, 1, 0, 0, 0, 0))

        dlong = 1L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1970, 1, 1, 0, 0, 0, 1))

        dlong = 3661000001L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1970, 1, 1, 1, 1, 1, 1))

        dlong = 345299413002010L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(1980, 12, 10, 12, 30, 13, 2010))

        dlong = 946684800999999L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(2000, 1, 1, 0, 0, 0, 999999))

        dlong = 1003539599000400L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(2001, 10, 20, 0, 59, 59, 400))

        dlong = 1293758400000080L
        assert_equal(p.long_to_datetime(dlong, 'us'), d.datetime(2010, 12, 31, 1, 20, 0, 80))

    # NANOSECOND
    def test_pre_epoch_nanosecond(self): 
        "Test creation of nanoseconds pre epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datetime, dlong, "ns")

    def test_post_epoch_nanosecond(self): 
        "Test creation of nanoseconds post epoch."
        
        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datetime, dlong, "ns")

    # PICOSECOND
    def test_pre_epoch_picosecond(self): 
        "Test creation of picoseconds pre epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datetime, dlong, "ps")

    def test_post_epoch_picosecond(self): 
        "Test creation of picoseconds post epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datetime, dlong, "ps")

    # FEMTOSECOND
    def test_pre_epoch_femtosecond(self): 
        "Test creation of femtoseconds pre epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datetime, dlong, "fs")

    def test_post_epoch_femtosecond(self): 
        "Test creation of femtoseconds post epoch."
    
        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datetime, dlong, "fs")

    # ATTOSECOND
    def test_pre_epoch_attosecond(self): 
        "Test creation of attoseconds pre epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datetime, dlong, "as")

    def test_post_epoch_attosecond(self): 
        "Test creation of attoseconds post epoch."

        dlong = 0L
        assert_raises(NotImplementedError, p.long_to_datetime, dlong, "as")


    ########################################################################
    ## Leap Year Tests
    ########################################################################

    def test_pre_epoch_leapyears(self): 
        "Test years with leap days pre epoch"

    	# Days
        dlong = -672L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1968, 2, 29))
        dlong = -2133L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1964, 2, 29))
        dlong = -352766L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1004, 2, 29))
        dlong = -352767L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1004, 2, 28))
        dlong = -352765L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1004, 3, 1))
        dlong = -406822L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(856, 2, 28))
        dlong = -406821L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(856, 2, 29))
        dlong = -406820L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(856, 3, 1))

    	# Business Days
        dlong = -480L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1968, 2, 29))
        dlong = -479L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1968, 3, 1))
        dlong = -1524L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1964, 2, 28))
        dlong = -1523L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1964, 3, 2))
        dlong = -93357L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1612, 2, 28))
        dlong = -93356L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1612, 2, 29))
        dlong = -93355L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1612, 3, 1))

    def test_post_epoch_leapyears(self): 
        "Test years with leap days post epoch."

        # Days
        dlong = 789L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1972, 2, 29))
        dlong = 12477L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(2004, 2, 29))
        dlong = 24165L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(2036, 2, 29))
        dlong = 24166L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(2036, 3, 1))

    	# Business Days
        dlong = 562L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1972, 2, 28))
        dlong = 2651L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1980, 2, 29))
        dlong = 8911L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(2004, 2, 27))
        dlong = 42306L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(2132, 2, 29))

    ########################################################################
    ## September 1752 Tests
    ########################################################################

    def test_september_1752(self): 
        "Assure September 3 - 13, 1752 exist." 
        # September 5, 1752 is a Sunday
        # Weeks
        dlong = -11330L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1752, 11, 5))
        dlong = -11329L
        assert_equal(p.long_to_datetime(dlong, 'W'), d.datetime(1752, 11, 12))

        # Days
        dlong = -79316L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1752, 11, 3))
        dlong = -79315L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1752, 11, 4))
        dlong = -79309L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1752, 11, 10))
        dlong = -79308L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1752, 11, 11))
        dlong = -79306L
        assert_equal(p.long_to_datetime(dlong, 'D'), d.datetime(1752, 11, 13))
        
		# Business Days
        dlong = -56654L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1752, 11, 3))
        dlong = -56653L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1752, 11, 6))
        dlong = -56648L
        assert_equal(p.long_to_datetime(dlong, 'B'), d.datetime(1752, 11, 13))

    ########################################################################
    ## Sanity Check
    ########################################################################

    def test_sanity(self):
        "Sanity check."

        # Doesn't test Y, M, W, B because of specific dates in dstring_dict
        #  Wouldn't be a problem to test for them, and might not be a bad idea
        #  But those tests would be extraneous for a simple sanity check
        freq_list    = ['D', 'h', 'm', 's', 'ms', 'us']
        dstring_dict = {'1800-01-01': (1800, 1, 1), '1960-02-02': (1960, 2, 2), \
                        '1970-01-01': (1970, 1, 1), '1980-01-01': (1980, 1, 1), 
                        '2001-07-18': (2001, 7, 18), '2002-12-31': (2002, 12, 31),
                        '2010-12-10': (2010, 12, 10),  '2020-02-19': (2020, 2, 19)}
        for freq in freq_list:
            for dstring, dtuple in dstring_dict.items():
                assert_equal(p.long_to_datetime(p.date_to_long(dstring, freq), freq), \
							 d.datetime(*dtuple))
                         

    ########################################################################
    ## Out of Range Tests
    ########################################################################

    def test_out_of_range(self): 
        "Test out of range dates."

