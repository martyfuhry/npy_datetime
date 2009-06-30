import types
import npy_datetime as d

import numpy as np
from numpy.testing import *

from numpy import ma
from numpy.ma.testutils import assert_equal, assert_array_equal

class TestCreation(TestCase):

	def __init__(self, *args, **kwds):
		TestCase.__init__(self, *args, **kwds)

	def test_basic_creation(self):
		"Can I create basic datetime64 types?"
		
		# Make some basic dates
		d1 = d.datetime(1,86400)
		d2 = d.datetime(2,10)
		d3 = d.datetime(3,12)
		d4 = d.datetime(4,-100)

		# Check frequencies
		assert_equal(d1.freq,1)
		assert_equal(d2.freq,2)
		assert_equal(d3.freq,3)
		assert_equal(d4.freq,4)

		# Check times
		assert_equal(d1.time,86400)
		assert_equal(d2.time,10)
		assert_equal(d3.time,12)
		assert_equal(d4.time,-100)


	#def test_from_direct(self):
		#"Tests creation from a list of direct time values and freqs"
		
		# Minutes 1 - 10 starting from the Epoch
		#for i in xrange(1,10):
			#dates.append(d.datetime64('S', i * 60)
		
		# Assert dates are right minutes
		#for i in xrange(1,10):
			# Do something

#################################################################
#----------------------------------------------------------------

if __name__ == "__main__":
	run_module_suite()
