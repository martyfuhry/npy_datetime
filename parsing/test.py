import parsedates as p
import Parser_ts as dt_parse

p.set_callback(dt_parse.DateTimeFromString)

def basic_test():
	dates = list()
	dates.append(p.parse_date("01/01/1970", "D"))
	dates.append(p.parse_date("12/01/1970", "MTH"))
	dates.append(p.parse_date("01/01/1980", "Y"))

	assert dates[0][0] == 0
	assert dates[1][0] == 12
	assert dates[2][0] == 10


