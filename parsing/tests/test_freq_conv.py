import parsedates as p
import Parser_ts  as dt_parse
import datetime as d

from numpy.testing import *

p.set_callback(dt_parse.DateTimeFromString)

class TestFreqConv():

    def test_Y2M(self):
        'Test frequency conversions from Y to M.'
        input   =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        control =  [-23520L, -11628L, -2640L, -12L, 0L, 120L, 480L, 1584L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'M', 'Y'), control[x])

    def test_Y2W(self):
        'Test frequency conversions from Y to W.'
        input   =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        control =  [-102268L, -50560L, -11479L, -52L, 0L, 522L, 2087L, 6888L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'W', 'Y'), control[x])

    def test_Y2B(self):
        'Test frequency conversions from Y to B.'
        input   =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        control =  [-511339L, -252800L, -57395L, -261L, 0L, 2608L, 10436L, 34436L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'B', 'Y'), control[x])

    def test_Y2D(self):
        'Test frequency conversions from Y to D.'
        input   =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        control =  [-715875L, -353920L, -80353L, -365L, 0L, 3652L, 14610L, 48212L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'D', 'Y'), control[x])

    def test_Y2h(self):
        'Test frequency conversions from Y to h.'
        input   =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        control =  [-17181000L, -8494080L, -1928472L, -8760L, 0L, 87648L, 350640L, 1157088L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'h', 'Y'), control[x])

    def test_Y2m(self):
        'Test frequency conversions from Y to m.'
        input   =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        control =  [-1030860000L, -509644800L, -115708320L, -525600L, 0L, 5258880L, 21038400L, 69425280L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'm', 'Y'), control[x])

    def test_Y2s(self):
        'Test frequency conversions from Y to s.'
        input   =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        control =  [-61851600000L, -30578688000L, -6942499200L, -31536000L, 0L, 315532800L, 1262304000L, 4165516800L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 's', 'Y'), control[x])

    def test_Y2ms(self):
        'Test frequency conversions from Y to ms.'
        input   =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        control =  [-61851600000000L, -30578688000000L, -6942499200000L, -31536000000L, 0L, 315532800000L, 1262304000000L, 4165516800000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'ms', 'Y'), control[x])

    def test_Y2us(self):
        'Test frequency conversions from Y to us.'
        input   =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        control =  [-61851600000000000L, -30578688000000000L, -6942499200000000L, -31536000000000L, 0L, 315532800000000L, 1262304000000000L, 4165516800000000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'us', 'Y'), control[x])

    def test_M2Y(self):
        'Test frequency conversions from M to Y.'
        input   =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        control =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'Y', 'M'), control[x])

    def test_M2W(self):
        'Test frequency conversions from M to W.'
        input   =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        control =  [-102268L, -50512L, -11431L, -26L, 9L, 570L, 2118L, 6918L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'W', 'M'), control[x])

    def test_M2B(self):
        'Test frequency conversions from M to B.'
        input   =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        control =  [-511339L, -252562L, -57157L, -132L, 41L, 2847L, 10586L, 34588L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'B', 'M'), control[x])

    def test_M2D(self):
        'Test frequency conversions from M to D.'
        input   =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        control =  [-715875L, -353586L, -80019L, -184L, 59L, 3987L, 14822L, 48424L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'D', 'M'), control[x])

    def test_M2h(self):
        'Test frequency conversions from M to h.'
        input   =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        control =  [-17181000L, -8486064L, -1920456L, -4416L, 1416L, 95688L, 355728L, 1162176L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'h', 'M'), control[x])

    def test_M2m(self):
        'Test frequency conversions from M to m.'
        input   =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        control =  [-1030860000L, -509163840L, -115227360L, -264960L, 84960L, 5741280L, 21343680L, 69730560L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'm', 'M'), control[x])

    def test_M2s(self):
        'Test frequency conversions from M to s.'
        input   =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        control =  [-61851600000L, -30549830400L, -6913641600L, -15897600L, 5097600L, 344476800L, 1280620800L, 4183833600L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 's', 'M'), control[x])

    def test_M2ms(self):
        'Test frequency conversions from M to ms.'
        input   =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        control =  [-61851600000000L, -30549830400000L, -6913641600000L, -15897600000L, 5097600000L, 344476800000L, 1280620800000L, 4183833600000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'ms', 'M'), control[x])

    def test_M2us(self):
        'Test frequency conversions from M to us.'
        input   =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        control =  [-61851600000000000L, -30549830400000000L, -6913641600000000L, -15897600000000L, 5097600000000L, 344476800000000L, 1280620800000000L, 4183833600000000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'us', 'M'), control[x])

    def test_W2Y(self):
        'Test frequency conversions from W to Y.'
        input   =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        control =  [-1961L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'Y', 'W'), control[x])

    def test_W2M(self):
        'Test frequency conversions from W to M.'
        input   =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        control =  [-23521L, -11617L, -2629L, -7L, 2L, 130L, 487L, 1590L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'M', 'W'), control[x])

    def test_W2B(self):
        'Test frequency conversions from W to B.'
        input   =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        control =  [-511343L, -252543L, -57138L, -133L, 41L, 2846L, 10586L, 34586L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'B', 'W'), control[x])

    def test_W2D(self):
        'Test frequency conversions from W to D.'
        input   =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        control =  [-715880L, -353560L, -79993L, -186L, 59L, 3986L, 14822L, 48422L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'D', 'W'), control[x])

    def test_W2h(self):
        'Test frequency conversions from W to h.'
        input   =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        control =  [-17181120L, -8485440L, -1919832L, -4464L, 1416L, 95664L, 355728L, 1162128L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'h', 'W'), control[x])

    def test_W2m(self):
        'Test frequency conversions from W to m.'
        input   =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        control =  [-1030867200L, -509126400L, -115189920L, -267840L, 84960L, 5739840L, 21343680L, 69727680L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'm', 'W'), control[x])

    def test_W2s(self):
        'Test frequency conversions from W to s.'
        input   =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        control =  [-61852032000L, -30547584000L, -6911395200L, -16070400L, 5097600L, 344390400L, 1280620800L, 4183660800L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 's', 'W'), control[x])

    def test_W2ms(self):
        'Test frequency conversions from W to ms.'
        input   =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        control =  [-61852032000000L, -30547584000000L, -6911395200000L, -16070400000L, 5097600000L, 344390400000L, 1280620800000L, 4183660800000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'ms', 'W'), control[x])

    def test_W2us(self):
        'Test frequency conversions from W to us.'
        input   =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        control =  [-61852032000000000L, -30547584000000000L, -6911395200000000L, -16070400000000L, 5097600000000L, 344390400000000L, 1280620800000000L, 4183660800000000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'us', 'W'), control[x])

    def test_B2Y(self):
        'Test frequency conversions from B to Y.'
        input   =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        control =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'Y', 'B'), control[x])

    def test_B2M(self):
        'Test frequency conversions from B to M.'
        input   =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        control =  [-23520L, -11617L, -2629L, -6L, 1L, 131L, 486L, 1591L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'M', 'B'), control[x])

    def test_B2W(self):
        'Test frequency conversions from B to W.'
        input   =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        control =  [-102268L, -50508L, -11427L, -26L, 8L, 570L, 2117L, 6918L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'W', 'B'), control[x])

    def test_B2D(self):
        'Test frequency conversions from B to D.'
        input   =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        control =  [-715875L, -353557L, -79989L, -184L, 57L, 3988L, 14820L, 48424L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'D', 'B'), control[x])

    def test_B2h(self):
        'Test frequency conversions from B to h.'
        input   =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        control =  [-17181000L, -8485368L, -1919736L, -4416L, 1368L, 95712L, 355680L, 1162176L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'h', 'B'), control[x])

    def test_B2m(self):
        'Test frequency conversions from B to m.'
        input   =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        control =  [-1030860000L, -509122080L, -115184160L, -264960L, 82080L, 5742720L, 21340800L, 69730560L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'm', 'B'), control[x])

    def test_B2s(self):
        'Test frequency conversions from B to s.'
        input   =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        control =  [-61851600000L, -30547324800L, -6911049600L, -15897600L, 4924800L, 344563200L, 1280448000L, 4183833600L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 's', 'B'), control[x])

    def test_B2ms(self):
        'Test frequency conversions from B to ms.'
        input   =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        control =  [-61851600000000L, -30547324800000L, -6911049600000L, -15897600000L, 4924800000L, 344563200000L, 1280448000000L, 4183833600000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'ms', 'B'), control[x])

    def test_B2us(self):
        'Test frequency conversions from B to us.'
        input   =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        control =  [-61851600000000000L, -30547324800000000L, -6911049600000000L, -15897600000000L, 4924800000000L, 344563200000000L, 1280448000000000L, 4183833600000000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'us', 'B'), control[x])

    def test_D2Y(self):
        'Test frequency conversions from D to Y.'
        input   =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        control =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'Y', 'D'), control[x])

    def test_D2M(self):
        'Test frequency conversions from D to M.'
        input   =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        control =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'M', 'D'), control[x])

    def test_D2W(self):
        'Test frequency conversions from D to W.'
        input   =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        control =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'W', 'D'), control[x])

    def test_D2B(self):
        'Test frequency conversions from D to B.'
        input   =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        control =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'B', 'D'), control[x])

    def test_D2h(self):
        'Test frequency conversions from D to h.'
        input   =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        control =  [-17181000L, -8485368L, -1919736L, -4416L, 1416L, 95712L, 355728L, 1162176L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'h', 'D'), control[x])

    def test_D2m(self):
        'Test frequency conversions from D to m.'
        input   =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        control =  [-1030860000L, -509122080L, -115184160L, -264960L, 84960L, 5742720L, 21343680L, 69730560L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'm', 'D'), control[x])

    def test_D2s(self):
        'Test frequency conversions from D to s.'
        input   =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        control =  [-61851600000L, -30547324800L, -6911049600L, -15897600L, 5097600L, 344563200L, 1280620800L, 4183833600L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 's', 'D'), control[x])

    def test_D2ms(self):
        'Test frequency conversions from D to ms.'
        input   =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        control =  [-61851600000000L, -30547324800000L, -6911049600000L, -15897600000L, 5097600000L, 344563200000L, 1280620800000L, 4183833600000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'ms', 'D'), control[x])

    def test_D2us(self):
        'Test frequency conversions from D to us.'
        input   =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        control =  [-61851600000000000L, -30547324800000000L, -6911049600000000L, -15897600000000L, 5097600000000L, 344563200000000L, 1280620800000000L, 4183833600000000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'us', 'D'), control[x])

    def test_h2Y(self):
        'Test frequency conversions from h to Y.'
        input   =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        control =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'Y', 'h'), control[x])

    def test_h2M(self):
        'Test frequency conversions from h to M.'
        input   =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        control =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'M', 'h'), control[x])

    def test_h2W(self):
        'Test frequency conversions from h to W.'
        input   =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        control =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'W', 'h'), control[x])

    def test_h2B(self):
        'Test frequency conversions from h to B.'
        input   =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        control =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'B', 'h'), control[x])

    def test_h2D(self):
        'Test frequency conversions from h to D.'
        input   =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        control =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'D', 'h'), control[x])

    def test_h2m(self):
        'Test frequency conversions from h to m.'
        input   =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        control =  [-1030859940L, -509121360L, -115183320L, -264780L, 84960L, 5744040L, 21343800L, 69731160L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'm', 'h'), control[x])

    def test_h2s(self):
        'Test frequency conversions from h to s.'
        input   =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        control =  [-61851596400L, -30547281600L, -6910999200L, -15886800L, 5097600L, 344642400L, 1280628000L, 4183869600L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 's', 'h'), control[x])

    def test_h2ms(self):
        'Test frequency conversions from h to ms.'
        input   =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        control =  [-61851596400000L, -30547281600000L, -6910999200000L, -15886800000L, 5097600000L, 344642400000L, 1280628000000L, 4183869600000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'ms', 'h'), control[x])

    def test_h2us(self):
        'Test frequency conversions from h to us.'
        input   =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        control =  [-61851596400000000L, -30547281600000000L, -6910999200000000L, -15886800000000L, 5097600000000L, 344642400000000L, 1280628000000000L, 4183869600000000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'us', 'h'), control[x])

    def test_m2Y(self):
        'Test frequency conversions from m to Y.'
        input   =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        control =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'Y', 'm'), control[x])

    def test_m2M(self):
        'Test frequency conversions from m to M.'
        input   =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        control =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'M', 'm'), control[x])

    def test_m2W(self):
        'Test frequency conversions from m to W.'
        input   =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        control =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'W', 'm'), control[x])

    def test_m2B(self):
        'Test frequency conversions from m to B.'
        input   =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        control =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'B', 'm'), control[x])

    def test_m2D(self):
        'Test frequency conversions from m to D.'
        input   =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        control =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'D', 'm'), control[x])

    def test_m2h(self):
        'Test frequency conversions from m to h.'
        input   =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        control =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'h', 'm'), control[x])

    def test_m2s(self):
        'Test frequency conversions from m to s.'
        input   =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        control =  [-61851595680L, -30547280880L, -6910997520L, -15885960L, 5098680L, 344643720L, 1280630880L, 4183869720L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 's', 'm'), control[x])

    def test_m2ms(self):
        'Test frequency conversions from m to ms.'
        input   =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        control =  [-61851595680000L, -30547280880000L, -6910997520000L, -15885960000L, 5098680000L, 344643720000L, 1280630880000L, 4183869720000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'ms', 'm'), control[x])

    def test_m2us(self):
        'Test frequency conversions from m to us.'
        input   =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        control =  [-61851595680000000L, -30547280880000000L, -6910997520000000L, -15885960000000L, 5098680000000L, 344643720000000L, 1280630880000000L, 4183869720000000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'us', 'm'), control[x])

    def test_s2Y(self):
        'Test frequency conversions from s to Y.'
        input   =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        control =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'Y', 's'), control[x])

    def test_s2M(self):
        'Test frequency conversions from s to M.'
        input   =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        control =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'M', 's'), control[x])

    def test_s2W(self):
        'Test frequency conversions from s to W.'
        input   =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        control =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'W', 's'), control[x])

    def test_s2B(self):
        'Test frequency conversions from s to B.'
        input   =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        control =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'B', 's'), control[x])

    def test_s2D(self):
        'Test frequency conversions from s to D.'
        input   =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        control =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'D', 's'), control[x])

    def test_s2h(self):
        'Test frequency conversions from s to h.'
        input   =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        control =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'h', 's'), control[x])

    def test_s2m(self):
        'Test frequency conversions from s to m.'
        input   =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        control =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'm', 's'), control[x])

    def test_s2ms(self):
        'Test frequency conversions from s to ms.'
        input   =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        control =  [-61851595650000L, -30547280860000L, -6910997461000L, -15885941000L, 5098738000L, 344643742000L, 1280630910000L, 4183869740000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'ms', 's'), control[x])

    def test_s2us(self):
        'Test frequency conversions from s to us.'
        input   =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        control =  [-61851595650000000L, -30547280860000000L, -6910997461000000L, -15885941000000L, 5098738000000L, 344643742000000L, 1280630910000000L, 4183869740000000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'us', 's'), control[x])

    def test_ms2Y(self):
        'Test frequency conversions from ms to Y.'
        input   =  [-61851595649818L, -30547280859999L, -6910997460001L, -15885940900L, 5098738810L, 344643742222L, 1280630910333L, 4183869740200L]
        control =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'Y', 'ms'), control[x])

    def test_ms2M(self):
        'Test frequency conversions from ms to M.'
        input   =  [-61851595649818L, -30547280859999L, -6910997460001L, -15885940900L, 5098738810L, 344643742222L, 1280630910333L, 4183869740200L]
        control =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'M', 'ms'), control[x])

    def test_ms2W(self):
        'Test frequency conversions from ms to W.'
        input   =  [-61851595649818L, -30547280859999L, -6910997460001L, -15885940900L, 5098738810L, 344643742222L, 1280630910333L, 4183869740200L]
        control =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'W', 'ms'), control[x])

    def test_ms2B(self):
        'Test frequency conversions from ms to B.'
        input   =  [-61851595649818L, -30547280859999L, -6910997460001L, -15885940900L, 5098738810L, 344643742222L, 1280630910333L, 4183869740200L]
        control =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'B', 'ms'), control[x])

    def test_ms2D(self):
        'Test frequency conversions from ms to D.'
        input   =  [-61851595649818L, -30547280859999L, -6910997460001L, -15885940900L, 5098738810L, 344643742222L, 1280630910333L, 4183869740200L]
        control =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'D', 'ms'), control[x])

    def test_ms2h(self):
        'Test frequency conversions from ms to h.'
        input   =  [-61851595649818L, -30547280859999L, -6910997460001L, -15885940900L, 5098738810L, 344643742222L, 1280630910333L, 4183869740200L]
        control =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'h', 'ms'), control[x])

    def test_ms2m(self):
        'Test frequency conversions from ms to m.'
        input   =  [-61851595649818L, -30547280859999L, -6910997460001L, -15885940900L, 5098738810L, 344643742222L, 1280630910333L, 4183869740200L]
        control =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'm', 'ms'), control[x])

    def test_ms2s(self):
        'Test frequency conversions from ms to s.'
        input   =  [-61851595649818L, -30547280859999L, -6910997460001L, -15885940900L, 5098738810L, 344643742222L, 1280630910333L, 4183869740200L]
        control =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 's', 'ms'), control[x])

    def test_ms2us(self):
        'Test frequency conversions from ms to us.'
        input   =  [-61851595649818L, -30547280859999L, -6910997460001L, -15885940900L, 5098738810L, 344643742222L, 1280630910333L, 4183869740200L]
        control =  [-61851595649818000L, -30547280859999000L, -6910997460001000L, -15885940900000L, 5098738810000L, 344643742222000L, 1280630910333000L, 4183869740200000L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'us', 'ms'), control[x])

    def test_us2Y(self):
        'Test frequency conversions from us to Y.'
        input   =  [-61851595649817169L, -30547280859999000L, -6910997460000001L, -15885940899991L, 5098738810000L, 344643742222220L, 1280630910333001L, 4183869740200100L]
        control =  [-1960L, -969L, -220L, -1L, 0L, 10L, 40L, 132L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'Y', 'us'), control[x])

    def test_us2M(self):
        'Test frequency conversions from us to M.'
        input   =  [-61851595649817169L, -30547280859999000L, -6910997460000001L, -15885940899991L, 5098738810000L, 344643742222220L, 1280630910333001L, 4183869740200100L]
        control =  [-23520L, -11617L, -2629L, -6L, 2L, 131L, 487L, 1591L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'M', 'us'), control[x])

    def test_us2W(self):
        'Test frequency conversions from us to W.'
        input   =  [-61851595649817169L, -30547280859999000L, -6910997460000001L, -15885940899991L, 5098738810000L, 344643742222220L, 1280630910333001L, 4183869740200100L]
        control =  [-102268L, -50508L, -11427L, -26L, 9L, 570L, 2118L, 6918L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'W', 'us'), control[x])

    def test_us2B(self):
        'Test frequency conversions from us to B.'
        input   =  [-61851595649817169L, -30547280859999000L, -6910997460000001L, -15885940899991L, 5098738810000L, 344643742222220L, 1280630910333001L, 4183869740200100L]
        control =  [-511339L, -252541L, -57135L, -132L, 41L, 2848L, 10586L, 34588L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'B', 'us'), control[x])

    def test_us2D(self):
        'Test frequency conversions from us to D.'
        input   =  [-61851595649817169L, -30547280859999000L, -6910997460000001L, -15885940899991L, 5098738810000L, 344643742222220L, 1280630910333001L, 4183869740200100L]
        control =  [-715875L, -353557L, -79989L, -184L, 59L, 3988L, 14822L, 48424L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'D', 'us'), control[x])

    def test_us2h(self):
        'Test frequency conversions from us to h.'
        input   =  [-61851595649817169L, -30547280859999000L, -6910997460000001L, -15885940899991L, 5098738810000L, 344643742222220L, 1280630910333001L, 4183869740200100L]
        control =  [-17180999L, -8485356L, -1919722L, -4413L, 1416L, 95734L, 355730L, 1162186L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'h', 'us'), control[x])

    def test_us2m(self):
        'Test frequency conversions from us to m.'
        input   =  [-61851595649817169L, -30547280859999000L, -6910997460000001L, -15885940899991L, 5098738810000L, 344643742222220L, 1280630910333001L, 4183869740200100L]
        control =  [-1030859928L, -509121348L, -115183292L, -264766L, 84978L, 5744062L, 21343848L, 69731162L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'm', 'us'), control[x])

    def test_us2s(self):
        'Test frequency conversions from us to s.'
        input   =  [-61851595649817169L, -30547280859999000L, -6910997460000001L, -15885940899991L, 5098738810000L, 344643742222220L, 1280630910333001L, 4183869740200100L]
        control =  [-61851595650L, -30547280860L, -6910997461L, -15885941L, 5098738L, 344643742L, 1280630910L, 4183869740L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 's', 'us'), control[x])

    def test_us2ms(self):
        'Test frequency conversions from us to ms.'
        input   =  [-61851595649817169L, -30547280859999000L, -6910997460000001L, -15885940899991L, 5098738810000L, 344643742222220L, 1280630910333001L, 4183869740200100L]
        control =  [-61851595649818L, -30547280859999L, -6910997460001L, -15885940900L, 5098738810L, 344643742222L, 1280630910333L, 4183869740200L]
        for x in xrange(0,len(input)):
            assert_equal(p.convert_freq(input[x], 'ms', 'us'), control[x])

