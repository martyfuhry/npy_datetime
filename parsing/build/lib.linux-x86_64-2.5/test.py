import parsedates

def parse(args):
 print "Arguments are: ", args

def add_ints(a,b):
 a = int(a)
 b = int(b)
 return a + b

parsedates.set_callback(parse)
parsedates.parse_date("one")
