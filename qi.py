# 2017
# WilC
# wilz04@gmail.com

from math import sqrt
from math import log

def g(x, r):
	c = x/2.0
	a = sqrt(r**2 - c**2)
	b = r - a
	return sqrt(b**2 + c**2)

def f(x, r):
	j = int(log(x/2, 2))
	y = r*sqrt(2)
	C = 4*y
	pi = C/(2.0*r)
	print format(y, '.32f')
	print format(pi, '.64f')
	for i in range(1, j):
		y = g(y, r)
		C = (2**(i+2))*y
		pi = C/(2.0*r)
		print format(y, '.32f')
		print format(pi, '.64f')
	return y

def main():
	# file = open("pi.csv", "w")
	# buffer = ""
	
	r = 8.0
	pi = 0.0
	pj = 0.0
	# for i in range(1, 26):
	x = 4294967296
	C = x*f(x, r)
	
	pj = pi
	pi = C/(2.0*r)
	
	# buffer += str(i) + "; " + format(pi, '.14f') + "; " + format(pi - pj, '.14f') + "\n"
	
	# file.write(buffer + "\n")
	# file.close()

main()
