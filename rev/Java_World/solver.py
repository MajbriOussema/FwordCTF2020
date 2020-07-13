from z3 import *


s = Solver()

key = BitVec('key',32)

s.add(((key ^ 51) + (key ^ 118) + (key ^ 51) + (key ^ 110) + (key ^ 95) + (key ^ 97) + (key ^ 95) + (key ^ 83) + (key ^ 55) + (key ^ 114) + (key ^ 48) + (key ^ 110) + (key ^ 71) + (key ^ 95) + (key ^ 112) + (key ^ 52)) == 1251)
try:
	if s.check():
		print s.model()
except Exception:
	print "failed"