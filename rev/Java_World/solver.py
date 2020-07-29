from z3 import *

#Using z3 solver to determine key value
s = Solver()

key = Int('key')

s.add(((key + 73) + (key + 95) + (key + 98) + (key + 51) + (key + 108) + (key + 49) + (key + 69) + (key + 118) + (key + 51) + (key + 95) + (key + 116) + (key + 72) + (key + 52) + (key + 116) + (key + 95) + (key + 106) + (key + 52) + (key + 118) + (key + 65) + (key + 95) + (key + 105) + (key + 53) + (key + 95) + (key + 65) + (key + 119) + (key + 51) + (key + 83) + (key + 48) + (key + 109) + (key + 69) + (key + 95) + (key + 58) + (key + 68) + (key + 68) + (key + 68) + (key + 68)) == 257940)

try:
	if s.check():
		print s.model()
except Exception:
	print "failed"