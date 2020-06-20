from z3 import *


s = Solver()

key = BitVec('key',32)

s.add(51^ key + 118^ key + 51^ key + 110^ key + 95^ key + 97^ key + 95^ key + 83^ key + 55^ key + 114^ key + 48^ key + 110^ key + 71^ key + 95^ key + 112^ key + 52^ key + 115^ key + 83^ key + 119^ key + 48^ key + 82^ key + 100^ key + 95^ key + 105^ key + 53^ key + 95^ key + 110^ key + 48^ key + 84^ key + 95^ key + 115^ key + 51^ key + 67^ key + 117^ key + 82^ key + 101^ key == key)
if s.check():
	print s.model()